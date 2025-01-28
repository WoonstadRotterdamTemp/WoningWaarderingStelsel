from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class BetalingsregelingstatusReferentiedata(Referentiedata):
    pass


class Betalingsregelingstatus(Referentiedatasoort):
    aangevraagd = BetalingsregelingstatusReferentiedata(
        code="AAN",
        naam="Aangevraagd",
    )
    """
    Aangemaakt, maar nog niet toegekend of in werking getreden.
    """

    actief = BetalingsregelingstatusReferentiedata(
        code="ACT",
        naam="Actief",
    )
    """
    Toegekend en momenteel lopend.
    """

    geannuleerd = BetalingsregelingstatusReferentiedata(
        code="ANN",
        naam="Geannuleerd",
    )
    """
    Tussentijds gestopt voordat deze volledig was afgerond.
    """

    beeindigd = BetalingsregelingstatusReferentiedata(
        code="BEE",
        naam="Beëindigd",
    )
    """
    Volledig afgerond, alle betalingsverplichtingen zijn voldaan.
    """

    bevroren = BetalingsregelingstatusReferentiedata(
        code="BEV",
        naam="Bevroren",
    )
    """
    Tijdelijk opgeschort vanwege onmogelijkheid om aan de verplichtingen te voldoen.
    """

    verwijderd = BetalingsregelingstatusReferentiedata(
        code="VER",
        naam="Verwijderd",
    )
    """
    Verwijderd omdat deze niet was toegekend of verkeerd of onterecht was vastgelegd.
    """
