import warnings
from collections import defaultdict
from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.criterium_id import CriteriumId, GedeeldMetSoort
from woningwaardering.stelsels.gedeelde_logica import (
    waardeer_gemeenschappelijke_parkeerruimte,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheidbericht,
    WoningwaarderingCriteriumSleutels,
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


class GemeenschappelijkeParkeerruimten(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten  # verkeerde parent, zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
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
                stelselgroep=self.stelselgroep,  # verkeerde parent zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
            )
        )

        if not eenheid.ruimten:
            warnings.warn(f"Eenheid ({eenheid.id}): geen ruimten gevonden")
            return woningwaardering_groep

        woningwaardering_groep.woningwaarderingen = []

        gedeeld_met_counter: defaultdict[int, defaultdict[str, Decimal]] = defaultdict(
            lambda: defaultdict(Decimal)
        )

        for ruimte in eenheid.ruimten:
            waarderingen_zelfstandig = waardeer_gemeenschappelijke_parkeerruimte(ruimte)
            if waarderingen_zelfstandig is not None:
                for waardering in list(waarderingen_zelfstandig):
                    if waardering is None:
                        continue

                    # Een parkeerruimte waartoe bewoners van één adres op grond van de huurovereenkomst exclusieve toegang hebben, wordt gewaardeerd volgens rubriek 2,  (bijvoorbeeld een garagebox behorende tot de woning) of rubriek 8 (bijvoorbeeld een oprit exclusief behorende tot de woning).
                    if not utils.gedeeld_met_eenheden(ruimte):
                        logger.debug(
                            f"Ruimte '{ruimte.naam}' ({ruimte.id}) is niet gedeeld met andere eenheden en telt daarom niet voor {self.stelselgroep.naam}."
                        )
                        continue

                    gedeeld_met_aantal_onzelfstandige_woonruimten = (
                        ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
                    )

                    if waardering.aantal is not None:
                        gedeeld_met_counter[
                            gedeeld_met_aantal_onzelfstandige_woonruimten
                        ]["aantal"] += Decimal(str(waardering.aantal))
                    if waardering.punten is not None:
                        gedeeld_met_counter[
                            gedeeld_met_aantal_onzelfstandige_woonruimten
                        ]["punten"] += Decimal(str(waardering.punten))

                    waardering.punten = float(
                        utils.rond_af(
                            Decimal(str(waardering.punten))
                            / Decimal(
                                str(gedeeld_met_aantal_onzelfstandige_woonruimten)
                            ),
                            decimalen=2,
                        )
                    )
                    if waardering.criterium is not None:
                        waardering.criterium.bovenliggende_criterium = WoningwaarderingCriteriumSleutels(
                            id=str(
                                CriteriumId(
                                    stelselgroep=self.stelselgroep,
                                    gedeeld_met_aantal=gedeeld_met_aantal_onzelfstandige_woonruimten,
                                    gedeeld_met_soort=GedeeldMetSoort.onzelfstandige_woonruimten,
                                    is_totaal=True,
                                )
                            ),
                        )
                        woningwaardering_groep.woningwaarderingen.append(waardering)

        for (
            gedeeld_met_aantal_onzelfstandige_woonruimten,
            count,
        ) in gedeeld_met_counter.items():
            woningwaardering_groep.woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        id=str(
                            CriteriumId(
                                stelselgroep=self.stelselgroep,
                                gedeeld_met_aantal=gedeeld_met_aantal_onzelfstandige_woonruimten,
                                gedeeld_met_soort=GedeeldMetSoort.onzelfstandige_woonruimten,
                                is_totaal=True,
                            )
                        ),
                        naam=f"Totaal gedeeld met {gedeeld_met_aantal_onzelfstandige_woonruimten} onzelfstandige woonruimten",
                    ),
                    aantal=float(count["aantal"]),
                    punten=float(
                        utils.rond_af(
                            Decimal(str(count["punten"]))
                            / Decimal(
                                str(gedeeld_met_aantal_onzelfstandige_woonruimten)
                            ),
                            decimalen=2,
                        )
                    ),
                )
            )

        totaal_punten = utils.rond_af_op_kwart(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if (
                    woningwaardering.punten is not None
                    and woningwaardering.criterium
                    and woningwaardering.criterium.bovenliggende_criterium is None
                )
            )
        )

        woningwaardering_groep.punten = float(totaal_punten)

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=GemeenschappelijkeParkeerruimten(peildatum=date(2025, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer(
            "tests/data/onzelfstandige_woonruimten/stelselgroepen/gemeenschappelijke_parkeerruimten/input/voorbeeld_beleidsboek.json"
        )
