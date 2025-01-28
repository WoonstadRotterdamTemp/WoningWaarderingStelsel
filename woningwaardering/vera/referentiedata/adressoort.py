from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class AdressoortReferentiedata(Referentiedata):
    pass


class Adressoort(Referentiedatasoort):
    buitenlands_adres = AdressoortReferentiedata(
        code="BUI",
        naam="Buitenlands adres",
    )
    """
    Een adres dat zicht bevindt buiten de landsgrenzen van Nederland. Dit type adres
    wordt gebruikt voor buitenlandse relaties of locaties.
    """

    eenheid_adres = AdressoortReferentiedata(
        code="EEN",
        naam="Eenheid adres",
    )
    """
    De adresgegevens die gekoppeld zijn aan een specifieke eenheid, zoals een woning
    appartement of bedrijfsruimte. Dit type adres omvat de volledige locatiegegevens
    die nodig zijn voor identificatie.
    """

    postadres = AdressoortReferentiedata(
        code="POS",
        naam="Postadres",
    )
    """
    Een adres dat speciaal bedoeld is voor het ontvangen van post, zoals een
    postbusnummer of een antwoordnummer. Dit type adres is uitsluitend van
    toepassing op Nederlandse locaties en mag geen fysieke locatie aanduiden.
    Buitenlandse postadressen moeten worden geregistreerd als een buitenlands adres.
    """
