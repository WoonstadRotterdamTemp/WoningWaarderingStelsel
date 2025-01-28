from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class EenheidcriteriumsoortReferentiedata(Referentiedata):
    pass


class Eenheidcriteriumsoort(Referentiedatasoort):
    binding = EenheidcriteriumsoortReferentiedata(
        code="BIN",
        naam="Binding",
    )
    """
    Er is voorrang voor woningzoekenden met binding tot een bepaald gebied. Bijvoorbeeld
    regionaal voor mensen die in het regionaal samenwerkingsverband wonen en/of
    werken, lokaal voor mensen die in de gemeente wonen.
    """

    groep = EenheidcriteriumsoortReferentiedata(
        code="GRO",
        naam="Groep",
    )
    """
    Er is voorrang voor woningzoekenden die tot een bepaalde groep behoren waar geen
    binding, urgentie of indicatie van toepassing is.
    """

    indicatie = EenheidcriteriumsoortReferentiedata(
        code="IND",
        naam="Indicatie",
    )
    """
    Er is voorrang voor woningzoekenden met een (medische) indicatie.
    """

    urgentie = EenheidcriteriumsoortReferentiedata(
        code="URG",
        naam="Urgentie",
    )
    """
    Er is voorrang voor woningzoekenden met een urgentie.
    """

    inkomen = EenheidcriteriumsoortReferentiedata(
        code="INK",
        naam="Inkomen",
    )
    """
    Huishouden met een bepaald verzamelinkomen.
    """

    leeftijd = EenheidcriteriumsoortReferentiedata(
        code="LEE",
        naam="Leeftijd",
    )
    """
    Huishouden met personen in een bepaalde leeftijdsgroep.
    """

    personen = EenheidcriteriumsoortReferentiedata(
        code="PER",
        naam="Personen",
    )
    """
    Huishouden van een bepaalde huishoudgrootte.
    """
