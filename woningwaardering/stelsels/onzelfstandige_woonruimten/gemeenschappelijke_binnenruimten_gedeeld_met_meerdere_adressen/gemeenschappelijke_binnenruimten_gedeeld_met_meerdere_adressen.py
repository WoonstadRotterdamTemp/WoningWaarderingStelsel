import warnings
from collections import defaultdict
from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.criterium_id import CriteriumId, GedeeldMetSoort
from woningwaardering.stelsels.gedeelde_logica import (
    waardeer_keuken,
    waardeer_oppervlakte_van_overige_ruimte,
    waardeer_oppervlakte_van_vertrek,
    waardeer_verkoeling_en_verwarming,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten.sanitair import (
    Sanitair as OnzelfstandigeWoonruimtenSanitair,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheidbericht,
    EenhedenRuimte,
    Referentiedata,
    WoningwaarderingCriteriumSleutels,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Doelgroep,
    Meeteenheid,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


class GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen
        super().__init__(
            begindatum=date.fromisoformat("2024-07-01"),
            einddatum=date.max,
            peildatum=peildatum,
        )

    def waardeer(
        self,
        eenheid: EenhedenEenheidbericht,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=self.stelsel,
                stelselgroep=self.stelselgroep,
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        if zorgwoning := self._zorgwoning(eenheid):
            woningwaardering_groep.woningwaarderingen.append(zorgwoning)
        else:
            gedeelde_ruimten = [
                ruimte
                for ruimte in eenheid.ruimten or []
                if ruimte.gedeeld_met_aantal_eenheden is not None
                and ruimte.gedeeld_met_aantal_eenheden > 1
            ]

            gedeeld_met_punten: defaultdict[int, defaultdict[int, Decimal]] = (
                defaultdict(lambda: defaultdict(Decimal))
            )  # {onzelfstandige_woonruimten: (aantal_adressen, punten)}

            # oppervlakte waarderingen
            gedeeld_met_punten, oppervlakte_waarderingen = (
                self._oppervlakte_waarderingen(gedeelde_ruimten, gedeeld_met_punten)
            )
            woningwaardering_groep.woningwaarderingen.extend(
                list(oppervlakte_waarderingen)
            )

            # verkoeling en verwarming waarderingen
            gedeeld_met_punten, verkoeling_en_verwarming_waarderingen = (
                self._verkoeling_en_verwarming_waarderingen(
                    gedeelde_ruimten, gedeeld_met_punten
                )
            )
            woningwaardering_groep.woningwaarderingen.extend(
                list(verkoeling_en_verwarming_waarderingen)
            )

            # keuken waarderingen
            gedeeld_met_punten, keuken_waarderingen = self._keuken_waarderingen(
                gedeelde_ruimten, gedeeld_met_punten
            )
            woningwaardering_groep.woningwaarderingen.extend(list(keuken_waarderingen))

            # sanitair waarderingen
            gedeeld_met_punten, sanitair_waarderingen = self._sanitair_waarderingen(
                gedeelde_ruimten, gedeeld_met_punten
            )
            woningwaardering_groep.woningwaarderingen.extend(
                list(sanitair_waarderingen)
            )

            # (sub)totaal waarderingen
            for (
                aantal_onzelfstandige_woonruimten,
                punten_per_aantal_adressen,
            ) in gedeeld_met_punten.items():
                onz_punten = Decimal("0")

                bovenliggende_criterium_id = str(
                    CriteriumId(
                        stelselgroep=self.stelselgroep,
                        gedeeld_met_aantal=aantal_onzelfstandige_woonruimten,
                        gedeeld_met_soort=GedeeldMetSoort.onzelfstandige_woonruimten,
                        is_totaal=True,
                    )
                )

                for aantal_adressen, punten in punten_per_aantal_adressen.items():
                    onz_punten += punten
                    woningwaardering_groep.woningwaarderingen.append(
                        self._maak_woningwaardering(
                            punten=punten,
                            id=str(
                                CriteriumId(
                                    stelselgroep=self.stelselgroep,
                                    gedeeld_met_aantal=aantal_adressen,
                                    gedeeld_met_soort=GedeeldMetSoort.adressen,
                                    is_totaal=True,
                                )
                            ),
                            criterium=f"Totaal (gedeeld met {aantal_adressen} adressen)",
                            bovenliggende_criterium_id=bovenliggende_criterium_id,
                        )
                    )

                woningwaardering_groep.woningwaarderingen.append(
                    self._maak_woningwaardering(
                        punten=onz_punten,
                        id=bovenliggende_criterium_id,
                        criterium=f"Totaal (gedeeld met {aantal_onzelfstandige_woonruimten} onzelfstandige {'woonruimten' if aantal_onzelfstandige_woonruimten > 1 else 'woonruimte'})",
                    )
                )

        punten = utils.rond_af_op_kwart(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
                and woningwaardering.criterium
                and woningwaardering.criterium.bovenliggende_criterium is None
            )
        )

        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid {eenheid.id} krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep

    def _zorgwoning(
        self, eenheid: EenhedenEenheidbericht
    ) -> WoningwaarderingResultatenWoningwaardering | None:
        """
        Beleidsboek: De ervaring leert dat bij het waarderen van de gemeenschappelijke ruimten en
        voorzieningen in een zorgwoning of woon/zorgcomplex de waardering per woning
        veelal uitkomt op een totaal van ongeveer 3 punten. Om arbeidsintensief
        meetwerk te voorkomen waardeert de Huurcommissie in dat geval een waardering
        van 3 punten per woning.

        Args:
            eenheid (EenhedenEenheidbericht): Eenheid

        Returns:
            WoningwaarderingResultatenWoningwaardering | None: Woningwaardering van 3 punten voor een zorgwoning of None als de eenheid geen zorgwoning is
        """
        if eenheid.doelgroep == Doelgroep.zorg:
            logger.info(
                f"Eenheid {eenheid.id} is een zorgwoning en krijgt 3 punten voor {self.stelselgroep.naam}"
            )
            return WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Zorgwoning",
                    id=str(
                        CriteriumId(
                            stelselgroep=self.stelselgroep,
                            criterium="zorgwoning",
                        )
                    ),
                ),
                punten=3.0,
            )
        logger.debug(
            f"Eenheid {eenheid.id} is geen zorgwoning en krijgt daarvoor geen punten voor {self.stelselgroep.naam}"
        )
        return None

    def _maak_woningwaardering(
        self,
        punten: Decimal | None,
        criterium: str,
        bovenliggende_criterium_id: str | None = None,
        aantal: float | None = None,
        meeteenheid: Referentiedata | None = None,
        id: str | None = None,
    ) -> WoningwaarderingResultatenWoningwaardering:
        woningwaardering = WoningwaarderingResultatenWoningwaardering(
            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                id=id,
                meeteenheid=meeteenheid,
                naam=criterium,
            ),
            aantal=aantal,
            punten=punten,
        )
        if bovenliggende_criterium_id and woningwaardering.criterium:
            woningwaardering.criterium.bovenliggende_criterium = (
                WoningwaarderingCriteriumSleutels(id=bovenliggende_criterium_id)
            )
        return woningwaardering

    def _oppervlakte_waarderingen(
        self,
        ruimten: list[EenhedenRuimte],
        gedeeld_met_punten: defaultdict[int, defaultdict[int, Decimal]],
    ) -> tuple[
        defaultdict[int, defaultdict[int, Decimal]],
        list[WoningwaarderingResultatenWoningwaardering],
    ]:
        waarderigen = []
        for ruimte in ruimten:
            aantal_onzelfstandige_woonruimten = (
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            )

            aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden or 1

            oppervlakte_vertrekken = list(waardeer_oppervlakte_van_vertrek(ruimte))

            oppervlakte_van_overige_ruimten = list(
                waardeer_oppervlakte_van_overige_ruimte(ruimte)
            )

            if oppervlakte_vertrekken or oppervlakte_van_overige_ruimten:
                if oppervlakte_vertrekken:
                    oppervlakte_resultaat = oppervlakte_vertrekken[0]
                    punten_per_m2 = Decimal("1.0")
                else:
                    oppervlakte_resultaat = oppervlakte_van_overige_ruimten[0]
                    punten_per_m2 = Decimal("0.75")

                punten = (
                    Decimal(str(oppervlakte_resultaat.aantal))
                    * punten_per_m2
                    / Decimal(str(aantal_eenheden))
                    / Decimal(str(aantal_onzelfstandige_woonruimten))
                )
                gedeeld_met_punten[aantal_onzelfstandige_woonruimten][
                    aantal_eenheden
                ] += punten

                if ruimte.soort is None:
                    warnings.warn(f"Geen soort gevonden voor ruimte {ruimte.id}")
                    continue
                if oppervlakte_resultaat.criterium is None:
                    warnings.warn(f"Geen criterium gevonden voor ruimte {ruimte.id}")
                    continue

                waarderigen.append(
                    self._maak_woningwaardering(
                        punten=punten,
                        criterium=f"{oppervlakte_resultaat.criterium.naam}: {ruimte.soort.naam}",
                        bovenliggende_criterium_id=str(
                            CriteriumId(
                                stelselgroep=self.stelselgroep,
                                gedeeld_met_aantal=aantal_eenheden,
                                gedeeld_met_soort=GedeeldMetSoort.adressen,
                                is_totaal=True,
                            )
                        ),
                        aantal=oppervlakte_resultaat.aantal,
                        meeteenheid=Meeteenheid.vierkante_meter_m2,
                        id=str(
                            CriteriumId(
                                stelselgroep=self.stelselgroep,
                                ruimte_id=ruimte.id,
                            )
                        ),
                    )
                )

        return gedeeld_met_punten, waarderigen

    def _verkoeling_en_verwarming_waarderingen(
        self,
        ruimten: list[EenhedenRuimte],
        gedeeld_met_punten: defaultdict[int, defaultdict[int, Decimal]],
    ) -> tuple[
        defaultdict[int, defaultdict[int, Decimal]],
        list[WoningwaarderingResultatenWoningwaardering],
    ]:
        waarderingen = []

        resultaten = list(waardeer_verkoeling_en_verwarming(ruimten))
        for ruimte, resultaat in resultaten:
            aantal_onzelfstandige_woonruimten = (
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            )
            aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden or 1

            punten = (
                Decimal(str(resultaat.punten))
                / Decimal(str(aantal_eenheden))
                / Decimal(str(aantal_onzelfstandige_woonruimten))
            )

            gedeeld_met_punten[aantal_onzelfstandige_woonruimten][aantal_eenheden] += (
                punten
            )
            criterium = resultaat.criterium
            if ruimte.soort is None:
                warnings.warn(f"Geen soort gevonden voor ruimte {ruimte.id}")
                continue
            if criterium is None:
                warnings.warn(f"Geen criterium gevonden voor ruimte {ruimte.id}")
                continue

            if resultaat.punten and resultaat.punten < 0:
                criterium_naam = f"{criterium.naam.rstrip(':') if criterium.naam else ''} voor {criterium.bovenliggende_criterium.id.split('__')[-1].lower().replace('_', ' ') if criterium.bovenliggende_criterium and criterium.bovenliggende_criterium.id else ''}"
            else:
                criterium_naam = f"{criterium.naam}: {criterium.bovenliggende_criterium.id.split('__')[-1].capitalize().replace('_', ' ') if criterium.bovenliggende_criterium and criterium.bovenliggende_criterium.id else ''}"

            waarderingen.append(
                self._maak_woningwaardering(
                    punten=punten,
                    criterium=criterium_naam,
                    bovenliggende_criterium_id=str(
                        CriteriumId(
                            stelselgroep=self.stelselgroep,
                            gedeeld_met_aantal=aantal_eenheden,
                            gedeeld_met_soort=GedeeldMetSoort.adressen,
                            is_totaal=True,
                        )
                    ),
                    aantal=resultaat.aantal,
                    meeteenheid=resultaat.criterium.meeteenheid
                    if resultaat.criterium
                    else None,
                    id=str(
                        CriteriumId(
                            stelselgroep=self.stelselgroep,
                            ruimte_id=ruimte.id,
                        )
                    ),
                )
            )

        return gedeeld_met_punten, waarderingen

    def _sanitair_waarderingen(
        self,
        ruimten: list[EenhedenRuimte],
        gedeeld_met_punten: defaultdict[int, defaultdict[int, Decimal]],
    ) -> tuple[
        defaultdict[int, defaultdict[int, Decimal]],
        list[WoningwaarderingResultatenWoningwaardering],
    ]:
        woningwaarderingen: list[WoningwaarderingResultatenWoningwaardering] = []
        woningwaarderingen_met_ruimten = list(
            OnzelfstandigeWoonruimtenSanitair.genereer_woningwaarderingen(
                ruimten, self.stelselgroep
            )
        )

        if not woningwaarderingen_met_ruimten:
            return gedeeld_met_punten, woningwaarderingen

        for ruimte, waarderingen in woningwaarderingen_met_ruimten:
            for waardering in waarderingen:
                aantal_onzelfstandige_woonruimten = (
                    ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
                )
                aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden or 1

                if ruimte.soort is None:
                    warnings.warn(f"Geen soort gevonden voor ruimte {ruimte.id}")
                    continue
                if waardering.criterium is None or waardering.criterium.naam is None:
                    warnings.warn(f"Geen criterium gevonden voor ruimte {ruimte.id}")
                    continue

                punten = (
                    Decimal(str(waardering.punten))
                    / Decimal(aantal_eenheden)
                    / Decimal(str(aantal_onzelfstandige_woonruimten))
                )

                gedeeld_met_punten[aantal_onzelfstandige_woonruimten][
                    aantal_eenheden
                ] += punten

                woningwaarderingen.append(
                    self._maak_woningwaardering(
                        punten=punten,
                        criterium=f"{waardering.criterium.naam.replace(':', '').replace(' -', ':')}",
                        bovenliggende_criterium_id=str(
                            CriteriumId(
                                stelselgroep=self.stelselgroep,
                                gedeeld_met_aantal=aantal_eenheden,
                                gedeeld_met_soort=GedeeldMetSoort.adressen,
                                is_totaal=True,
                            )
                        ),
                        aantal=None,
                        meeteenheid=None,
                        id=str(
                            CriteriumId(
                                stelselgroep=self.stelselgroep,
                                ruimte_id=ruimte.id,
                            )
                        ),
                    )
                )

        return gedeeld_met_punten, woningwaarderingen

    def _keuken_waarderingen(
        self,
        ruimten: list[EenhedenRuimte],
        gedeeld_met_punten: defaultdict[int, defaultdict[int, Decimal]],
    ) -> tuple[
        defaultdict[int, defaultdict[int, Decimal]],
        list[WoningwaarderingResultatenWoningwaardering],
    ]:
        woningwaarderingen = []
        for ruimte in ruimten:
            aantal_onzelfstandige_woonruimten = (
                ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            )
            aantal_eenheden = ruimte.gedeeld_met_aantal_eenheden or 1

            waarderingen = list(waardeer_keuken(ruimte, self.stelsel))
            for waardering in waarderingen:
                if waardering.criterium is None:
                    logger.warning(
                        f"Geen criterium gevonden in waardring voor ruimte {ruimte.id}"
                    )
                    continue
                aantal_onzelfstandige_woonruimten = (
                    ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
                )

                if not waardering.punten:
                    continue

                punten = (
                    Decimal(str(waardering.punten))
                    / Decimal(str(aantal_eenheden))
                    / Decimal(str(aantal_onzelfstandige_woonruimten))
                    if waardering.punten
                    else Decimal("0")
                )
                gedeeld_met_punten[aantal_onzelfstandige_woonruimten][
                    aantal_eenheden
                ] += punten

                if waardering.criterium.naam is None:
                    criterium = f"{ruimte.naam}"
                else:
                    criterium = f"{ruimte.naam + ': ' if ruimte.naam is not None and ruimte.naam not in waardering.criterium.naam else ''}{waardering.criterium.naam}"

                woningwaarderingen.append(
                    self._maak_woningwaardering(
                        punten=punten,
                        criterium=criterium,
                        bovenliggende_criterium_id=str(
                            CriteriumId(
                                stelselgroep=self.stelselgroep,
                                gedeeld_met_aantal=aantal_eenheden,
                                gedeeld_met_soort=GedeeldMetSoort.adressen,
                                is_totaal=True,
                            )
                        ),
                        aantal=waardering.aantal,
                        meeteenheid=waardering.criterium.meeteenheid,
                        id=str(
                            CriteriumId(
                                stelselgroep=self.stelselgroep,
                                ruimte_id=ruimte.id,
                            )
                        ),
                    )
                )
        return gedeeld_met_punten, woningwaarderingen


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen(
            peildatum=date(2025, 1, 1)
        ),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer(
            "tests/data/onzelfstandige_woonruimten/stelselgroepen/gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen/input/voorbeeld_beleidsboek.json"
        )
