from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class MonitorintervalReferentiedata(Referentiedata):
    pass


class Monitorinterval(Referentiedatasoort):
    monitorinterval_5_minuten = MonitorintervalReferentiedata(
        code="5MI",
        naam="5 minuten",
    )

    kwartier = MonitorintervalReferentiedata(
        code="KWT",
        naam="Kwartier",
    )

    uur = MonitorintervalReferentiedata(
        code="UUR",
        naam="Uur",
    )

    dag = MonitorintervalReferentiedata(
        code="DAG",
        naam="Dag",
    )

    week = MonitorintervalReferentiedata(
        code="WEE",
        naam="Week",
    )

    maand = MonitorintervalReferentiedata(
        code="MAA",
        naam="Maand",
    )

    kwartaal = MonitorintervalReferentiedata(
        code="KWA",
        naam="Kwartaal",
    )

    jaar = MonitorintervalReferentiedata(
        code="JAA",
        naam="Jaar",
    )

    variabel = MonitorintervalReferentiedata(
        code="VAR",
        naam="Variabel",
    )
