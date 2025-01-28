from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class OvereenkomstsoortReferentiedata(Referentiedata):
    pass


class Overeenkomstsoort(Referentiedatasoort):
    arbeid = OvereenkomstsoortReferentiedata(
        code="ARB",
        naam="Arbeid",
    )
    """
    Arbeidsovereenkomst
    """

    betalerovereenkomst = OvereenkomstsoortReferentiedata(
        code="BET",
        naam="Betalerovereenkomst",
    )
    """
    Overeenkomst waarin afspraken zijn vastgelegd met een afwijkende betaler voor een
    andere (huur-)overeenkomst
    """

    huurovereenkomst = OvereenkomstsoortReferentiedata(
        code="HUU",
        naam="Huurovereenkomst",
    )
    """
    Overeenkomst met betrekking tot het huren van roerend of onroerend goed.
    """

    inhuur = OvereenkomstsoortReferentiedata(
        code="INH",
        naam="Inhuur",
    )
    """
    Inhuurovereenkomst
    """

    inschrijving = OvereenkomstsoortReferentiedata(
        code="INS",
        naam="Inschrijving",
    )
    """
    Overeenkomst met betrekking tot de registratie van een woningzoekende in een
    woonruimteverdeel gebied.
    """

    koopovereenkomst = OvereenkomstsoortReferentiedata(
        code="KOO",
        naam="Koopovereenkomst",
    )
    """
    Overeenkomst met betrekking tot het kopen van roerend of onroerend goed.
    """

    lease = OvereenkomstsoortReferentiedata(
        code="LEA",
        naam="Lease",
    )
    """
    Leaseovereenkomst
    """

    monitoringovereenkomst = OvereenkomstsoortReferentiedata(
        code="MON",
        naam="Monitoringovereenkomst",
    )
    """
    Overeenkomst voor het monitoren van de energieprestaties en gebruik van een eenheid.
    """

    onderhoudsovereenkomst = OvereenkomstsoortReferentiedata(
        code="OND",
        naam="Onderhoudsovereenkomst",
    )
    """
    Overeenkomst met betrekking tot het onderhouden of beheren van roerend of onroerend
    goed.
    """

    serviceovereenkomst = OvereenkomstsoortReferentiedata(
        code="SER",
        naam="Serviceovereenkomst",
    )
    """
    Overeenkomst met betrekking tot (aanvullende) dienstverlening zoals glazenwassen,
    reparaties, groenverzorging. Ook de verschillende vormen van inschrijvingen of
    abonnementen vallen onder de soort Service overeenkomst.
    """
