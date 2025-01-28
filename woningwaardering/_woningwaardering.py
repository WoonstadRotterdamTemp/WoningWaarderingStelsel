from datetime import date

from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.onzelfstandige_woonruimten.onzelfstandige_woonruimten import (
    OnzelfstandigeWoonruimten,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.zelfstandige_woonruimten import (
    ZelfstandigeWoonruimten,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheidbericht,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
)


class Woningwaardering:
    """Initialiseert een Woningwaardering object dat automatisch het juiste stelsel detecteert.

    Parameters:
        peildatum (date, optional): De peildatum voor de waardering.
            Standaard is de huidige datum.

    Attributes:
        peildatum (date): De peildatum voor de waardering.
        stelsels (dict): Dictionary met alle beschikbare stelsels.
    """

    def __init__(self, peildatum: date = date.today()) -> None:
        self.peildatum = peildatum

    def waardeer(
        self,
        eenheid: EenhedenEenheidbericht,
    ) -> WoningwaarderingResultatenWoningwaarderingResultaat:
        """Berekent de woningwaardering voor een eenheid door automatisch het juiste stelsel te detecteren.

        Parameters:
            eenheid (EenhedenEenheidbericht): De eenheid waarvoor de woningwaardering wordt berekend.

        Returns:
            WoningwaarderingResultatenWoningwaarderingResultaat: Het resultaat van de woningwaardering.

        Raises:
            ValueError: Als het type woonruimte niet kan worden bepaald.
        """
        if (
            eenheid.woningwaarderingstelsel is None
            or eenheid.woningwaarderingstelsel is None
        ):
            raise ValueError(
                f"Eenheid ({eenheid.id}): woningwaarderingstelsel-attribuut ontbreekt in het inputmodel."
            )
        elif eenheid.woningwaarderingstelsel not in [
            Woningwaarderingstelsel.zelfstandige_woonruimten,
            Woningwaarderingstelsel.onzelfstandige_woonruimten,
        ]:
            raise ValueError(
                f"Eenheid ({eenheid.id}): ongeldig woningwaarderingsstelsel-attribuut: {eenheid.woningwaarderingstelsel}. Code moet één van {Woningwaarderingstelsel.zelfstandige_woonruimten} of {Woningwaarderingstelsel.onzelfstandige_woonruimten} zijn."
            )
        elif (
            eenheid.woningwaarderingstelsel
            == Woningwaarderingstelsel.zelfstandige_woonruimten
        ):
            stelsel: ZelfstandigeWoonruimten | OnzelfstandigeWoonruimten = (
                ZelfstandigeWoonruimten(peildatum=self.peildatum)
            )
        elif (
            eenheid.woningwaarderingstelsel
            == Woningwaarderingstelsel.onzelfstandige_woonruimten
        ):
            stelsel = OnzelfstandigeWoonruimten(peildatum=self.peildatum)

        return stelsel.waardeer(eenheid)


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=Woningwaardering(peildatum=date(2025, 1, 1)),  # type: ignore
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/onzelfstandige_woonruimten/input/15004000185.json")
