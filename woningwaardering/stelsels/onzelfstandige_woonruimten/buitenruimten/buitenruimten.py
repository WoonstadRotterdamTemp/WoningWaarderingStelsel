import warnings
from collections import defaultdict
from datetime import date
from decimal import Decimal
from typing import Generator

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.criterium_id import CriteriumId, GedeeldMetSoort
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.utils import (
    classificeer_ruimte,
    gedeeld_met_eenheden,
    gedeeld_met_onzelfstandige_woonruimten,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheidbericht,
    EenhedenRuimte,
    WoningwaarderingCriteriumSleutels,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Meeteenheid,
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


class Buitenruimten(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.buitenruimten  # verkeerde parent, zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
        super().__init__(
            begindatum=date.fromisoformat("2024-07-01"),
            einddatum=date.max,
            peildatum=peildatum,
        )

    def waardeer(
        self,
        eenheid: EenhedenEenheidbericht,
        woningwaardering_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat
        | None = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=self.stelsel,
                stelselgroep=self.stelselgroep,
            )
        )

        woningwaardering_groep.woningwaarderingen = []
        gedeeld_met_counter: defaultdict[int, defaultdict[int, Decimal]] = defaultdict(
            lambda: defaultdict(Decimal)
        )  # {onzelfstandige_woonruimten: (aantal_adressen, punten)}
        gedeeld_met_m2_som: defaultdict[int, defaultdict[int, Decimal]] = defaultdict(
            lambda: defaultdict(Decimal)
        )  # {onzelfstandige_woonruimten: (aantal_adressen, vierkante_meters)}

        # punten per buitenruimte
        for ruimte in eenheid.ruimten or []:
            woningwaarderingen = self._punten_voor_buitenruimte(ruimte)
            for woningwaardering in woningwaarderingen:
                if woningwaardering.criterium is None:
                    continue

                woningwaardering.criterium.id = str(
                    CriteriumId(
                        stelselgroep=self.stelselgroep,
                        ruimte_id=ruimte.id,
                    )
                )

                if (ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1) < 2 and (
                    ruimte.gedeeld_met_aantal_eenheden or 1
                ) < 2:
                    woningwaardering.criterium.bovenliggende_criterium = (
                        WoningwaarderingCriteriumSleutels(
                            id=str(
                                CriteriumId(
                                    stelselgroep=self.stelselgroep,
                                    gedeeld_met_aantal=1,
                                    is_totaal=True,
                                )
                            )
                        )
                    )
                elif (ruimte.gedeeld_met_aantal_eenheden or 1) > 1:
                    woningwaardering.criterium.bovenliggende_criterium = WoningwaarderingCriteriumSleutels(
                        id=str(
                            CriteriumId(
                                stelselgroep=self.stelselgroep,
                                gedeeld_met_aantal=ruimte.gedeeld_met_aantal_eenheden,
                                gedeeld_met_soort=GedeeldMetSoort.adressen,
                                is_totaal=True,
                            )
                        )
                    )
                elif (ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1) > 1:
                    woningwaardering.criterium.bovenliggende_criterium = WoningwaarderingCriteriumSleutels(
                        id=str(
                            CriteriumId(
                                stelselgroep=self.stelselgroep,
                                gedeeld_met_aantal=ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten,
                                gedeeld_met_soort=GedeeldMetSoort.onzelfstandige_woonruimten,
                                is_totaal=True,
                            )
                        )
                    )

                if woningwaardering.punten is not None:
                    gedeeld_met_counter[
                        ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
                    ][ruimte.gedeeld_met_aantal_eenheden or 1] += Decimal(
                        str(woningwaardering.punten)
                    )

                gedeeld_met_m2_som[
                    ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
                ][ruimte.gedeeld_met_aantal_eenheden or 1] += Decimal(
                    str(
                        woningwaardering.aantal
                        if isinstance(woningwaardering.aantal, float)
                        else 0
                    )
                )

                woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        # minimaal 2 punten bij aanwezigheid van privé buitenruimten
        if (
            result := self._prive_buitenruimten_aanwezig(
                eenheid, woningwaardering_groep
            )
        ) is not None:
            woningwaardering_groep.woningwaarderingen.append(result)
            if result.punten is not None:
                gedeeld_met_counter[1][1] += Decimal(str(result.punten))

        # maak (sub)totalen
        for aantal_onz, aantal_adressen_punten in gedeeld_met_counter.items():
            for aantal_adressen, punten in aantal_adressen_punten.items():
                woningwaardering = WoningwaarderingResultatenWoningwaardering(
                    punten=float(punten),
                    aantal=float(gedeeld_met_m2_som[aantal_onz][aantal_adressen])
                    if gedeeld_met_m2_som[aantal_onz][aantal_adressen] > 0
                    else None,
                )

                if aantal_onz == 1 and aantal_adressen == 1:
                    woningwaardering.criterium = (
                        WoningwaarderingResultatenWoningwaarderingCriterium(
                            naam="Totaal (privé)",
                            id=str(
                                CriteriumId(
                                    stelselgroep=self.stelselgroep,
                                    gedeeld_met_aantal=1,
                                    is_totaal=True,
                                )
                            ),
                        )
                    )
                    woningwaardering.criterium.meeteenheid = (
                        Meeteenheid.vierkante_meter_m2
                    )
                    woningwaardering_groep.woningwaarderingen.append(woningwaardering)

                elif aantal_adressen > 1:
                    woningwaardering.criterium = (
                        WoningwaarderingResultatenWoningwaarderingCriterium(
                            naam=f"Totaal (gedeeld met {aantal_adressen} adressen)",
                            id=str(
                                CriteriumId(
                                    stelselgroep=self.stelselgroep,
                                    gedeeld_met_aantal=aantal_adressen,
                                    gedeeld_met_soort=GedeeldMetSoort.adressen,
                                    is_totaal=True,
                                )
                            ),
                        )
                    )
                    woningwaardering.criterium.meeteenheid = (
                        Meeteenheid.vierkante_meter_m2
                    )
                    if aantal_onz > 1:
                        woningwaardering.criterium.bovenliggende_criterium = WoningwaarderingCriteriumSleutels(
                            id=str(
                                CriteriumId(
                                    stelselgroep=self.stelselgroep,
                                    gedeeld_met_aantal=aantal_onz,
                                    gedeeld_met_soort=GedeeldMetSoort.onzelfstandige_woonruimten,
                                    is_totaal=True,
                                )
                            )
                        )

                    woningwaardering_groep.woningwaarderingen.append(woningwaardering)

            if aantal_onz > 1:
                woningwaardering = WoningwaarderingResultatenWoningwaardering(
                    punten=float(sum(aantal_adressen_punten.values())),
                    aantal=float(sum(gedeeld_met_m2_som[aantal_onz].values())),
                )
                woningwaardering.criterium = WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=f"Totaal (gedeeld met {aantal_onz} onzelfstandige woonruimten)",
                    id=str(
                        CriteriumId(
                            stelselgroep=self.stelselgroep,
                            gedeeld_met_aantal=aantal_onz,
                            gedeeld_met_soort=GedeeldMetSoort.onzelfstandige_woonruimten,
                            is_totaal=True,
                        )
                    ),
                    meeteenheid=Meeteenheid.vierkante_meter_m2,
                )
                woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        woningwaardering_groep.punten = float(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
                and woningwaardering.criterium is not None
                and woningwaardering.criterium.bovenliggende_criterium is None
            )
        )

        if geen_buitenruimten := self._geen_buitenruimten(woningwaardering_groep):
            logger.info(
                f"Eenheid ({eenheid.id}): geen buitenruimten aanwezig, {geen_buitenruimten.punten} punten voor {self.stelselgroep.naam}."
            )
            woningwaardering_groep.woningwaarderingen.append(geen_buitenruimten)
            woningwaardering_groep.punten += float(
                Decimal(str(geen_buitenruimten.punten))
            )

        # maximaal 15 punten
        elif maximering := self._maximering(eenheid, woningwaardering_groep):
            woningwaardering_groep.woningwaarderingen.append(maximering)
            woningwaardering_groep.punten += float(Decimal(str(maximering.punten)))

        # rond af op kwarten
        woningwaardering_groep.punten = float(
            utils.rond_af_op_kwart(woningwaardering_groep.punten)
        )

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep

    def _geen_buitenruimten(
        self, woningwaardering_groep: WoningwaarderingResultatenWoningwaarderingGroep
    ) -> WoningwaarderingResultatenWoningwaardering | None:
        """Een aftrek van 5 punten wordt toegepast als de woning in het geheel geen privé-buitenruimte, gemeenschappelijk buitenruimte of loggia heeft.

        Args:
            woningwaardering_groep (WoningwaarderingResultatenWoningwaarderingGroep): Woningwaardering groep van buitenruimten.

        Returns:
            WoningwaarderingResultatenWoningwaardering | None: Woningwaardering met -5 punten als er geen buitenruimten aanwezig zijn.
        """
        if not woningwaardering_groep.woningwaarderingen:
            woningwaardering = WoningwaarderingResultatenWoningwaardering()
            woningwaardering.criterium = (
                WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Geen buitenruimten",
                    id=str(
                        CriteriumId(
                            stelselgroep=self.stelselgroep,
                            criterium="geen_buitenruimten",
                        )
                    ),
                )
            )
            woningwaardering.punten = -5.0
            return woningwaardering
        return None

    def _maximering(
        self,
        eenheid: EenhedenEenheidbericht,
        woningwaardering_groep: WoningwaarderingResultatenWoningwaarderingGroep,
    ) -> WoningwaarderingResultatenWoningwaardering | None:
        """Berekent de maximering voor Buitenruimten. Maximaal 15 punten toegestaan.


        Args:
            eenheid (EenhedenEenheidbericht): Eenheid waarvoor de maximering berekend wordt.
            woningwaardering_groep (WoningwaarderingResultatenWoningwaarderingGroep): Woningwaardering groep van buitenruimten.

        Returns:
            WoningwaarderingResultatenWoningwaardering | None: Maximering als er een maximering is.
        """
        max_punten = Decimal("15")
        punten = Decimal(str(woningwaardering_groep.punten or "0"))
        if punten > max_punten:
            aftrek = max_punten - punten

            logger.info(
                f"Eenheid ({eenheid.id}): maximaal aantal punten voor {self.stelselgroep.naam} overschreden ({punten} > {max_punten}). {aftrek} punt(en) aftrek."
            )

            woningwaardering = WoningwaarderingResultatenWoningwaardering()
            woningwaardering.criterium = (
                WoningwaarderingResultatenWoningwaarderingCriterium(
                    id=str(
                        CriteriumId(
                            stelselgroep=self.stelselgroep,
                            criterium="maximaal_15_punten",
                        )
                    ),
                    naam="Maximaal 15 punten",
                )
            )
            woningwaardering.punten = float(aftrek)
            return woningwaardering

        logger.debug(
            f"Eenheid ({eenheid.id}): geen maximaal aantal punten voor {self.stelselgroep.naam} overschreden ({punten} <= {max_punten})."
        )
        return None

    def _punten_voor_buitenruimte(
        self,
        ruimte: EenhedenRuimte,
    ) -> Generator[WoningwaarderingResultatenWoningwaardering, None, None]:
        """Berekent de punten voor een ruimte voor rubriek Buitenruimten

        0.75 punten per m2 voor gedeelde buitenruimten.
        0.35 punten per m2 voor privé buitenruimten.

        Ruimte moet minimaal een afmeting hebben van 2 m x 1,5 m x 1,5 m (hoogte, lengte, breedte).
        Parkeerplaatsen worden niet meegewaardeerd als ze gedeeld zijn met andere eenheden.

        Args:
            ruimte (EenhedenRuimte): Ruimte waarvoor de punten berekend worden.

        Yields:
            WoningwaarderingResultatenWoningwaardering: Punten voor de buitenruimte.
        """
        if classificeer_ruimte(ruimte) == Ruimtesoort.buitenruimte or (
            ruimte.detail_soort
            in [
                Ruimtedetailsoort.stalling_extern,
                Ruimtedetailsoort.stalling_intern,
            ]
        ):
            if not ruimte.oppervlakte:
                warnings.warn(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen oppervlakte",
                    UserWarning,
                )
                return
            if gedeeld_met_eenheden(ruimte):
                # Gemeenschappelijke buitenruimten hebben een minimumafmeting van 2 m x 1,5 m, 1,5 m (hoogte, lengte, breedte)
                if not (ruimte.lengte and ruimte.breedte):
                    warnings.warn(
                        f"Ruimte '{ruimte.naam}' ({ruimte.id}) is een gedeelde buitenruimte, maar heeft geen lengte en/of breedte, terwijl daar wel eisen voor zijn: (h, l, b) >= (2, 1.5, 1.5).",
                        UserWarning,
                    )
                if (
                    (ruimte.hoogte and ruimte.hoogte < 2)
                    or (ruimte.lengte and ruimte.lengte < 1.5)
                    or (ruimte.breedte and ruimte.breedte < 1.5)
                ):
                    logger.debug(
                        f"Ruimte '{ruimte.naam}' ({ruimte.id}) is een met {ruimte.gedeeld_met_aantal_eenheden} gedeelde buitenruimte met een (h, l, b) kleiner dan (2, 1.5, 1.5) en telt daarom niet mee voor {self.stelselgroep.naam}."
                    )
                    return
            # Parkeerplaatsen worden alleen gewaardeerd als ze niet gedeeld zijn met andere eenheden
            if (
                ruimte.detail_soort
                == Ruimtedetailsoort.parkeerplaats  # parkeerplaats heeft als ruimtesoort buitenruimte
                and gedeeld_met_eenheden(ruimte)
            ):
                logger.debug(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) is een gedeelde parkeerplaats en telt daarom niet mee voor {self.stelselgroep.naam}."
                )
                return

            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) van {ruimte.oppervlakte:.2f}m2 telt mee voor {self.stelselgroep.naam}."
            )
            woningwaardering = WoningwaarderingResultatenWoningwaardering()
            woningwaardering.criterium = (
                WoningwaarderingResultatenWoningwaarderingCriterium(
                    meeteenheid=Meeteenheid.vierkante_meter_m2,
                    naam=ruimte.naam
                    if not gedeeld_met_eenheden(ruimte)
                    else f"{ruimte.naam}",
                    id=str(
                        CriteriumId(
                            stelselgroep=self.stelselgroep,
                            ruimte_id=ruimte.id,
                            gedeeld_met_aantal=ruimte.gedeeld_met_aantal_eenheden,
                            gedeeld_met_soort=GedeeldMetSoort.adressen,
                        )
                    ),
                )
            )
            woningwaardering.aantal = float(
                utils.rond_af(ruimte.oppervlakte, decimalen=2)
            )
            # Voor privé-buitenruimten worden in ieder geval 2 punten toegekend en vervolgens per vierkante meter 0,75 punt.
            # De in ieder geval 2 punten worden verderop toegevoegd.
            if gedeeld_met_onzelfstandige_woonruimten(ruimte):
                woningwaardering.punten = float(
                    Decimal(str(ruimte.oppervlakte))
                    * Decimal("0.75")
                    / Decimal(str(ruimte.gedeeld_met_aantal_eenheden or 1))
                    / Decimal(str(ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten))
                )
            else:
                woningwaardering.punten = float(
                    Decimal(str(ruimte.oppervlakte))
                    * Decimal("0.35")
                    / Decimal(str(ruimte.gedeeld_met_aantal_eenheden or 1))
                )
            yield woningwaardering
        else:
            logger.debug(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt niet mee voor {self.stelselgroep.naam}."
            )

    def _prive_buitenruimten_aanwezig(
        self,
        eenheid: EenhedenEenheidbericht,
        woningwaardering_groep: WoningwaarderingResultatenWoningwaarderingGroep,
    ) -> WoningwaarderingResultatenWoningwaardering | None:
        """Kent 2 punten toe bij de aanwezigheid van privé buitenruimten.

        Args:
            eenheid (EenhedenEenheidbericht): Eenheid waarvoor de punten berekend worden.
            woningwaardering_groep (WoningwaarderingResultatenWoningwaarderingGroep): Woningwaardering groep van buitenruimten.

        Returns:
            WoningwaarderingResultatenWoningwaardering | None: Woningwaardering met 2 punten als er privé buitenruimten aanwezig zijn.
        """
        # 2 punten bij de aanwezigheid van privé buitenruimten
        if woningwaardering_groep.woningwaarderingen and any(
            classificeer_ruimte(ruimte) == Ruimtesoort.buitenruimte
            and not gedeeld_met_eenheden(ruimte)
            and not gedeeld_met_onzelfstandige_woonruimten(ruimte)
            for ruimte in eenheid.ruimten or []
        ):
            woningwaardering = WoningwaarderingResultatenWoningwaardering()
            woningwaardering.criterium = (
                WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Privé buitenruimten aanwezig",
                    bovenliggende_criterium=WoningwaarderingCriteriumSleutels(
                        id=str(
                            CriteriumId(
                                stelselgroep=self.stelselgroep,
                                gedeeld_met_aantal=1,
                                is_totaal=True,
                            )
                        )
                    ),
                )
            )
            woningwaardering.punten = 2.0
            logger.info(
                f"Eenheid ({eenheid.id}): privé buitenruimten aanwezig, {woningwaardering.punten} punten voor {self.stelselgroep.naam}."
            )
            return woningwaardering
        logger.debug(
            f"Eenheid ({eenheid.id}): geen privé buitenruimten aanwezig voor {self.stelselgroep.naam}."
        )
        return None


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=Buitenruimten(peildatum=date(2025, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer(
            "tests/data/onzelfstandige_woonruimten/stelselgroepen/buitenruimten/input/oprit.json"
        )
