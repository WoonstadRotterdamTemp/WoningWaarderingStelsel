import warnings
from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.zelfstandige_woonruimten.utils import classificeer_ruimte
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.referentiedata.meeteenheid import Meeteenheid
from woningwaardering.vera.referentiedata.ruimtesoort import Ruimtesoort


class Buitenruimten(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.buitenruimten
        super().__init__(
            begindatum=date.fromisoformat("2024-07-01"),
            einddatum=date.max,
            peildatum=peildatum,
        )

    def bereken(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten.value,
                stelselgroep=Woningwaarderingstelselgroep.buitenruimten.value,
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        buitenruimten_aanwezig = False
        for ruimte in eenheid.ruimten or []:
            if classificeer_ruimte(ruimte) == Ruimtesoort.buitenruimte:
                buitenruimten_aanwezig = True
                gedeelde_ruimte = (
                    ruimte.gedeeld_met_aantal_eenheden
                    and ruimte.gedeeld_met_aantal_eenheden >= 2
                )
                if not ruimte.oppervlakte:
                    warnings.warn(
                        f"Ruimte {ruimte.naam} ({ruimte.id}) heeft geen oppervlakte",
                        UserWarning,
                    )
                    continue

                woningwaardering = WoningwaarderingResultatenWoningwaardering()
                if gedeelde_ruimte:  # gedeelde buitenruimte
                    logger.info(
                        f"Ruimte {ruimte.naam} ({ruimte.id}) is een met {ruimte.gedeeld_met_aantal_eenheden} gedeelde buitenruimte met oppervlakte {ruimte.oppervlakte}m2 en wordt gewaardeerd onder stelselgroep {Woningwaarderingstelselgroep.buitenruimten.naam}."
                    )
                    woningwaardering.aantal = utils.rond_af(
                        ruimte.oppervlakte / ruimte.gedeeld_met_aantal_eenheden,
                        decimalen=2,
                    )
                    woningwaardering.punten = float(
                        utils.rond_af(
                            ruimte.oppervlakte
                            * 0.75
                            / ruimte.gedeeld_met_aantal_eenheden,
                            decimalen=2,
                        )
                    )
                    woningwaardering.criterium = WoningwaarderingResultatenWoningwaarderingCriterium(
                        meeteenheid=Meeteenheid.vierkante_meter_m2.value,
                        naam=f"{ruimte.naam} (gedeeld met {ruimte.gedeeld_met_aantal_eenheden})",
                    )
                else:  # privé buitenruimte
                    logger.info(
                        f"Ruimte {ruimte.naam} ({ruimte.id}) is een privé-buitenruimte met oppervlakte {ruimte.oppervlakte}m2 en wordt gewaardeerd onder stelselgroep {Woningwaarderingstelselgroep.buitenruimten.naam}."
                    )
                    woningwaardering.criterium = (
                        WoningwaarderingResultatenWoningwaarderingCriterium(
                            meeteenheid=Meeteenheid.vierkante_meter_m2.value,
                            naam=f"{ruimte.naam} (privé)",
                        )
                    )
                    woningwaardering.aantal = utils.rond_af(
                        ruimte.oppervlakte, decimalen=2
                    )
                    woningwaardering.punten = float(
                        utils.rond_af(ruimte.oppervlakte * 0.35, decimalen=2)
                    )

                woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        punten = utils.rond_af(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            ),
            decimalen=0,
        )
        max_punten = 15
        if punten > max_punten:  # maximaal 15 punten
            aftrek = max_punten - punten

            logger.info(
                f"Eenheid {eenheid.id}: maximaal aantal punten voor buitenruimten overschreden ({punten} > {max_punten}). Een aftrek van {aftrek} punt(en) wordt toegepast."
            )
            punten += aftrek
            woningwaardering = WoningwaarderingResultatenWoningwaardering()
            woningwaardering.criterium = (
                WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Maximaal 15 punten",
                )
            )
            woningwaardering.punten = float(aftrek)
            woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        if not buitenruimten_aanwezig:
            logger.info(
                f"Eenheid {eenheid.id} heeft geen buitenruimten of loggia. Vijf minpunten voor geen buitenruimten toegepast."
            )
            woningwaardering = WoningwaarderingResultatenWoningwaardering()
            woningwaardering.criterium = (
                WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Geen buitenruimten",
                )
            )
            woningwaardering.punten = -5
            woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid {eenheid.id} wordt gewaardeerd met {woningwaardering_groep.punten} punten voor stelselgroep {Woningwaarderingstelselgroep.buitenruimten.naam}"
        )
        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    logger.enable("woningwaardering")

    buitenruimten = Buitenruimten(peildatum=date.fromisoformat("2024-07-01"))

    with open(
        "tests/data/zelfstandige_woonruimten/stelselgroepen/prive_buitenruimten/input/gedeelde_buitenruimtes.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    woningwaardering_resultaat = buitenruimten.bereken(eenheid)

    print(
        woningwaardering_resultaat.model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )

    tabel = utils.naar_tabel(woningwaardering_resultaat)

    print(tabel)
