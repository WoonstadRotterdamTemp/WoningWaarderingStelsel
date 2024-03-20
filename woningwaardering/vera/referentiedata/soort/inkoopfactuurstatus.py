from woningwaardering.vera.bvg.generated import Referentiedata


class Inkoopfactuurstatus:
    afgewezen = Referentiedata(
        code="AFG",
        naam="Afgewezen",
    )
    """
    Inkoopfactuur is afgewezen.
    """

    afgehandeld = Referentiedata(
        code="AFH",
        naam="Afgehandeld",
    )
    """
    Inkoopfactuur is afgehandeld.
    """

    afgekeurd = Referentiedata(
        code="AGK",
        naam="Afgekeurd",
    )
    """
    Inkoopfactuur is afgekeurd.
    """

    aangeboden_ter_betaling = Referentiedata(
        code="ATB",
        naam="Aangeboden ter betaling",
    )
    """
    Inkoopfactuur is aangeboden ter betaling.
    """

    aangeboden_ter_goedkeuring = Referentiedata(
        code="ATG",
        naam="Aangeboden ter goedkeuring",
    )
    """
    Inkoopfactuur is aangeboden ter goedkeuring.
    """

    betaald = Referentiedata(
        code="BET",
        naam="Betaald",
    )
    """
    Inkoopfactuur is betaald.
    """

    geblokkeerd = Referentiedata(
        code="BLK",
        naam="Geblokkeerd",
    )
    """
    Inkoopfactuur is geblokkeerd.
    """

    goedgekeurd = Referentiedata(
        code="GDK",
        naam="Goedgekeurd",
    )
    """
    Inkoopfactuur is goedgekeurd.
    """

    historisch = Referentiedata(
        code="HIS",
        naam="Historisch",
    )
    """
    Inkoopfactuur is gearchiveerd/historisch.
    """

    in_behandeling = Referentiedata(
        code="IBH",
        naam="In behandeling",
    )
    """
    Inkoopfactuur is in behandeling.
    """

    geregistreerd = Referentiedata(
        code="REG",
        naam="Geregistreerd",
    )
    """
    Inkoopfactuur is geregistreerd.
    """

    wacht_op_creditfactuur = Referentiedata(
        code="WOC",
        naam="Wacht op creditfactuur",
    )
    """
    Er wordt gewacht op een creditfactuur.
    """
