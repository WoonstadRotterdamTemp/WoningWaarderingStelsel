from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class MeeteenheidReferentiedata(Referentiedata):
    pass


class Meeteenheid(Referentiedatasoort):
    centimeter = MeeteenheidReferentiedata(
        code="CM",
        naam="Centimeter",
    )
    """
    Aantal uitgedrukt in centimeters
    """

    omvang_personeelsbestand = MeeteenheidReferentiedata(
        code="FTE",
        naam="Omvang personeelsbestand",
    )

    gram = MeeteenheidReferentiedata(
        code="GRM",
        naam="Gram",
    )
    """
    Aantal uitgedrukt in gram
    """

    kilogram = MeeteenheidReferentiedata(
        code="KGR",
        naam="Kilogram",
    )

    liter = MeeteenheidReferentiedata(
        code="LTR",
        naam="Liter",
    )

    vierkante_meter_m2 = MeeteenheidReferentiedata(
        code="M2",
        naam="Vierkante meter, m2",
    )

    kubieke_meter_m3 = MeeteenheidReferentiedata(
        code="M3",
        naam="Kubieke meter, m3",
    )

    millimeter = MeeteenheidReferentiedata(
        code="MIL",
        naam="Millimeter",
    )
    """
    Aantal uitgedrukt in millimeters
    """

    minuten = MeeteenheidReferentiedata(
        code="MIN",
        naam="Minuten",
    )
    """
    Aantal uitgedrukt in minuten, bijvoorbeeld 15 minuten reistijd
    """

    meter = MeeteenheidReferentiedata(
        code="MTR",
        naam="Meter",
    )

    stuks = MeeteenheidReferentiedata(
        code="STU",
        naam="Stuks",
    )
    """
    Aantal uitgedrukt per stuk, bijvoorbeeld 2 stuks deurklink, 10 stuks schroeven, etc.
    """

    uren = MeeteenheidReferentiedata(
        code="UUR",
        naam="Uren",
    )
    """
    Aantal uitgedrukt in uren, bijvoorbeeld 2,5 uur werktijd. 15 minuten kan uitgedrukt
    worden in 0,25 uur
    """

    euro = MeeteenheidReferentiedata(
        code="EUR",
        naam="Euro",
    )
    """
    Aantal uitgedrukt in euro's
    """
