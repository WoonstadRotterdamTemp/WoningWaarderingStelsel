from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.ruimtesoort import (
    Ruimtesoort,
)
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class CollectiefobjectsoortReferentiedata(Referentiedata):
    pass


class Collectiefobjectsoort(Referentiedatasoort):
    achterpad = CollectiefobjectsoortReferentiedata(
        code="APD",
        naam="Achterpad",
        parent=Ruimtesoort.buitenruimte,
    )
    """
    Een smalle doorgang achter woningen, vaak gebruikt als toegang tot tuinen of
    bergingen.
    """

    atrium_en_of_patio = CollectiefobjectsoortReferentiedata(
        code="ATR",
        naam="Atrium / Patio",
        parent=Ruimtesoort.buitenruimte,
    )
    """
    Niet overdekt atrium of patio
    """

    achtertuin = CollectiefobjectsoortReferentiedata(
        code="ATU",
        naam="Achtertuin",
        parent=Ruimtesoort.buitenruimte,
    )
    """
    Tuin gelegen aan de achterzijde van de woning. Deze waarde kan gebruikt worden voor
    de woningwaardering indien deze duiding van tuin bekend is.
    """

    gemeenschappelijk_balkon = CollectiefobjectsoortReferentiedata(
        code="BAL",
        naam="Gemeenschappelijk balkon",
        parent=Ruimtesoort.buitenruimte,
    )
    """
    Balkon dat gedeeld wordt door meerdere bewoners of gebruikers.
    """

    badkamer_met_toilet = CollectiefobjectsoortReferentiedata(
        code="BAT",
        naam="Badkamer met toilet",
        parent=Ruimtesoort.vertrek,
    )
    """
    Een gecombineerde sanitaire ruimte met een douche, bad en toilet in één vertrek.
    """

    gemeenschappelijke_badkamer = CollectiefobjectsoortReferentiedata(
        code="BDK",
        naam="Gemeenschappelijke badkamer",
        parent=Ruimtesoort.vertrek,
    )
    """
    Sanitaire ruimte gedeeld door meerdere gebruikers, bedoeld voor wassen en douchen.
    """

    gemeenschappelijke_berging = CollectiefobjectsoortReferentiedata(
        code="BER",
        naam="Gemeenschappelijke berging",
        parent=Ruimtesoort.overige_ruimten,
    )
    """
    Ruimte bedoeld voor het opslaan van goederen en gedeeld door meerdere bewoners.
    """

    bijkeuken = CollectiefobjectsoortReferentiedata(
        code="BIJ",
        naam="Bijkeuken",
        parent=Ruimtesoort.overige_ruimten,
    )
    """
    Ruimte grenzend aan de eigenlijke keuken die voor ondersteunende huishoudelijke
    handelingen gebruikt wordt, zoals wassen, drogen en strijken, maar ook voor het
    opbergen en bewaren van (etens)voorraden en schoonmaakspullen.
    """

    casco = CollectiefobjectsoortReferentiedata(
        code="CAS",
        naam="Casco",
        parent=Ruimtesoort.overige_ruimten,
    )
    """
    Constructieve basis van een gebouw, zoals muren en dak zonder verdere afwerking.
    """

    centrale_hal = CollectiefobjectsoortReferentiedata(
        code="CEH",
        naam="Centrale hal",
        parent=Ruimtesoort.overige_ruimten,
    )
    """
    Een grote gemeenschappelijke hal, vaak als entree voor een gebouw.
    """

    dak = CollectiefobjectsoortReferentiedata(
        code="DAK",
        naam="Dak",
        parent=Ruimtesoort.overige_ruimten,
    )
    """
    Bovenzijde van een gebouw die bescherming biedt tegen weersinvloeden.
    """

    doucheruimte = CollectiefobjectsoortReferentiedata(
        code="DOU",
        naam="Doucheruimte",
        parent=Ruimtesoort.vertrek,
    )
    """
    Sanitaire ruimte met een douche.
    """

    gemeenschappelijke_fietsenstalling = CollectiefobjectsoortReferentiedata(
        code="FTS",
        naam="Gemeenschappelijke fietsenstalling",
        parent=Ruimtesoort.overige_ruimten,
    )
    """
    Ruimte bestemd voor het stallen van fietsen en gedeeld door meerdere gebruikers.
    """

    gemeenschappelijk_dakterras = CollectiefobjectsoortReferentiedata(
        code="GAK",
        naam="Gemeenschappelijk dakterras",
        parent=Ruimtesoort.buitenruimte,
    )
    """
    Een buitenruimte op het dak, gedeeld door meerdere gebruikers en bedoeld voor
    recreatie.
    """

    galerij = CollectiefobjectsoortReferentiedata(
        code="GAL",
        naam="Galerij",
        parent=Ruimtesoort.buitenruimte,
    )
    """
    Een overdekte gang aan de buitenzijde van een gebouw, vaak verbonden met
    appartementen.
    """

    gang = CollectiefobjectsoortReferentiedata(
        code="GAN",
        naam="Gang",
        parent=Ruimtesoort.verkeersruimte,
    )
    """
    Een betrekkelijk smalle en lange ruimte omgeven door muren en afgedekt door een
    plafond of zoldering, in een gebouw, als verbinding van vertrekken waarvan de
    deuren erop uitkomen.
    """

    garage = CollectiefobjectsoortReferentiedata(
        code="GAR",
        naam="Garage",
        parent=Ruimtesoort.overige_ruimten,
    )
    """
    Overige ruimte: een overdekte en afsluitbare ruimte om voertuigen in te stallen.
    """

    hal = CollectiefobjectsoortReferentiedata(
        code="HAL",
        naam="Hal",
        parent=Ruimtesoort.verkeersruimte,
    )
    """
    Verkeersruimte bijv. entree, Hal, overloop, speelhal etc.
    """

    kelder = CollectiefobjectsoortReferentiedata(
        code="KEL",
        naam="Kelder",
        parent=Ruimtesoort.overige_ruimten,
    )
    """
    Dat gedeelte van een gebouw dat onder de grond (onder het maaiveld) is gelegen.
    """

    gemeenschappeijke_keuken = CollectiefobjectsoortReferentiedata(
        code="KEU",
        naam="Gemeenschappeijke keuken",
        parent=Ruimtesoort.vertrek,
    )
    """
    Vertrek of plaats in een gebouw waarin mensen hun voedsel bereiden of laten bereiden
    """

    lift = CollectiefobjectsoortReferentiedata(
        code="LIF",
        naam="Lift",
        parent=Ruimtesoort.overige_ruimten,
    )
    """
    Een mechanisch systeem dat personen of goederen verticaal verplaatst binnen een
    gebouw.
    """

    onderdoorgang = CollectiefobjectsoortReferentiedata(
        code="ONG",
        naam="Onderdoorgang",
        parent=Ruimtesoort.overige_ruimten,
    )
    """
    Een overdekte doorgang onder een gebouw of constructie.
    """

    overige_gemeenschappelijke_ruimte_of_voorziening = (
        CollectiefobjectsoortReferentiedata(
            code="OGR",
            naam="Overige gemeenschappelijke ruimte of voorziening",
            parent=Ruimtesoort.overige_ruimten,
        )
    )
    """
    Gemeenschappelijke ruimte of voorziening die niet nader is gespecifeerd als
    collectiefobjectsoort. Bijvoorbeeld gemeenschappelijke hobbyruimte.
    """

    overig_vertrek = CollectiefobjectsoortReferentiedata(
        code="OVT",
        naam="Overig vertrek",
        parent=Ruimtesoort.vertrek,
    )
    """
    Vertrek dat niet nader gespecifeerd is als ruimtedetailsoort. Bijvoorbeeld eetkamer,
    hobbykamer, studeerkamer etc.
    """

    parkeerplek_type_1 = CollectiefobjectsoortReferentiedata(
        code="PP1",
        naam="Parkeerplek type 1",
        parent=Ruimtesoort.overige_ruimten,
    )
    """
    Parkeerplek Type I: parkeerplek in afgesloten parkeergarage behorende tot het
    complex.
    """

    parkeerplek_type_2 = CollectiefobjectsoortReferentiedata(
        code="PP2",
        naam="Parkeerplek type 2",
        parent=Ruimtesoort.buitenruimte,
    )
    """
    Parkeerplek Type II: parkeerplek buiten behorende tot het complex met dak.
    """

    parkeerplek_type_3 = CollectiefobjectsoortReferentiedata(
        code="PP3",
        naam="Parkeerplek type 3",
        parent=Ruimtesoort.buitenruimte,
    )
    """
    Parkeerplek Type III: parkeerplek buiten behorende tot het complex of de woning
    zonder dak.
    """

    recreatie_en_of_ontmoetingsruimte = CollectiefobjectsoortReferentiedata(
        code="ROR",
        naam="Recreatie-/ontmoetingsruimte",
        parent=Ruimtesoort.overige_ruimten,
    )
    """
    Ruimte waar bewoners samenkomen voor recreatie of sociale activiteiten.
    """

    recreatieruimte = CollectiefobjectsoortReferentiedata(
        code="REC",
        naam="Recreatieruimte",
        parent=Ruimtesoort.overige_ruimten,
    )
    """
    Een ruimte binnen de eenheid die recreatie als gebruiksdoel heeft. Bijvoorbeeld
    binnen een zorginstelling.
    """

    schuur = CollectiefobjectsoortReferentiedata(
        code="SCH",
        naam="Schuur",
        parent=Ruimtesoort.overige_ruimten,
    )
    """
    Overige ruimte: veelal vrijstaand gebouw, dat gebruikt wordt om goederen of voedsel
    in op te slaan, en ook als werkruimte kan dienen, maar niet als woning bedoeld
    is.
    """

    serre = CollectiefobjectsoortReferentiedata(
        code="SER",
        naam="Serre",
        parent=Ruimtesoort.vertrek,
    )
    """
    Glazen veranda verbonden aan een woning.
    """

    speelplaats = CollectiefobjectsoortReferentiedata(
        code="SPP",
        naam="Speelplaats",
        parent=Ruimtesoort.buitenruimte,
    )
    """
    Buitenruimte ingericht voor spel en recreatie van kinderen.
    """

    stortkoker = CollectiefobjectsoortReferentiedata(
        code="STK",
        naam="Stortkoker",
        parent=Ruimtesoort.overige_ruimten,
    )
    """
    Installatie om afval of goederen naar beneden te transporteren, meestal naar een
    verzamelpunt.
    """

    terrein = CollectiefobjectsoortReferentiedata(
        code="TER",
        naam="Terrein",
        parent=Ruimtesoort.buitenruimte,
    )
    """
    Een stuk grond behorend bij een gebouw of complex.
    """

    terras = CollectiefobjectsoortReferentiedata(
        code="TES",
        naam="Terras",
        parent=Ruimtesoort.buitenruimte,
    )
    """
    Buitenruimte: deel van een buitenruimte met een vlakke oppervlakte die wordt
    gebruikt om op te zitten, te eten, te drinken of andere activiteiten te doen.
    """

    gemeenschappelijke_toilet = CollectiefobjectsoortReferentiedata(
        code="TOI",
        naam="Gemeenschappelijke toilet",
        parent=Ruimtesoort.overige_ruimten,
    )
    """
    Sanitaire ruimte met een toilet, gedeeld door meerdere bewoners of gebruikers.
    """

    trappenhuis = CollectiefobjectsoortReferentiedata(
        code="TRH",
        naam="Trappenhuis",
        parent=Ruimtesoort.overige_ruimten,
    )
    """
    Een ruimte in een gebouw die trappen bevat en toegang biedt tot verschillende
    verdiepingen.
    """

    technische_ruimte = CollectiefobjectsoortReferentiedata(
        code="TRU",
        naam="Technische ruimte",
        parent=Ruimtesoort.overige_ruimten,
    )
    """
    Een afgesloten ruimte voor installaties zoals verwarmings- of ventilatiesystemen.
    """

    tuin = CollectiefobjectsoortReferentiedata(
        code="TUI",
        naam="Tuin",
        parent=Ruimtesoort.buitenruimte,
    )
    """
    Gemeenschappelijke buitenruimte, vaak groen aangelegd, voor recreatief gebruik.
    """

    tussenkamer = CollectiefobjectsoortReferentiedata(
        code="TUS",
        naam="Tussenkamer",
        parent=Ruimtesoort.vertrek,
    )
    """
    Ruimte gelegen tussen en verbonden met twee andere kamers.
    """

    vliering = CollectiefobjectsoortReferentiedata(
        code="VLI",
        naam="Vliering",
        parent=Ruimtesoort.overige_ruimten,
    )
    """
    Ruimte onder het dak zonder vaste trap, met onvoldoende oppervlakte en/of stahoogte
    voor een verblijfsruimte en uitsluitend geschikt voor opslag.
    """

    voortuin = CollectiefobjectsoortReferentiedata(
        code="VTU",
        naam="Voortuin",
        parent=Ruimtesoort.buitenruimte,
    )
    """
    Tuin gelegen voor de voorgevellijn, waar meestal de voordeur van een woning is
    gelegen. Deze waarde kan gebruikt worden voor de woningwaardering indien deze
    duiding van tuin bekend is.
    """

    wasruimte = CollectiefobjectsoortReferentiedata(
        code="WAS",
        naam="Wasruimte",
        parent=Ruimtesoort.overige_ruimten,
    )
    """
    Een gemeenschappelijke wasruimte.
    """

    woonkamer_en_of_keuken = CollectiefobjectsoortReferentiedata(
        code="WOK",
        naam="Woonkamer/keuken",
        parent=Ruimtesoort.vertrek,
    )
    """
    Ruimte met een gecombineerde functie van keuken en woonkamer
    """

    woonkamer = CollectiefobjectsoortReferentiedata(
        code="WOO",
        naam="Woonkamer",
        parent=Ruimtesoort.vertrek,
    )
    """
    De kamer in een huis waar het dagelijkse gezinsleven zich afspeelt. Het is een van
    de grootste vertrekken.
    """

    woon_en_of_slaapkamer = CollectiefobjectsoortReferentiedata(
        code="WSL",
        naam="Woon-/slaapkamer",
        parent=Ruimtesoort.vertrek,
    )
    """
    Ruimte met een gecombineerde functie van woonkamer en slaapkamer.
    """

    zijtuin = CollectiefobjectsoortReferentiedata(
        code="ZIJ",
        naam="Zijtuin",
        parent=Ruimtesoort.buitenruimte,
    )
    """
    Buitenruimte: tuin gelegen aan de zijkant van een woning. Deze waarde kan gebruikt
    worden voor de woningwaardering indien deze duiding van tuin bekend is.
    """

    loggia = CollectiefobjectsoortReferentiedata(
        code="LOG",
        naam="Loggia",
        parent=Ruimtesoort.buitenruimte,
    )
    """
    Een inpandig balkon.
    """

    zolder = CollectiefobjectsoortReferentiedata(
        code="ZOL",
        naam="Zolder",
        parent=Ruimtesoort.overige_ruimten,
    )
    """
    Ruimte onder het dak met vaste trap, die qua oppervlakte en stahoogte geschikt is om
    als vertrek te worden gekwalificeerd, maar die niet voldoet aan de
    afwerkingseisen.
    """

    zoldervertrek = CollectiefobjectsoortReferentiedata(
        code="ZVT",
        naam="Zoldervertrek",
        parent=Ruimtesoort.vertrek,
    )
    """
    Ruimte onder het dak, die zowel qua oppervlakte en stahoogte als afwerking geschikt
    is om als vertrek te worden gekwalificeerd
    """
