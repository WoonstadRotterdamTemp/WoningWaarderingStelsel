from datetime import date
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.gedeelde_logica.prijsopslag_monumenten import (
    check_monumenten_attribuut,
    opslag_beschermd_stads_of_dorpsgezicht,
    opslag_gemeentelijk_of_provinciaal_monument,
    opslag_rijksmonument,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheidbericht,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


class PrijsopslagMonumenten(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        super().__init__(
            begindatum=date(2025, 1, 1),
            einddatum=date.max,
            peildatum=peildatum,
        )
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.prijsopslag_monumenten

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

        woningwaardering_groep.woningwaarderingen = list(
            woningwaardering
            for woningwaardering in self._genereer_woningwaarderingen(
                self.peildatum, eenheid, woningwaardering_resultaat
            )
            if woningwaardering is not None
        )

        opslagpercentage = Decimal(
            sum(
                Decimal(str(woningwaardering.opslagpercentage))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.opslagpercentage is not None
            )
        )

        woningwaardering_groep.opslagpercentage = float(opslagpercentage)
        punten = Decimal(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            )
        )

        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep

    @staticmethod
    def _genereer_woningwaarderingen(
        peildatum: date,
        eenheid: EenhedenEenheidbericht,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> Iterator[WoningwaarderingResultatenWoningwaardering | None]:
        check_monumenten_attribuut(eenheid)

        yield opslag_rijksmonument(
            peildatum,
            eenheid,
            stelselgroep=Woningwaarderingstelselgroep.prijsopslag_monumenten,
        )
        yield opslag_gemeentelijk_of_provinciaal_monument(
            eenheid,
            stelselgroep=Woningwaarderingstelselgroep.prijsopslag_monumenten,
        )
        yield opslag_beschermd_stads_of_dorpsgezicht(
            eenheid,
            stelselgroep=Woningwaarderingstelselgroep.prijsopslag_monumenten,
        )


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=PrijsopslagMonumenten(peildatum=date(2025, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/onzelfstandige_woonruimten/input/15004000185.json")
