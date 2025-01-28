from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.prijscomponentsoort import (
    Prijscomponentsoort,
)
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class PrijscomponentdetailsoortReferentiedata(Referentiedata):
    pass


class Prijscomponentdetailsoort(Referentiedatasoort):
    administratiekosten = PrijscomponentdetailsoortReferentiedata(
        code="AKO",
        naam="Administratiekosten",
        parent=Prijscomponentsoort.eenmalig,
    )
    """
    Administratiekosten zijn de kosten die een organisatie of bedrijf maakt voor het
    uitvoeren van administratieve taken. Dit omvat alle werkzaamheden die nodig zijn
    om de dagelijkse bedrijfsvoering te ondersteunen en te organiseren. Denk hierbij
    aan het verwerken, beheren en bijhouden van financiële en operationele gegevens.
    """

    alarm_bewaking = PrijscomponentdetailsoortReferentiedata(
        code="ALA",
        naam="Alarm bewaking",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor het alarm en de bewaking van de woning
    """

    servicekosten_bedrijfsruimten = PrijscomponentdetailsoortReferentiedata(
        code="BED",
        naam="Servicekosten bedrijfsruimten",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor services m.b.t. bedrijfsruimten
    """

    beheerders = PrijscomponentdetailsoortReferentiedata(
        code="BEH",
        naam="Beheerder(s)",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor de beheerder(s) van de eenheid en/of het complex
    """

    borg = PrijscomponentdetailsoortReferentiedata(
        code="BOR",
        naam="Borg",
        parent=Prijscomponentsoort.eenmalig,
    )

    dienst_en_recreatieruimten = PrijscomponentdetailsoortReferentiedata(
        code="DIE",
        naam="Dienst- en recreatieruimten",
        parent=Prijscomponentsoort.service,
    )
    """
    De maandelijkse kosten voor reparaties en groot onderhoud aan dienstruimten en
    recreatieruimten. Deze kosten komen meestal voor bij senioren- of
    bejaardenwoningen. Het gaat niet om de inventaris, het schoonmaken van de
    ruimten of onderhoud aan de tuin.
    """

    electriciteit = PrijscomponentdetailsoortReferentiedata(
        code="ELE",
        naam="Electriciteit",
        parent=Prijscomponentsoort.verbruik,
    )
    """
    Elektriciteit is een vorm van energie die voortkomt uit de beweging of het stromen
    van elektrische ladingen, meestal door een geleider zoals koper of aluminium.
    Het is een fundamenteel natuurkundig verschijnsel dat wordt gebruikt als
    energiebron voor talloze toepassingen in ons dagelijks leven en de industrie.
    """

    elektrische_installaties = PrijscomponentdetailsoortReferentiedata(
        code="ELI",
        naam="Elektrische installaties",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor het gebruik van elektrische installaties
    """

    elektra_oplaadpunt = PrijscomponentdetailsoortReferentiedata(
        code="ELO",
        naam="Elektra oplaadpunt",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor het gebruik van een oplaadpunt voor andere elektrische
    apparaten dan een elektrische auto (b.v. scootmobiel)
    """

    energie_voor_gemeenschappelijke_ruimten = PrijscomponentdetailsoortReferentiedata(
        code="ENE",
        naam="Energie voor gemeenschappelijke ruimten",
        parent=Prijscomponentsoort.service,
    )
    """
    Dit zijn bijvoorbeeld de maandelijkse kosten voor elektriciteit voor bijvoorbeeld:
    lift, verlichting, ventilatie, alarminstallatie. Alleen voor gemeenschappelijke
    ruimten.
    """

    energieprestatievergoeding = PrijscomponentdetailsoortReferentiedata(
        code="EPV",
        naam="Energieprestatievergoeding",
        parent=Prijscomponentsoort.verbruik,
    )
    """
    Een vergoeding die verhuurder aan huurder mag vragen voor een huurwoning die zelf
    energie opwekt
    """

    gas = PrijscomponentdetailsoortReferentiedata(
        code="GAS",
        naam="Gas",
        parent=Prijscomponentsoort.verbruik,
    )
    """
    Aardgas is een fossiele brandstof die voornamelijk bestaat uit methaan.
    """

    reparatie_gem_ruimten = PrijscomponentdetailsoortReferentiedata(
        code="GEM",
        naam="Reparatie gem. ruimten",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor het repareren van defecten aan gemeenschappelijke ruimten
    """

    gladheidsbestrijding = PrijscomponentdetailsoortReferentiedata(
        code="GHB",
        naam="Gladheidsbestrijding",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor het bestrijden van gladheid rondom de eenheid
    """

    glasbewassing = PrijscomponentdetailsoortReferentiedata(
        code="GLB",
        naam="Glasbewassing",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor het wassen van glas van ramen en deuren van de eenheid
    """

    glasfonds = PrijscomponentdetailsoortReferentiedata(
        code="GLF",
        naam="Glasfonds",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor de voorziening voor repareren van glasschade
    """

    groenvoorziening = PrijscomponentdetailsoortReferentiedata(
        code="GRO",
        naam="Groenvoorziening",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor het onderhouden van de groenvoorziening rondom de eenheid
    """

    huismeester = PrijscomponentdetailsoortReferentiedata(
        code="HUI",
        naam="Huismeester",
        parent=Prijscomponentsoort.service,
    )
    """
    De maandelijkse kosten voor de diensten die de huismeester, flatwacht, wijkbeheerder
    of conciërge levert.
    """

    huisvuil = PrijscomponentdetailsoortReferentiedata(
        code="HUV",
        naam="Huisvuil",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor het verwerken van huisvuil
    """

    individuele_garage = PrijscomponentdetailsoortReferentiedata(
        code="IGA",
        naam="Individuele garage",
        parent=Prijscomponentsoort.parkeren,
    )
    """
    Inpandige parkeerplek individueel
    """

    installaties = PrijscomponentdetailsoortReferentiedata(
        code="INS",
        naam="Installaties",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor het gebruik van andere installaties dan elektrische
    installaties
    """

    inventaris = PrijscomponentdetailsoortReferentiedata(
        code="INV",
        naam="Inventaris",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor het gebruik van inventaris
    """

    kale_huur = PrijscomponentdetailsoortReferentiedata(
        code="KAL",
        naam="Kale huur",
        parent=Prijscomponentsoort.netto_huur,
    )
    """
    Basisbedrag voor het gebruik van de woning
    """

    laadpaal = PrijscomponentdetailsoortReferentiedata(
        code="LAA",
        naam="Laadpaal",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor het gebruik van een laadpaal voor elektrische auto
    """

    liftkosten = PrijscomponentdetailsoortReferentiedata(
        code="LIF",
        naam="Liftkosten",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor het gebruik van de lift(en)
    """

    linnenpakket = PrijscomponentdetailsoortReferentiedata(
        code="LIN",
        naam="Linnenpakket",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor het gebruik van linnen
    """

    matiging_huurtoeslag = PrijscomponentdetailsoortReferentiedata(
        code="MAT",
        naam="Matiging huurtoeslag",
        parent=Prijscomponentsoort.huuraanpassing,
    )
    """
    Component voor het matigen van de huurprijs op basis van toegekende huurtoeslag
    conform de wettelijke regeling van vóór 2014. Dit component is alleen bedoeld
    voor het uitwisselen van historische data
    """

    mechanische_ventilatie = PrijscomponentdetailsoortReferentiedata(
        code="MVE",
        naam="Mechanische ventilatie",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor het gebruik van de mechanische ventilatie
    """

    overnamekosten = PrijscomponentdetailsoortReferentiedata(
        code="OKO",
        naam="Overnamekosten",
        parent=Prijscomponentsoort.eenmalig,
    )
    """
    Overnamekosten zijn de kosten die gepaard gaan met de overname van een bedrijf,
    organisatie of activa. Dit omvat alle uitgaven die nodig zijn om het
    overnameproces te voltooien, inclusief juridische, financiële en operationele
    aspecten.
    """

    onderhoudsabonnement = PrijscomponentdetailsoortReferentiedata(
        code="OND",
        naam="Onderhoudsabonnement",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor onderhoudsabonnement. De huurder is zelf verantwoordelijk
    voor het klein onderhoud aan de woning. Als de huurder een onderhoudsabonnement
    afsluit, dan regelt de corporatie het klein onderhoud voor de huurder.
    """

    overige_netto_huur_component = PrijscomponentdetailsoortReferentiedata(
        code="ONH",
        naam="Overige netto huur component",
        parent=Prijscomponentsoort.netto_huur,
    )
    """
    Een overige netto huur component wordt bijvoorbeeld gebruikt om de extra huur na het
    aanbrengen van (verduurzamings-) verbeteringen te onderscheiden van de basis
    kale huur.
    """

    overige_kosten_gem_ruimten = PrijscomponentdetailsoortReferentiedata(
        code="OVE",
        naam="Overige kosten gem. ruimten",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor overige kosten voor gemeenschappelijke ruimten (naast
    schoonmaak, energie en reparatie)
    """

    parkeerplaats_buiten = PrijscomponentdetailsoortReferentiedata(
        code="PBU",
        naam="Parkeerplaats buiten",
        parent=Prijscomponentsoort.parkeren,
    )
    """
    Uitpandige parkeerplek
    """

    parkeergarage = PrijscomponentdetailsoortReferentiedata(
        code="PGA",
        naam="Parkeergarage",
        parent=Prijscomponentsoort.parkeren,
    )
    """
    Inpandige parkeerplek collectief
    """

    rioolfonds = PrijscomponentdetailsoortReferentiedata(
        code="RIO",
        naam="Rioolfonds",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor de voorziening voor het repareren van problemen aan het
    riool
    """

    schoonmaak_eenheid = PrijscomponentdetailsoortReferentiedata(
        code="SCE",
        naam="Schoonmaak eenheid",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor schoonmaak van de eenheid
    """

    schoonmaak_van_gemeenschappelijke_ruimten = PrijscomponentdetailsoortReferentiedata(
        code="SCH",
        naam="Schoonmaak van gemeenschappelijke ruimten",
        parent=Prijscomponentsoort.service,
    )
    """
    De maandelijkse schoonmaakkosten voor de lift en andere gemeenschappelijke ruimten,
    zoals een galerij, trappenhuis of recreatieruimte
    """

    signaallevering_o_a_cai = PrijscomponentdetailsoortReferentiedata(
        code="SIG",
        naam="Signaallevering (o.a. CAI)",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor signaallevering (o.a. CAI)
    """

    schoorsteenvegen = PrijscomponentdetailsoortReferentiedata(
        code="STV",
        naam="Schoorsteenvegen",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor het vegen van de schoorsteen
    """

    verenigingskosten = PrijscomponentdetailsoortReferentiedata(
        code="VER",
        naam="Verenigingskosten",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor lidmaatschap van  verenigingen
    """

    volkstuin = PrijscomponentdetailsoortReferentiedata(
        code="VOL",
        naam="Volkstuin",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor het gebruik van een volkstuin
    """

    vve_kosten = PrijscomponentdetailsoortReferentiedata(
        code="VVE",
        naam="VVE kosten",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor VVE-lidmaatschap
    """

    verzekeringskosten = PrijscomponentdetailsoortReferentiedata(
        code="VZE",
        naam="Verzekeringskosten",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor verzekeringen
    """

    warmte_installaties = PrijscomponentdetailsoortReferentiedata(
        code="WAI",
        naam="Warmte-installaties",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor het gebruik van installaties voor verwarming van de
    vertrekken van de eenheid
    """

    warmte = PrijscomponentdetailsoortReferentiedata(
        code="WAR",
        naam="Warmte",
        parent=Prijscomponentsoort.verbruik,
    )
    """
    Centrale verwarming, Stadsverwarming, etc.
    """

    water = PrijscomponentdetailsoortReferentiedata(
        code="WAT",
        naam="Water",
    )
    """
    Voor dagelijks gebruik zoals douchen, toiletspoeling, schoonmaken, en koken. Of
    water als service voor bijv. schoonmaak.
    """

    witgoed = PrijscomponentdetailsoortReferentiedata(
        code="WIT",
        naam="Witgoed",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor het gebruik van witgoed (bijvoorbeeld wasmachine of droger)
    """

    warmwaterinstallaties = PrijscomponentdetailsoortReferentiedata(
        code="WWI",
        naam="Warmwaterinstallaties",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor het gebruik van installaties voor warm water
    """

    zonnepanelen = PrijscomponentdetailsoortReferentiedata(
        code="ZON",
        naam="Zonnepanelen",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor het gebruik van zonnepanelen
    """

    zonwering = PrijscomponentdetailsoortReferentiedata(
        code="ZWE",
        naam="Zonwering",
        parent=Prijscomponentsoort.service,
    )
    """
    Maandelijkse kosten voor het gebruik van zonwering
    """
