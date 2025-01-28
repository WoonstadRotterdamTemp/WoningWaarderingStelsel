from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.eenheidklimaatbeheersingsoort import (
    Eenheidklimaatbeheersingsoort,
)
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class EenheidklimaatbeheersingReferentiedata(Referentiedata):
    pass


class Eenheidklimaatbeheersing(Referentiedatasoort):
    airco = EenheidklimaatbeheersingReferentiedata(
        code="AIR",
        naam="Airco",
    )
    """
    Een airconditioner (airco) is een apparaat dat de luchttemperatuur en vochtigheid in
    een ruimte regelt voor comfortabele omstandigheden. Het werkt door warme lucht
    uit de ruimte te verwijderen, te koelen via een koelmiddel zoals freon, en
    vervolgens gekoelde lucht terug te blazen om de gewenste temperatuur te
    handhaven. Dit kan zowel individueel als collectief georganiseerd zijn.
    """

    blokverwarming = EenheidklimaatbeheersingReferentiedata(
        code="BLO",
        naam="Blokverwarming",
        parent=Eenheidklimaatbeheersingsoort.collectief,
    )
    """
    Blokverwarming is een centraal verwarmingssysteem dat wordt gebruikt in gebouwen met
    meerdere woningen. In plaats van individuele cv-ketels hebben alle woningen een
    gemeenschappelijke warmtebron, meestal een centrale ketelinstallatie. Warm water
    wordt via leidingen naar radiatoren in elke woning gestuurd om de ruimten te
    verwarmen.
    """

    centrale_verwarming = EenheidklimaatbeheersingReferentiedata(
        code="CEV",
        naam="Centrale verwarming",
        parent=Eenheidklimaatbeheersingsoort.individueel,
    )
    """
    Een verwarmingssysteem dat specifiek is ontworpen om één enkele eenheid te
    verwarmen. De warmte wordt centraal opgewekt en vervolgens naar verschillende
    ruimtes in de woning of eenheid getransporteerd. Dit in tegenstelling tot
    centrale verwarmingssystemen die meerdere eenheden of gebouwen kunnen bedienen
    (zoals stadsverwarming of blokverwarming).
    """

    gaskachels = EenheidklimaatbeheersingReferentiedata(
        code="GAS",
        naam="Gaskachels",
        parent=Eenheidklimaatbeheersingsoort.individueel,
    )
    """
    Een gaskachel is een verwarmingstoestel dat werkt op aardgas of propaan. Het bevat
    een brander die gas verbrandt om warmte te produceren, waardoor de
    omgevingstemperatuur wordt verhoogd voor comfort in een ruimte.
    """

    houtkachel = EenheidklimaatbeheersingReferentiedata(
        code="HKA",
        naam="Houtkachel",
        parent=Eenheidklimaatbeheersingsoort.individueel,
    )
    """
    Een houtkachel is een verwarmingstoestel dat brandt op hout als brandstof. Het heeft
    een vuurhaard waarin hout wordt verbrand om warmte te genereren, waardoor een
    ruimte wordt verwarmd voor comfort.
    """

    muurverwarming = EenheidklimaatbeheersingReferentiedata(
        code="MUU",
        naam="Muurverwarming",
        parent=Eenheidklimaatbeheersingsoort.individueel,
    )
    """
    Muurverwarming is een verwarmingssysteem waarbij warmte wordt gegenereerd door
    leidingen die in de muren zijn ingebed. Warm water stroomt door deze leidingen,
    waardoor de muren warmte afgeven en de ruimte gelijkmatig verwarmen.
    """

    mechanische_ventilatie = EenheidklimaatbeheersingReferentiedata(
        code="MVE",
        naam="Mechanische ventilatie",
    )
    """
    Mechanische ventilatie is een systeem dat wordt gebruikt om verse lucht in gebouwen
    te brengen en vervuilde lucht af te voeren. Het maakt gebruik van ventilatoren
    om luchtstromen te creëren en te reguleren voor een gezond binnenklimaat. Dit
    kan zowel individueel als collectief georganiseerd zijn.
    """

    open_haard = EenheidklimaatbeheersingReferentiedata(
        code="OHA",
        naam="Open haard",
        parent=Eenheidklimaatbeheersingsoort.individueel,
    )
    """
    Een open haard is een vuurplaats in een huis met een opening waarin hout of andere
    brandbare materialen worden verbrand. Het biedt warmte, sfeer en soms ook
    kookmogelijkheden.
    """

    stadsverwarming = EenheidklimaatbeheersingReferentiedata(
        code="STV",
        naam="Stadsverwarming",
        parent=Eenheidklimaatbeheersingsoort.collectief,
    )
    """
    Stadsverwarming is een systeem waarbij warmte wordt geproduceerd op één centrale
    locatie, meestal een energiecentrale, en vervolgens via een netwerk van
    leidingen naar huizen en bedrijven in een stad wordt getransporteerd. De warmte
    wordt gebruikt voor ruimteverwarming, tapwaterverwarming en soms ook voor
    industriële processen, wat bijdraagt aan energie-efficiëntie.
    """

    onverwarmd = EenheidklimaatbeheersingReferentiedata(
        code="ONV",
        naam="Onverwarmd",
    )

    vloerverwarming = EenheidklimaatbeheersingReferentiedata(
        code="VLV",
        naam="Vloerverwarming",
        parent=Eenheidklimaatbeheersingsoort.individueel,
    )
    """
    Vloerverwarming is een verwarmingssysteem waarbij warmte wordt afgegeven via
    leidingen onder de vloer. Warm water stroomt door deze leidingen, waardoor de
    vloer wordt verwarmd en de warmte gelijkmatig wordt verspreid in de ruimte.
    """

    volledig_elektrisch = EenheidklimaatbeheersingReferentiedata(
        code="VOL",
        naam="Volledig Elektrisch",
        parent=Eenheidklimaatbeheersingsoort.individueel,
    )
    """
    Volledig elektrische klimaatbeheersing
    """

    warmtepomp_cv = EenheidklimaatbeheersingReferentiedata(
        code="WAC",
        naam="Warmtepomp CV",
    )
    """
    Warmtepomp i.c.m. CV-ketel voor verwarming en warm water. Ook wel een hybride
    waterpomp genoemd. Dit kan zowel individueel als collectief georganiseerd zijn.
    """

    warmtepomp = EenheidklimaatbeheersingReferentiedata(
        code="WAR",
        naam="Warmtepomp",
    )
    """
    Volledig elektrische warmtepomp voor verwarming en warm water. Dit kan zowel
    individueel als collectief georganiseerd zijn.
    """

    warmte_koudeopslaginstallatie = EenheidklimaatbeheersingReferentiedata(
        code="WKO",
        naam="Warmte- koudeopslaginstallatie",
    )
    """
    Een warmte-koudeopslaginstallatie (WKO) is een duurzaam verwarmingssysteem dat
    warmte in de zomer uit een gebouw haalt en opslaat in de grond, om het in de
    winter weer te gebruiken voor verwarming. Er is altijd sprake een
    (bodem-)waterpomp Dit kan zowel individueel als collectief georganiseerd zijn.
    """

    warmteterugwinsysteem = EenheidklimaatbeheersingReferentiedata(
        code="WTW",
        naam="Warmteterugwinsysteem",
    )
    """
    Een warmteterugwinsysteem (WTW) is een installatie die de warmte uit afgevoerde
    lucht recupereert en gebruikt om de binnenkomende verse lucht te verwarmen,
    waardoor energie wordt bespaard en het binnenklimaat wordt verbeterd. Dit kan
    zowel individueel als collectief georganiseerd zijn.
    """
