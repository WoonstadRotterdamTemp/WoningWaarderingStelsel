from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class EenheidmonumentReferentiedata(Referentiedata):
    pass


class Eenheidmonument(Referentiedatasoort):
    gemeentelijk_beschermd_dorpsgezicht = EenheidmonumentReferentiedata(
        code="DGG",
        naam="Gemeentelijk beschermd dorpsgezicht",
    )
    """
    Bij ontwikkelingen binnen een stads- of dorpsgezicht moet rekening gehouden met de
    cultuurhistorische waarde. Elk beschermd gebied heeft hiervoor een eigen
    bestemmingsplan. Vergeleken met een gewoon bestemmingsplan is het
    gedetailleerder en gelden er strengere regels, zowel voor de bebouwde als voor
    de onbebouwde ruimte. Bovendien is voor een aantal bouwactiviteiten een
    vergunning nodig. Het gebied is door de gemeente aangewezen als beschermd
    dorpsgezicht.
    """

    rijksbeschermd_dorpsgezicht = EenheidmonumentReferentiedata(
        code="DGR",
        naam="Rijksbeschermd dorpsgezicht",
    )
    """
    Bij ontwikkelingen binnen een stads- of dorpsgezicht moet rekening gehouden met de
    cultuurhistorische waarde. Elk beschermd gebied heeft hiervoor een eigen
    bestemmingsplan. Vergeleken met een gewoon bestemmingsplan is het
    gedetailleerder en gelden er strengere regels, zowel voor de bebouwde als voor
    de onbebouwde ruimte. Bovendien is voor een aantal bouwactiviteiten een
    vergunning nodig. Het gebied is door de rijksoverheid aangewezen als beschermd
    dorpsgezicht.
    """

    gemeentelijk_monument = EenheidmonumentReferentiedata(
        code="GEM",
        naam="Gemeentelijk monument",
    )
    """
    Een gemeente kan besluiten een bijzonder pand op de gemeentelijke monumentenlijst te
    zetten. Dit gebeurt als een pand geen nationale betekenis heeft, maar wel van
    plaatselijk of regionaal belang is.
    """

    provinciaal_monument = EenheidmonumentReferentiedata(
        code="PRO",
        naam="Provinciaal monument",
    )
    """
    Niet alleen panden, maar ook dijken, grenspalen en gemeente-overschrijdende objecten
    kunnen deel uitmaken van een provinciale monumentenlijst. De lijst wordt
    samengesteld door de Provinciale Staten van de provincie. Als een pand op de
    lijst staat, betekent het dat het pand bescherming geniet vanuit de provincie.
    Bovendien dient de lijst als basis voor eventuele subsidietoezeggingen.
    Noord-Holland en Drenthe zijn de enige provincies die provinciale monumenten
    hebben aangewezen.
    """

    rijksmonument = EenheidmonumentReferentiedata(
        code="RIJ",
        naam="Rijksmonument",
    )
    """
    Rijksmonumenten zijn gebouwen of andere objecten die om hun nationale
    cultuurhistorische waarde door de rijksoverheid zijn aangewezen als beschermd
    monument.
    """

    gemeentelijk_beschermd_stadsgezicht = EenheidmonumentReferentiedata(
        code="SGG",
        naam="Gemeentelijk beschermd stadsgezicht",
    )
    """
    Bij ontwikkelingen binnen een stads- of dorpsgezicht moet rekening gehouden met de
    cultuurhistorische waarde. Elk beschermd gebied heeft hiervoor een eigen
    bestemmingsplan. Vergeleken met een gewoon bestemmingsplan is het
    gedetailleerder en gelden er strengere regels, zowel voor de bebouwde als voor
    de onbebouwde ruimte. Bovendien is voor een aantal bouwactiviteiten een
    vergunning nodig. Het gebied is door de gemeente aangewezen als beschermd
    stadsgezicht.
    """

    rijksbeschermd_stadsgezicht = EenheidmonumentReferentiedata(
        code="SGR",
        naam="Rijksbeschermd stadsgezicht",
    )
    """
    Bij ontwikkelingen binnen een stads- of dorpsgezicht moet rekening gehouden met de
    cultuurhistorische waarde. Elk beschermd gebied heeft hiervoor een eigen
    bestemmingsplan. Vergeleken met een gewoon bestemmingsplan is het
    gedetailleerder en gelden er strengere regels, zowel voor de bebouwde als voor
    de onbebouwde ruimte. Bovendien is voor een aantal bouwactiviteiten een
    vergunning nodig. Het gebied is door de rijksoverheid aangewezen als beschermd
    stadsgezicht.
    """

    werelderfgoed = EenheidmonumentReferentiedata(
        code="WER",
        naam="Werelderfgoed",
    )
    """
    Werelderfgoederen zijn culturele of natuurlijke monumenten die mondiaal gezien
    uitzonderlijk en onvervangbaar zijn. Alleen als een monument is ingeschreven op
    de Werelderfgoedlijst van UNESCO mag het de titel Werelderfgoed dragen.
    """
