from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.woningwaarderingstelsel import (
    Woningwaarderingstelsel,
)
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class WoningwaarderingstelselgroepReferentiedata(Referentiedata):
    pass


class Woningwaarderingstelselgroep(Referentiedatasoort):
    bijzondere_voorzieningen = WoningwaarderingstelselgroepReferentiedata(
        code="BIJ",
        naam="Bijzondere voorzieningen",
        parent=Woningwaarderingstelsel.zelfstandige_woonruimten,
    )
    """
    De groep criteria die betrekking heeft op de aanwezigheid van bijzondere
    voorzieningen, uitsluitend van toepassing bij zorgwoningen (Beleidsboek
    Waarderingsstelsel zelfstandige woonruimte)
    """

    beschermd_monument_bmo = WoningwaarderingstelselgroepReferentiedata(
        code="BMO",
        naam="Beschermd monument",
        parent=Woningwaarderingstelsel.onzelfstandige_woonruimten,
    )
    """
    De extra punten die worden toegekend als de woonruimte bestaat uit of deel uitmaakt
    van een rijksmonument (Beleidsboek Waarderingsstelsel onzelfstandige woonruimte)
    """

    beschermd_monument_bmz = WoningwaarderingstelselgroepReferentiedata(
        code="BMZ",
        naam="Beschermd monument",
        parent=Woningwaarderingstelsel.zelfstandige_woonruimten,
    )
    """
    De extra punten die worden toegekend als de woonruimte bestaat uit of deel uitmaakt
    van een rijksmonument (Beleidsboek Waarderingsstelsel zelfstandige woonruimte)
    """

    berging = WoningwaarderingstelselgroepReferentiedata(
        code="BWN",
        naam="Berging",
        parent=Woningwaarderingstelsel.woonwagens,
    )
    """
    Niet-standaardwoonwagen: De groep criteria die betrekking heeft op de aanwezigheid
    van een berging (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    energieprestatie = WoningwaarderingstelselgroepReferentiedata(
        code="ENE",
        naam="Energieprestatie",
    )
    """
    De groep criteria die betrekking heeft op de energieprestaties (Beleidsboek
    Waarderingsstelsel zelfstandige woonruimte)
    """

    extra_punten_woonoppervlakte_standplaats = (
        WoningwaarderingstelselgroepReferentiedata(
            code="EOS",
            naam="Extra punten woonoppervlakte standplaats",
            parent=Woningwaarderingstelsel.standplaatsen,
        )
    )
    """
    Standplaats: De groep criteria die betrekking heeft op de woonoppervlakte als die
    meer dan 200m2 bedraagt (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    woonvoorzieningen_voor_gehandicapten = WoningwaarderingstelselgroepReferentiedata(
        code="GEH",
        naam="Woonvoorzieningen voor gehandicapten",
    )
    """
    De groep criteria die betrekking heeft op ingrepen die zijn gedaan ten behoeve van
    een gehandicapte (Beleidsboek Waarderingsstelsel zelfstandige woonruimte)
    """

    voorzieningen_gehandicapten_standplaats = (
        WoningwaarderingstelselgroepReferentiedata(
            code="GST",
            naam="Voorzieningen gehandicapten standplaats",
            parent=Woningwaarderingstelsel.standplaatsen,
        )
    )
    """
    Standplaats: De groep criteria die betrekking heeft op (gedeeltelijk) vanuit de WMO
    gesubsidieerde voorzieningen voor gehandicapten (Puntentelling:
    woonwagen/standplaats: Huurcommissie)
    """

    voorzieningen_gehandicapten_niet_standaardwoonwagen = (
        WoningwaarderingstelselgroepReferentiedata(
            code="GWN",
            naam="Voorzieningen gehandicapten niet-standaardwoonwagen",
            parent=Woningwaarderingstelsel.woonwagens,
        )
    )
    """
    Niet-standaardwoonwagen: De groep criteria die betrekking heeft op (gedeeltelijk)
    vanuit de WMO gesubsidieerde voorzieningen voor gehandicapten (Puntentelling:
    woonwagen/standplaats: Huurcommissie)
    """

    voorzieningen_gehandicapten_standaardwoonwagen = (
        WoningwaarderingstelselgroepReferentiedata(
            code="GWS",
            naam="Voorzieningen gehandicapten standaardwoonwagen",
            parent=Woningwaarderingstelsel.woonwagens,
        )
    )
    """
    Standaardwoonwagen: De groep criteria die betrekking heeft op (gedeeltelijk) vanuit
    de WMO gesubsidieerde voorzieningen voor gehandicapten (Puntentelling:
    woonwagen/standplaats: Huurcommissie)
    """

    keuken = WoningwaarderingstelselgroepReferentiedata(
        code="KEU",
        naam="Keuken",
    )
    """
    De groep criteria die betrekking heeft op de keuken (Beleidsboek Waarderingsstelsel
    zelfstandige woonruimte)
    """

    kookgelegenheid = WoningwaarderingstelselgroepReferentiedata(
        code="KOO",
        naam="Kookgelegenheid",
        parent=Woningwaarderingstelsel.onzelfstandige_woonruimten,
    )
    """
    De groep criteria die betrekking heeft op de kookgelegenheid (Beleidsboek
    Waarderingsstelsel onzelfstandige woonruimte)
    """

    extra_kwaliteit_keuken_en_sanitair_standplaats = (
        WoningwaarderingstelselgroepReferentiedata(
            code="KST",
            naam="Extra kwaliteit keuken en sanitair standplaats",
            parent=Woningwaarderingstelsel.standplaatsen,
        )
    )
    """
    Standplaats: De groep criteria die betrekking heeft op extra kwaliteit van keuken en
    sanitair  (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    kwaliteitsfactoren = WoningwaarderingstelselgroepReferentiedata(
        code="KWA",
        naam="Kwaliteitsfactoren",
        parent=Woningwaarderingstelsel.onzelfstandige_woonruimten,
    )
    """
    De groep criteria die betrekking heeft op aanvullende kwaliteitsfactoren
    (Beleidsboek Waarderingsstelsel onzelfstandige woonruimte)
    """

    keuken_en_sanitair_niet_standaardwoonwagen = (
        WoningwaarderingstelselgroepReferentiedata(
            code="KWN",
            naam="Keuken en sanitair niet-standaardwoonwagen",
            parent=Woningwaarderingstelsel.woonwagens,
        )
    )
    """
    Niet-standaardwoonwagen: De groep criteria die betrekking heeft op keuken en
    sanitair  (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    extra_kwaliteit_keuken_en_sanitair_standaardwoonwagen = (
        WoningwaarderingstelselgroepReferentiedata(
            code="KWS",
            naam="Extra kwaliteit keuken en sanitair standaardwoonwagen",
            parent=Woningwaarderingstelsel.woonwagens,
        )
    )
    """
    Standaardwoonwagen: De groep criteria die betrekking heeft op extra kwaliteit van
    keuken en sanitair  (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    minpunten_woonomgeving_standplaats = WoningwaarderingstelselgroepReferentiedata(
        code="MWS",
        naam="Minpunten woonomgeving standplaats",
        parent=Woningwaarderingstelsel.standplaatsen,
    )
    """
    Standplaats: De groep criteria die betrekking heeft op hinderlijke situaties in de
    woonomgeving (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    oppervlakte_van_overige_ruimten = WoningwaarderingstelselgroepReferentiedata(
        code="OOZ",
        naam="Oppervlakte van overige ruimten",
    )
    """
    Tot deze ruimten worden gerekend: bijkeukens, bergingen, wasruimten, schuren,
    garages, zolders en kelders (Beleidsboek Waarderingsstelsel zelfstandige
    woonruimte)
    """

    oppervlakte_onzelfstandige_woonruimte = WoningwaarderingstelselgroepReferentiedata(
        code="OPO",
        naam="Oppervlakte onzelfstandige woonruimte",
        parent=Woningwaarderingstelsel.onzelfstandige_woonruimten,
    )
    """
    De groep criteria die betrekking heeft op de oppervlakte van kamers en keukens, en
    van verwarmde gemeenschappelijke verblijfsruimten (Beleidsboek
    Waarderingsstelsel onzelfstandige woonruimte)
    """

    oppervlakte_standplaats = WoningwaarderingstelselgroepReferentiedata(
        code="OST",
        naam="Oppervlakte standplaats",
        parent=Woningwaarderingstelsel.standplaatsen,
    )
    """
    Standplaats: De groep criteria die betrekking heeft op de oppervlakte
    (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    oppervlakte_van_vertrekken = WoningwaarderingstelselgroepReferentiedata(
        code="OVZ",
        naam="Oppervlakte van vertrekken",
    )
    """
    Onder vertrekken worden verstaan: woonkamer, andere kamers, keuken, badkamer en
    doucheruimte (Beleidsboek Waarderingsstelsel zelfstandige woonruimte)
    """

    oppervlakte_niet_standaardwoonwagen = WoningwaarderingstelselgroepReferentiedata(
        code="OWN",
        naam="Oppervlakte niet-standaardwoonwagen",
        parent=Woningwaarderingstelsel.woonwagens,
    )
    """
    Niet-standaardwoonwagen: De groep criteria die betrekking heeft op de oppervlakte
    (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    oppervlakte_standaardwoonwagen = WoningwaarderingstelselgroepReferentiedata(
        code="OWS",
        naam="Oppervlakte standaardwoonwagen",
        parent=Woningwaarderingstelsel.woonwagens,
    )
    """
    Standaardwoonwagen: De groep criteria die betrekking heeft op de oppervlakte
    (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    prive_buitenruimten = WoningwaarderingstelselgroepReferentiedata(
        code="PRI",
        naam="Privé-buitenruimten",
        parent=Woningwaarderingstelsel.zelfstandige_woonruimten,
    )
    """
    Privé-buitenruimten zijn tot de woning behorende buitenruimten, waarvan de bewoners
    van de desbetreffende woning krachtens de huurovereenkomst het exclusieve
    gebruiksrecht hebben. Dit kunnen onder meer voor-, zij- of achtertuinen,
    balkons, platjes of terrassen zijn (Beleidsboek Waarderingsstelsel zelfstandige
    woonruimte)
    """

    renovatie = WoningwaarderingstelselgroepReferentiedata(
        code="REN",
        naam="Renovatie",
        parent=Woningwaarderingstelsel.zelfstandige_woonruimten,
    )
    """
    De groep criteria die betrekking heeft op renovatie van de woonruimte (Beleidsboek
    Waarderingsstelsel zelfstandige woonruimte)
    """

    sanitair = WoningwaarderingstelselgroepReferentiedata(
        code="SAN",
        naam="Sanitair",
    )
    """
    De groep criteria die betrekking heeft op het sanitair (Beleidsboek
    Waarderingsstelsel zelfstandige woonruimte)
    """

    toilet = WoningwaarderingstelselgroepReferentiedata(
        code="TOI",
        naam="Toilet",
        parent=Woningwaarderingstelsel.onzelfstandige_woonruimten,
    )
    """
    De groep criteria die betrekking heeft op de w.c. (Beleidsboek Waarderingsstelsel
    onzelfstandige woonruimte)
    """

    verwarmingsmogelijkheden = WoningwaarderingstelselgroepReferentiedata(
        code="VON",
        naam="Verwarmingsmogelijkheden",
        parent=Woningwaarderingstelsel.onzelfstandige_woonruimten,
    )
    """
    De groep criteria die betrekking heeft op de verwarmingsmogelijkheden (Beleidsboek
    Waarderingsstelsel onzelfstandige woonruimte)
    """

    verwarming_standplaats = WoningwaarderingstelselgroepReferentiedata(
        code="VST",
        naam="Verwarming standplaats",
        parent=Woningwaarderingstelsel.standplaatsen,
    )
    """
    Standplaats: De groep criteria die betrekking heeft op de verwarming (Puntentelling:
    woonwagen/standplaats: Huurcommissie)
    """

    verwarming_niet_standaardwoonwagen = WoningwaarderingstelselgroepReferentiedata(
        code="VWN",
        naam="Verwarming niet-standaardwoonwagen",
        parent=Woningwaarderingstelsel.woonwagens,
    )
    """
    Niet-standaardwoonwagen: De groep criteria die betrekking heeft op de verwarming
    (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    verwarming_standaardwoonwagen = WoningwaarderingstelselgroepReferentiedata(
        code="VWS",
        naam="Verwarming standaardwoonwagen",
        parent=Woningwaarderingstelsel.woonwagens,
    )
    """
    Standaardwoonwagen: De groep criteria die betrekking heeft op de verwarming
    (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    verwarming = WoningwaarderingstelselgroepReferentiedata(
        code="VZE",
        naam="Verwarming",
        parent=Woningwaarderingstelsel.zelfstandige_woonruimten,
    )
    """
    Vertrekken, die met punten als vertrek zijn gewaardeerd, en die verwarmd zijn. Open
    keukens, of vertrekken die met een schuifwand met elkaar in verbinding staan,
    worden als afzonderlijk vertrek geteld (Beleidsboek Waarderingsstelsel
    zelfstandige woonruimte)
    """

    wasgelegenheid = WoningwaarderingstelselgroepReferentiedata(
        code="WAS",
        naam="Wasgelegenheid",
        parent=Woningwaarderingstelsel.onzelfstandige_woonruimten,
    )
    """
    De groep criteria die betrekking heeft op douche, bad en wastafel (Beleidsboek
    Waarderingsstelsel onzelfstandige woonruimte)
    """

    punten_voor_de_woz_waarde = WoningwaarderingstelselgroepReferentiedata(
        code="WOZ",
        naam="Punten voor de WOZ-waarde",
    )
    """
    De groep criteria die betrekking heeft op de vastgestelde WOZ-waarde (Beleidsboek
    Waarderingsstelsel zelfstandige woonruimte)
    """

    woonomgeving_standplaats = WoningwaarderingstelselgroepReferentiedata(
        code="WST",
        naam="Woonomgeving standplaats",
        parent=Woningwaarderingstelsel.standplaatsen,
    )
    """
    Standplaats: De groep criteria die betrekking heeft op de woonomgeving
    (Puntentelling: woonwagen/standplaats: Huurcommissie)
    """

    verkoeling_en_verwarming = WoningwaarderingstelselgroepReferentiedata(
        code="VKV",
        naam="Verkoeling en verwarming",
    )
    """
    Waardering van verwarmde vertrekken, overige ruimten en verkeersruimten, inclusief
    extra punten voor verkoeling, op basis van NTA 8800 energielabels en
    vastgestelde eisen aan koelsystemen en verwarming.
    """

    buitenruimten = WoningwaarderingstelselgroepReferentiedata(
        code="BUI",
        naam="Buitenruimten",
    )
    """
    Waardering van privé- en gemeenschappelijke buitenruimten, met puntenaftrek voor
    woningen zonder buitenruimte.
    """

    gemeenschappelijke_parkeerruimten = WoningwaarderingstelselgroepReferentiedata(
        code="GPA",
        naam="Gemeenschappelijke parkeerruimten",
    )
    """
    Waardering van parkeerplekken in een gemeenschappelijke ruimte die exclusief
    gebruikt worden door bewoners van minimaal twee adressen, met puntentoekenning
    afhankelijk van type en aanwezigheid van laadpaal.
    """

    prijsopslag_monumenten_en_nieuwbouw = WoningwaarderingstelselgroepReferentiedata(
        code="PMN",
        naam="Prijsopslag monumenten en nieuwbouw",
        parent=Woningwaarderingstelsel.zelfstandige_woonruimten,
    )
    """
    Prijsopslagen voor monumenten en nieuwbouw, waarbij extra percentages worden
    toegevoegd aan de maximale huurprijs voor rijks-, gemeentelijke of provinciaal
    aangewezen monumenten, evenals voor nieuwbouwwoningen die aan specifieke
    criteria voldoen.
    """

    prijsopslag_monumenten = WoningwaarderingstelselgroepReferentiedata(
        code="PMO",
        naam="Prijsopslag monumenten",
        parent=Woningwaarderingstelsel.onzelfstandige_woonruimten,
    )
    """
    Prijsopslag voor monumenten op grond van artikel 8a van het Besluit huurprijzen
    woonruimte.
    """

    gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen = (
        WoningwaarderingstelselgroepReferentiedata(
            code="GVR",
            naam="Gemeenschappelijke vertrekken, overige ruimten en voorzieningen",
            parent=Woningwaarderingstelsel.zelfstandige_woonruimten,
        )
    )
    """
    Waardering van gemeenschappelijke vertrekken, overige ruimten en voorzieningen,
    exclusief toegankelijk voor bewoners van minimaal twee adressen, met uitsluiting
    van ruimten waarvoor ook door derden wordt betaald of die door de verhuurder
    worden gebruikt
    """

    gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen = (
        WoningwaarderingstelselgroepReferentiedata(
            code="GBA",
            naam="Gemeenschappelijke binnenruimten gedeeld met meerdere adressen",
            parent=Woningwaarderingstelsel.onzelfstandige_woonruimten,
        )
    )
    """
    Waardering van gemeenschappelijke binnenruimten gedeeld met meerdere adressen
    """

    bijzondere_voorzieningen_zorgwoning_en_aanbelfunctie = (
        WoningwaarderingstelselgroepReferentiedata(
            code="BIA",
            naam="Bijzondere voorzieningen: zorgwoning en aanbelfunctie",
            parent=Woningwaarderingstelsel.zelfstandige_woonruimten,
        )
    )
    """
    Waardering van bijzondere voorzieningen als aanbelfunctie met video- en
    audioverbinding, laadpaal en het geheel aan voorzieningen die de woning tot
    zorgwoning maken
    """

    bijzondere_voorzieningen_zorgwoning = WoningwaarderingstelselgroepReferentiedata(
        code="BIZ",
        naam="Bijzondere voorzieningen: zorgwoning",
        parent=Woningwaarderingstelsel.onzelfstandige_woonruimten,
    )
    """
    Waardering van bijzondere voorzieningen in een zorgwoning
    """

    aftrekpunten = WoningwaarderingstelselgroepReferentiedata(
        code="AFT",
        naam="Aftrekpunten",
        parent=Woningwaarderingstelsel.onzelfstandige_woonruimten,
    )
    """
    Aftrekpunten waardering onzelfstandige woonruimten
    """
