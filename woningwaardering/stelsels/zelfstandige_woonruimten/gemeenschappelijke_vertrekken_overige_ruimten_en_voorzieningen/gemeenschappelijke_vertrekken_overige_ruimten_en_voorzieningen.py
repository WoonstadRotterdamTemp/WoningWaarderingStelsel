from datetime import date
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.criterium_id import CriteriumId
from woningwaardering.stelsels.gedeelde_logica import (
    waardeer_keuken,
    waardeer_oppervlakte_van_overige_ruimte,
    waardeer_oppervlakte_van_vertrek,
    waardeer_sanitair,
    waardeer_verkoeling_en_verwarming,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.utils import (
    classificeer_ruimte,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheidbericht,
    EenhedenRuimte,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Doelgroep,
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


class GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen
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

        # Gemeenschappelijke ruimten en voorzieningen in een zorgwoning
        #
        # De ervaring leert dat bij het waarderen van de gemeenschappelijke ruimten en
        # voorzieningen in een zorgwoning of woon/zorgcomplex de waardering per woning
        # veelal uitkomt op een totaal van ongeveer 3 punten. Om arbeidsintensief
        # meetwerk te voorkomen waardeert de Huurcommissie in dat geval een waardering
        # van 3 punten per woning.
        if eenheid.doelgroep == Doelgroep.zorg:
            logger.info(
                f"Eenheid ({eenheid.id}) is een zorgwoning en wordt met 3 punten gewaardeerd voor stelselgroep {Woningwaarderingstelselgroep.gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen.naam}"
            )
            woningwaardering_groep.woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
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
            )
        else:
            gedeelde_ruimten = [
                ruimte
                for ruimte in eenheid.ruimten or []
                if utils.gedeeld_met_eenheden(ruimte)
            ]

            oppervlakte_berekeningen = {
                Ruimtesoort.vertrek: waardeer_oppervlakte_van_vertrek,
                Ruimtesoort.overige_ruimten: waardeer_oppervlakte_van_overige_ruimte,
            }

            for ruimte in gedeelde_ruimten:
                if ruimte.detail_soort is None:
                    continue

                ruimtesoort = classificeer_ruimte(ruimte)
                if ruimtesoort is None:
                    continue

                oppervlakte_berekening = oppervlakte_berekeningen.get(ruimtesoort, None)

                if oppervlakte_berekening is not None:
                    oppervlakte_waarderingen = list(oppervlakte_berekening(ruimte))
                # Gemeenschappelijke bergingen worden gewaardeerd als overige ruimte als:
                #
                # […]
                # * de oppervlakte, na deling door het aantal adressen, per woning minstens
                #   2m2 bedraagt.
                if ruimte.detail_soort == Ruimtedetailsoort.berging:
                    if ruimte.oppervlakte and ruimte.gedeeld_met_aantal_eenheden:
                        gedeelde_oppervlakte = (
                            ruimte.oppervlakte / ruimte.gedeeld_met_aantal_eenheden
                        )
                        if gedeelde_oppervlakte < Decimal("2.0"):
                            logger.info(
                                f"Eenheid ({eenheid.id}): {Ruimtedetailsoort.berging.naam} ({ruimte.id}) heeft, na deling door het aantal adressen, een oppervlakte van minder dan 2 m2 en wordt daarom niet gewaardeerd onder {Woningwaarderingstelselgroep.gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen.naam}"
                            )
                            oppervlakte_waarderingen = []

                # waarderingen voor de oppervlakten van gedeelde ruimten
                for oppervlakte_waardering in oppervlakte_waarderingen:
                    if oppervlakte_waardering.punten is None:
                        oppervlakte_waardering.punten = float(
                            Decimal(str(oppervlakte_waardering.aantal))
                            * (
                                Decimal("1.0")
                                if ruimtesoort == Ruimtesoort.vertrek
                                else Decimal("0.75")
                            )
                        )

                woningwaardering_groep.woningwaarderingen.extend(
                    self._deel_woningwaarderingen_door_aantal_eenheden(
                        ruimte, oppervlakte_waarderingen
                    )
                )

                # waarderingen voor de keuken van gedeelde ruimten
                keuken_waarderingen = list(waardeer_keuken(ruimte, self.stelsel))
                woningwaardering_groep.woningwaarderingen.extend(
                    self._deel_woningwaarderingen_door_aantal_eenheden(
                        ruimte, keuken_waarderingen
                    )
                )

                # waarderingen voor sanitair van gedeelde ruimten
                sanitair_waarderingen = list(
                    waardeer_sanitair(ruimte, self.stelselgroep, self.stelsel)
                )
                woningwaardering_groep.woningwaarderingen.extend(
                    self._deel_woningwaarderingen_door_aantal_eenheden(
                        ruimte, sanitair_waarderingen
                    )
                )

            # waarderingen voor de verkoeling en verwarming van gedeelde ruimten
            verkoeling_en_verwarming_waarderingen = list(
                waardeer_verkoeling_en_verwarming(gedeelde_ruimten)
            )

            for ruimte, waardering in verkoeling_en_verwarming_waarderingen:
                woningwaardering_groep.woningwaarderingen.extend(
                    self._deel_woningwaarderingen_door_aantal_eenheden(
                        ruimte, [waardering]
                    )
                )

        punten = utils.rond_af_op_kwart(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            ),
        )

        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep

    def _deel_woningwaarderingen_door_aantal_eenheden(
        self,
        ruimte: EenhedenRuimte,
        woningwaarderingen: list[WoningwaarderingResultatenWoningwaardering],
    ) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
        for woningwaardering in woningwaarderingen or []:
            woningwaardering.punten = float(
                utils.rond_af(
                    float(
                        Decimal(str(woningwaardering.punten))
                        / Decimal(str(ruimte.gedeeld_met_aantal_eenheden))
                    ),
                    decimalen=2,
                )
            )

            if (
                woningwaardering.criterium is not None
                and woningwaardering.criterium.naam is not None
            ):
                woningwaardering.criterium.naam = f"{woningwaardering.criterium.naam} (gedeeld met {ruimte.gedeeld_met_aantal_eenheden})"
            yield woningwaardering


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen(
            peildatum=date(2025, 1, 1)
        ),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/generiek/input/37101000032.json")
