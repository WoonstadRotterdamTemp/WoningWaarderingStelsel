from abc import ABC, abstractmethod
from collections import defaultdict
from datetime import date
from typing import Iterator

from woningwaardering.stelsels.criteriumsleutels import CriteriumSleutels
from woningwaardering.stelsels.utils import is_geldig
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheidbericht,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    WoningwaarderingstelselgroepReferentiedata,
    WoningwaarderingstelselReferentiedata,
)


class Stelselgroep(ABC):
    @property
    def stelsel(self) -> WoningwaarderingstelselReferentiedata:
        return self._stelsel

    @stelsel.setter
    def stelsel(self, value: WoningwaarderingstelselReferentiedata) -> None:
        self._stelsel = value

    @property
    def stelselgroep(self) -> WoningwaarderingstelselgroepReferentiedata:
        return self._stelselgroep

    @stelselgroep.setter
    def stelselgroep(self, value: WoningwaarderingstelselgroepReferentiedata) -> None:
        self._stelselgroep = value

    """Initialiseert een Stelselgroep.

    Args:
        begindatum (date): De begindatum van de geldigheid van de stelselgroep.
        einddatum (date, optional): De einddatum (t/m) van de geldigheid van de stelselgroep.
        peildatum (date, optional): De peildatum voor de waardering".

    Raises:
        ValueError: Als de stelselgroep niet geldig is op de peildatum.
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
    def waardeer(
        self,
        eenheid: EenhedenEenheidbericht,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        """Bereken de woningwaardering voor een specifieke eenheid op stelselgroep-niveau.

        Args:
            eenheid (EenhedenEenheidbericht): De eenheid waarvoor de woningwaardering wordt berekend.
            woningwaardering_resultaat (WoningwaarderingResultatenWoningwaarderingResultaat | None, optional): Het resultaat van de woningwaardering.

        Returns:
            WoningwaarderingResultatenWoningwaarderingGroep: Het resultaat van de woningwaardering voor de gehele groep.
        """
        pass  # pragma: no cover

    def criteriumsleutel_resultaten(
        self,
        woningwaardering_groep: WoningwaarderingResultatenWoningwaarderingGroep,
    ) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
        criteriumsleutelpunten: dict[str, float] = defaultdict(float)
        for woningwaardering in woningwaardering_groep.woningwaarderingen or []:
            if (
                woningwaardering.criterium
                and woningwaardering.criterium.bovenliggende_criterium
                and woningwaardering.criterium.bovenliggende_criterium.id
                and isinstance(woningwaardering.punten, float)
            ):
                criteriumsleutelpunten[
                    woningwaardering.criterium.bovenliggende_criterium.id
                ] += woningwaardering.punten

        for id, punten in criteriumsleutelpunten.items():
            yield WoningwaarderingResultatenWoningwaardering(
                criterium=CriteriumSleutels[id].value,
                punten=punten,
            )
