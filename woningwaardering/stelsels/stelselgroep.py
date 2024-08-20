from abc import ABC, abstractmethod
from datetime import date

from woningwaardering.stelsels.utils import is_geldig
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


class Stelselgroep(ABC):
    """Initialiseert een Stelselgroep.

    Args:
        peildatum (date, optional): De peildatum voor de waardering".
    """

    def __init__(
        self,
        begindatum: date,
        einddatum: date = date.max,
        peildatum: date = date.today(),
    ) -> None:
        self.peildatum = peildatum
        if not is_geldig(begindatum, einddatum, peildatum):
            raise ValueError(
                f"Stelselgroep ({begindatum} - {einddatum}) is niet geldig op peildatum ({peildatum})."
            )

    @abstractmethod
    def bereken(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        """Bereken de woningwaardering voor een specifieke eenheid op stelselgroep-niveau.

        Args:
            eenheid (EenhedenEenheid): De eenheid waarvoor de woningwaardering wordt berekend.
            woningwaardering_resultaat (WoningwaarderingResultatenWoningwaarderingResultaat | None, optional): Het resultaat van de woningwaardering.

        Returns:
            WoningwaarderingResultatenWoningwaarderingGroep: Het resultaat van de woningwaardering voor de gehele groep.
        """
        pass  # pragma: no cover
