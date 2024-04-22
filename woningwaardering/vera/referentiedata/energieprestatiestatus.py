from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Energieprestatiestatus(Enum):
    definitief = Referentiedata(
        code="DEF",
        naam="Definitief",
    )
    """
    Een definitieve energieprestatie is een bij de Rijksoverheid afgemelde
    energieprestatie, wat leidt tot een officieel geldig label.
    """

    voorlopig = Referentiedata(
        code="VOO",
        naam="Voorlopig",
    )
    """
    Een voorlopige energieprestatie wordt ook wel &#39;pré-label&#39; genoemd en is een op basis
    van woningkenmerken afgeleide (theoretische) prestatie
    """

    @property
    def code(self) -> str | None:
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam

    @property
    def parent(self) -> Referentiedata | None:
        return self.value.parent
