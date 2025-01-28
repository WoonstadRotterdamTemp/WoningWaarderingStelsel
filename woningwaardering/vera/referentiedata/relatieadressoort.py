from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class RelatieadressoortReferentiedata(Referentiedata):
    pass


class Relatieadressoort(Referentiedatasoort):
    bezoekadres = RelatieadressoortReferentiedata(
        code="BEZ",
        naam="Bezoekadres",
    )
    """
    Het adres waar een relatie fysiek te bezoeken is.
    """

    factuuradres = RelatieadressoortReferentiedata(
        code="FAC",
        naam="Factuuradres",
    )
    """
    Het adres dat wordt gebruikt voor het verzenden van facturen en andere financiële
    correspondentie.
    """

    leveringsadres = RelatieadressoortReferentiedata(
        code="LEV",
        naam="Leveringsadres",
    )
    """
    Het adres waar eventuele goederen afgeleverd of bezorgd dienen te worden.
    """

    postadres = RelatieadressoortReferentiedata(
        code="POS",
        naam="Postadres",
    )
    """
    Het adres dat is aangewezen voor het ontvangen van correspondentie per post. Dit kan
    een postbus of een ander adres zijn dat afwijkt van het bezoekadres.
    """

    woonadres = RelatieadressoortReferentiedata(
        code="WOO",
        naam="Woonadres",
    )
    """
    Het adres waar een relatie daadwerkelijk woont.
    """
