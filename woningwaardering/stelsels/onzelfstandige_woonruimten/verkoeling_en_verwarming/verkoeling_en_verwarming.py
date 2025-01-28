from collections import defaultdict
from datetime import date
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.criterium_id import CriteriumId, GedeeldMetSoort
from woningwaardering.stelsels.gedeelde_logica import (
    waardeer_verkoeling_en_verwarming,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.utils import (
    deel_punten_door_aantal_onzelfstandige_woonruimten,
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
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


class VerkoelingEnVerwarming(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.verkoeling_en_verwarming  # verkeerde parent, zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
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

        woningwaardering_groep.woningwaarderingen = []

        ruimten = [
            ruimte
            for ruimte in eenheid.ruimten or []
            if ruimte.gedeeld_met_aantal_eenheden is None
            or ruimte.gedeeld_met_aantal_eenheden == 1
        ]

        woningwaarderingen = list(waardeer_verkoeling_en_verwarming(ruimten))
        woningwaarderingen_totaal: list[
            tuple[EenhedenRuimte, WoningwaarderingResultatenWoningwaardering]
        ] = []
        for ruimte, woningwaardering in woningwaarderingen:
            waardering_gedeeld = list(
                deel_punten_door_aantal_onzelfstandige_woonruimten(
                    ruimte, [woningwaardering], update_criterium_naam=False
                )
            )[0]  # er is altijd maar een woningwaardering
            woningwaarderingen_totaal.append((ruimte, waardering_gedeeld))
            woningwaardering_groep.woningwaarderingen.append(waardering_gedeeld)

        woningwaardering_groep.woningwaarderingen.extend(
            list(self._maak_totalen(woningwaarderingen_totaal))
        )

        punten = utils.rond_af_op_kwart(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
                and woningwaardering.criterium
                and woningwaardering.criterium.bovenliggende_criterium is None
            ),
        )

        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep

    def _maak_totalen(
        self,
        waarderingen: list[
            tuple[EenhedenRuimte, WoningwaarderingResultatenWoningwaardering]
        ],
    ) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
        gedeeld_met_counter: defaultdict[int, defaultdict[str, Decimal]] = defaultdict(
            lambda: defaultdict(Decimal)
        )

        # {bovenliggend_criterium: {onzelfstandige_woonruimten: punten}}
        for ruimte, woningwaardering in waarderingen:
            gedeeld_met_onz = ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
            gedeeld_met_counter[gedeeld_met_onz][
                woningwaardering.criterium.bovenliggende_criterium.id
                if woningwaardering.criterium
                and woningwaardering.criterium.bovenliggende_criterium
                and woningwaardering.criterium.bovenliggende_criterium.id
                else "verkoeling_en_verwarming_default"
            ] += Decimal(str(woningwaardering.punten))

        for aantal_onz, bovenliggend_criterium_punten in gedeeld_met_counter.items():
            for criterium_id, punten in bovenliggend_criterium_punten.items():
                yield WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        id=criterium_id,
                        naam=criterium_id.split("__")[-1]
                        .capitalize()
                        .replace("_", " "),
                        bovenliggende_criterium=WoningwaarderingCriteriumSleutels(
                            id=str(
                                CriteriumId(
                                    stelselgroep=self.stelselgroep,
                                    gedeeld_met_aantal=aantal_onz,
                                    gedeeld_met_soort=GedeeldMetSoort.onzelfstandige_woonruimten,
                                    is_totaal=True,
                                )
                            )
                        ),
                    ),
                    punten=float(punten),
                )
            yield WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    id=str(
                        CriteriumId(
                            stelselgroep=self.stelselgroep,
                            gedeeld_met_aantal=aantal_onz,
                            gedeeld_met_soort=GedeeldMetSoort.onzelfstandige_woonruimten,
                            is_totaal=True,
                        )
                    ),
                    naam=f"Totaal (gedeeld met {aantal_onz} onzelfstandige woonruimten)"
                    if aantal_onz > 1
                    else "Totaal (privé)",
                ),
                punten=float(
                    utils.rond_af_op_kwart(sum(bovenliggend_criterium_punten.values()))
                ),
            )


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=VerkoelingEnVerwarming(peildatum=date(2025, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer(
            "tests/data/onzelfstandige_woonruimten/stelselgroepen/verkoeling_en_verwarming/input/vertrek_verkoeld_en_verwarmd_onz.json"
        )
