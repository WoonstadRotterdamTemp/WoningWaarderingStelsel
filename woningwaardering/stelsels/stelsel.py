from datetime import date
from decimal import Decimal
from importlib.resources import files

import pandas as pd
from loguru import logger

from woningwaardering.stelsels.stelselgroep import (
    Stelselgroep,
)
from woningwaardering.stelsels.utils import (
    is_geldig,
    normaliseer_ruimte_namen,
    rond_af,
    rond_af_op_kwart,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheidbericht,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    WoningwaarderingstelselgroepReferentiedata,
    WoningwaarderingstelselReferentiedata,
)


class Stelsel:
    """Initialiseert een Stelsel object.

    Parameters:
        stelsel (WoningwaarderingstelselReferentiedata): Het stelsel dat wordt berekend.
        begindatum (date): De begindatum van de geldigheid van het stelsel.
        einddatum (date, optional): De einddatum van de geldigheid van het stelsel.
        peildatum (date, optional): De peildatum voor de waardering.
            Standaard is de huidige datum.
        stelselgroepen (list[type[Stelselgroep]] | None, optional): De stelselgroepen die worden berekend.

    Raises:
        ValueError: Als het stelsel niet geldig is op de peildatum.
    """

    def __init__(
        self,
        stelsel: WoningwaarderingstelselReferentiedata,
        begindatum: date,
        einddatum: date = date.max,
        peildatum: date = date.today(),
        stelselgroepen: list[type[Stelselgroep]] | None = None,
    ) -> None:
        self.stelsel = stelsel
        logger.info(f"Stelsel {stelsel.naam} wordt gebruikt.")
        if not is_geldig(begindatum, einddatum, peildatum):
            raise ValueError(
                f"Stelsel {stelsel.naam} met begindatum {begindatum} en einddatum {einddatum} is niet geldig op peildatum {peildatum}."
            )

        self.peildatum = peildatum
        self.stelselgroepen = [
            stelselgroep(peildatum) for stelselgroep in stelselgroepen or []
        ]
        self.df_maximale_huur = pd.read_csv(
            str(
                files("woningwaardering").joinpath(
                    f"stelsels/{stelsel.name}/maximale_huurprijzen.csv"
                )
            )
        )

    def waardeer(
        self,
        eenheid: EenhedenEenheidbericht,
        *,
        negeer_stelselgroep: WoningwaarderingstelselgroepReferentiedata | None = None,
    ) -> WoningwaarderingResultatenWoningwaarderingResultaat:
        """Berekent de woningwaardering voor een stelsel.

        Parameters:
            eenheid (EenhedenEenheidbericht): De eenheid waarvoor de woningwaardering wordt berekend.
            negeer_stelselgroep (WoningwaarderingstelselgroepReferentiedata | None, optional): Een stelselgroep die moet worden overgeslagen.

        Returns:
            WoningwaarderingResultatenWoningwaarderingResultaat: Het bijgewerkte resultaat van de woningwaardering.
        """

        normaliseer_ruimte_namen(eenheid)

        resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
        resultaat.stelsel = self.stelsel

        resultaat.groepen = []

        for stelselgroep in self.stelselgroepen:
            if (
                negeer_stelselgroep is not None
                and stelselgroep.stelselgroep == negeer_stelselgroep
            ):
                continue

            resultaat.groepen.append(stelselgroep.waardeer(eenheid, resultaat))

        resultaat.punten = float(Stelsel.bereken_puntentotaal(resultaat))

        resultaat.opslagpercentage = (
            sum(
                woningwaardering_groep.opslagpercentage
                for woningwaardering_groep in resultaat.groepen or []
                if woningwaardering_groep.opslagpercentage is not None
            )
            or None
        )

        maximale_huur = self.bereken_maximale_huur(resultaat)

        resultaat.maximale_huur = float(maximale_huur)

        huurprijsopslag = rond_af(
            maximale_huur * Decimal(str(resultaat.opslagpercentage or 0)),
            decimalen=2,
        )

        resultaat.huurprijsopslag = float(huurprijsopslag)

        resultaat.maximale_huur_inclusief_opslag = float(
            maximale_huur + huurprijsopslag
        )

        return resultaat

    @staticmethod
    def bereken_puntentotaal(
        resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    ) -> Decimal:
        # Het puntentotaal per woning wordt na eindsaldering (met inbegrip van de bij
        # zorgwoningen geldende toeslag) afgerond op hele punten.
        # Bij 0,5 punten of meer wordt afgerond naar boven op hele punten, bij minder
        # dan 0,5 punten wordt afgerond naar beneden op hele punten. In de
        # eindsaldering zitten ook de punten voor eventuele gemeenschappelijke ruimten
        # en voorzieningen.
        return rond_af(
            sum(
                # De waardering in punten wordt per rubriek na saldering afgerond op
                # 0,25 punt waarbij een achtste (1/8) punt naar boven wordt afgerond.
                # Dat wil zeggen dat 0,125 wordt afgerond naar 0,25. Een kwartpunt is
                # de kleinst werkbare waardering binnen het woningwaarderingsstelsel
                # voor een afzonderlijke rubriek.
                rond_af_op_kwart(woningwaardering_groep.punten)
                for woningwaardering_groep in resultaat.groepen or []
                if woningwaardering_groep.punten is not None
            ),
            decimalen=0,
        )

    def bereken_maximale_huur(
        self, resultaat: WoningwaarderingResultatenWoningwaarderingResultaat
    ) -> Decimal:
        punten = Decimal(str(resultaat.punten))

        df_maximale_huur = self.df_maximale_huur

        begrensde_punten = min(
            max(punten, df_maximale_huur["Punten"].min()),
            df_maximale_huur["Punten"].max(),
        )

        maximale_huur = Decimal(
            df_maximale_huur[df_maximale_huur["Punten"] == begrensde_punten][
                "Bedrag"
            ].item()
        )

        # In geval van een woonruimte met méér dan 250 punten wordt de maximale
        # huurprijs als volgt berekend: elk punt boven de 250 wordt vermenigvuldigd met
        # het verschil tussen de bedragen, genoemd in de huurprijstabel (zie bijlage 5)
        # bij 249 en 250 punten. Het verkregen bedrag wordt vervolgens opgeteld bij de
        # maximale huurprijs die volgens de huurprijstabel behoort bij 250 punten.
        hoogste_twee = df_maximale_huur.nlargest(2, "Punten")
        hoogste_punten = Decimal(hoogste_twee.iloc[0]["Punten"])
        hoogste_bedrag = Decimal(hoogste_twee.iloc[0]["Bedrag"])
        een_na_hoogste_bedrag = Decimal(hoogste_twee.iloc[1]["Bedrag"])

        bedrag_verschil = hoogste_bedrag - een_na_hoogste_bedrag

        punten_boven_hoogste = max(punten - hoogste_punten, Decimal(0))
        aanvullende_waarde = punten_boven_hoogste * bedrag_verschil

        maximale_huur += aanvullende_waarde

        return maximale_huur
