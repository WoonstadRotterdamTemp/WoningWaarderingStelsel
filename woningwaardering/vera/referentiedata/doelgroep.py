from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class DoelgroepReferentiedata(Referentiedata):
    pass


class Doelgroep(Referentiedatasoort):
    persoon = DoelgroepReferentiedata(
        code="EEN",
        naam="Persoon",
    )
    """
    Woonruimte is bestemd voor en/of huurder vormt een eenpersoonshuishouden
    """

    gezin = DoelgroepReferentiedata(
        code="GEZ",
        naam="Gezin",
    )
    """
    Leefverband van één of meer volwassenen die verantwoordelijkheid dragen voor de
    verzorging en opvoeding van één of meer kinderen.
    """

    huishouden_zonder_kinderen = DoelgroepReferentiedata(
        code="HZO",
        naam="Huishouden zonder kinderen",
    )
    """
    Huishouden zonder kinderen - Eén of meerdere volwassen personen (tot een bepaald
    maximum leeftijd) die samen een huishouden vormen en (nog) geen kinderen
    verzorgen.
    """

    jongeren = DoelgroepReferentiedata(
        code="JON",
        naam="Jongeren",
    )
    """
    Woonruimte is bestemd voor en/of huurder heeft op het moment van toewijzing een
    specifieke maximum leeftijd
    """

    senioren = DoelgroepReferentiedata(
        code="SEN",
        naam="Senioren",
    )
    """
    Woonruimte is bestemd voor en/of huurder heeft op het moment van toewijzing een
    specifieke minimum leeftijd
    """

    starter = DoelgroepReferentiedata(
        code="STA",
        naam="Starter",
    )
    """
    Woonruimte is bestemd voor en/of huurder betreft een starter op de woningmarkt
    """

    studenten = DoelgroepReferentiedata(
        code="STU",
        naam="Studenten",
    )
    """
    Woonruimte is bestemd voor en/of huurder is een student (ontvangt
    studiefinanciering, studeert voltijds of gaat promoveren).
    """

    zorg = DoelgroepReferentiedata(
        code="ZOR",
        naam="Zorg",
    )
    """
    Woonruimte is bestemd voor en/of huurder is een zorgbehoevende ((iemand die
    afhankelijk is van) woonruimte die naar aard en gebruik geen logische andere
    aanwendbaarheid kent dan een zorgwoning). Betreft o.a. aanleunwoningen en
    serviceflats.
    """

    zorgdragers = DoelgroepReferentiedata(
        code="ZDR",
        naam="Zorgdragers",
    )
    """
    Woonruimte is bestemd voor iemand die is geselecteerd op maatschappelijke motivatie/
    goede buur.
    """
