import warnings
from datetime import date
from decimal import ROUND_DOWN, Decimal
from importlib.resources import files
from itertools import chain

import pandas as pd
from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.criterium_id import CriteriumId
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheidbericht,
    EenhedenWozEenheid,
    WoningwaarderingCriteriumSleutels,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.referentiedata.meeteenheid import Meeteenheid
from woningwaardering.vera.referentiedata.ruimtedetailsoort import Ruimtedetailsoort

LOOKUP_TABEL_FOLDER = (
    "stelsels/zelfstandige_woonruimten/punten_voor_de_woz_waarde/lookup_tabellen"
)

DATUM_FORMAT = "%d-%m-%Y"


class PuntenVoorDeWozWaarde(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        super().__init__(
            begindatum=date(2025, 1, 1),
            einddatum=date.max,
            peildatum=peildatum,
        )
        self.stelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.punten_voor_de_woz_waarde
        self.pd_woz_factor = pd.read_csv(
            files("woningwaardering").joinpath(f"{LOOKUP_TABEL_FOLDER}/woz_factor.csv"),
            parse_dates=["Peildatum"],
        )
        self.pd_minimum_woz_waarde = pd.read_csv(
            files("woningwaardering").joinpath(
                f"{LOOKUP_TABEL_FOLDER}/minimum_woz_waarde.csv"
            ),
            parse_dates=["Peildatum"],
        )

    def waardeer(
        self,
        eenheid: EenhedenEenheidbericht,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=self.stelsel,
                stelselgroep=self.stelselgroep,
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        if not woningwaardering_resultaat or not woningwaardering_resultaat.groepen:
            logger.warning(
                "Geen woningwaardering resultaat gevonden: Woningwaarderingresultaat wordt aangemaakt"
            )
            from woningwaardering.stelsels.zelfstandige_woonruimten.zelfstandige_woonruimten import (
                ZelfstandigeWoonruimten,
            )

            woningwaardering_resultaat = ZelfstandigeWoonruimten(
                peildatum=self.peildatum
            ).waardeer(
                eenheid,
                negeer_stelselgroep=Woningwaarderingstelselgroep.punten_voor_de_woz_waarde,
            )

        woz_eenheid = self.bepaal_woz_eenheid(eenheid)

        if woz_eenheid is None:
            warnings.warn(
                f"Eenheid ({eenheid.id}): geen WOZ-waarde gevonden", UserWarning
            )
            return woningwaardering_groep

        if woz_eenheid.vastgestelde_waarde is None:
            warnings.warn("Vastgestelde WOZ-waarde in WOZ-eenheid is None")
            return woningwaardering_groep

        if woz_eenheid.waardepeildatum is None:
            warnings.warn("Waardepeildatum in WOZ-eenheid is None")
            return woningwaardering_groep

        logger.info(
            f"Eenheid ({eenheid.id}): WOZ-waarde op waardepeildatum {woz_eenheid.waardepeildatum} is €{woz_eenheid.vastgestelde_waarde:.0f}"
        )

        woz_waarde = self.minimum_woz_waarde(woz_eenheid)

        if woz_waarde is None:
            warnings.warn(
                f"Eenheid ({eenheid.id}): geen minimum WOZ-waarde gevonden", UserWarning
            )
            return woningwaardering_groep

        factoren = self.pd_woz_factor[
            self.pd_woz_factor["Peildatum"]
            == pd.to_datetime(woz_eenheid.waardepeildatum)
        ]
        if len(factoren) != 1:
            raise ValueError(
                f"Eenheid ({eenheid.id}): lookup-table gefaald voor peildatum {woz_eenheid.waardepeildatum} voor {self.stelselgroep.naam}."
            )

        factor_onderdeel_I = Decimal(str(factoren["Onderdeel I"].values[0]))
        factor_onderdeel_II = Decimal(str(factoren["Onderdeel II"].values[0]))

        punten_onderdeel_I = utils.rond_af(
            (woz_waarde / factor_onderdeel_I), decimalen=2
        )

        logger.info(
            f"Eenheid ({eenheid.id}): Punten voor de WOZ-waarde onderdeel I is {woz_waarde:.0f} / {factor_onderdeel_I:.0f} = {punten_onderdeel_I:.2f}"
        )

        id_onderdeel_I = str(
            CriteriumId(
                stelselgroep=self.stelselgroep, criterium="onderdeel_I", is_totaal=True
            )
        )
        id_onderdeel_II = str(
            CriteriumId(
                stelselgroep=self.stelselgroep, criterium="onderdeel_II", is_totaal=True
            )
        )

        woningwaardering_groep.woningwaarderingen.append(
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=f"WOZ-waarde op waardepeildatum {woz_eenheid.waardepeildatum.strftime(DATUM_FORMAT)}",
                    id=str(
                        CriteriumId(
                            stelselgroep=self.stelselgroep,
                            criterium="woz_waarde",
                        )
                    ),
                ),
                aantal=int(woz_eenheid.vastgestelde_waarde),
            )
        )
        # indien de woz-waarde niet gelijk is aan de vastgestelde waarde, is de minimale woz-waarde van toepassing
        if woz_waarde != woz_eenheid.vastgestelde_waarde:
            woningwaardering_groep.woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam="Minimum WOZ-waarde gebruikt voor berekening",
                        id=str(
                            CriteriumId(
                                stelselgroep=self.stelselgroep,
                                criterium="minimum_woz_waarde",
                            )
                        ),
                        bovenliggende_criterium=WoningwaarderingCriteriumSleutels(
                            id=id_onderdeel_I,
                        ),
                    ),
                    aantal=int(woz_waarde),
                )
            )
        woningwaardering_groep.woningwaarderingen.append(
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Factor I",
                    id=str(
                        CriteriumId(
                            stelselgroep=self.stelselgroep,
                            criterium="factor_I",
                        )
                    ),
                    bovenliggende_criterium=WoningwaarderingCriteriumSleutels(
                        id=id_onderdeel_I,
                    ),
                ),
                aantal=factor_onderdeel_I,
            )
        )
        woningwaardering_groep.woningwaarderingen.append(
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Onderdeel I",
                    id=id_onderdeel_I,
                ),
                punten=punten_onderdeel_I,
            )
        )

        oppervlakte = self.bepaal_oppervlakte(eenheid, woningwaardering_resultaat)

        if oppervlakte == 0:
            warnings.warn(
                f"Eenheid ({eenheid.id}): kan geen punten voor de WOZ waarde berekenen omdat het totaal van de oppervlakte van stelselgroepen {Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.naam} en {Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam} 0 is",
                UserWarning,
            )
            return woningwaardering_groep

        punten_onderdeel_II = utils.rond_af(
            woz_waarde / oppervlakte / factor_onderdeel_II,
            decimalen=2,
        )

        logger.info(
            f"Eenheid ({eenheid.id}): Punten voor de WOZ-waarde onderdeel II is {woz_waarde:.0f} / {oppervlakte:.2f} / {factor_onderdeel_II:.0f} = {punten_onderdeel_II:.2f}"
        )

        # indien de woz-waarde niet gelijk is aan de vastgestelde waarde, is de minimale woz-waarde van toepassing
        if woz_waarde != woz_eenheid.vastgestelde_waarde:
            woningwaardering_groep.woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam="Minimum WOZ-waarde gebruikt voor berekening",
                        id=str(
                            CriteriumId(
                                stelselgroep=self.stelselgroep,
                                criterium="minimum_woz_waarde",
                            )
                        ),
                        bovenliggende_criterium=WoningwaarderingCriteriumSleutels(
                            id=id_onderdeel_II,
                        ),
                    ),
                    aantal=int(woz_waarde),
                )
            )

        woningwaardering_groep.woningwaarderingen.append(
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Oppervlakte van vertrekken en overige ruimten",
                    id=str(
                        CriteriumId(
                            stelselgroep=self.stelselgroep,
                            criterium="oppervlakte_vertrekken_en_overige_ruimten",
                        )
                    ),
                    bovenliggende_criterium=WoningwaarderingCriteriumSleutels(
                        id=id_onderdeel_II,
                    ),
                    meeteenheid=Meeteenheid.vierkante_meter_m2,
                ),
                aantal=oppervlakte,
            )
        )
        woningwaardering_groep.woningwaarderingen.append(
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Factor II",
                    id=str(
                        CriteriumId(
                            stelselgroep=self.stelselgroep,
                            criterium="factor_II",
                        )
                    ),
                    bovenliggende_criterium=WoningwaarderingCriteriumSleutels(
                        id=id_onderdeel_II,
                    ),
                ),
                aantal=factor_onderdeel_II,
            )
        )

        woningwaardering_groep.woningwaarderingen.append(
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Onderdeel II",
                    id=id_onderdeel_II,
                ),
                punten=float(punten_onderdeel_II),
            )
        )

        woningwaardering_groep = self._corrigeer_woz_punten(
            eenheid, woningwaardering_groep, woningwaardering_resultaat
        )

        punten = self._som_woz_punten(woningwaardering_groep)

        woningwaardering_groep.punten = float(utils.rond_af(punten, decimalen=0))

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )

        return woningwaardering_groep

    def _corrigeer_woz_punten(
        self,
        eenheid: EenhedenEenheidbericht,
        woningwaardering_groep: WoningwaarderingResultatenWoningwaarderingGroep,
        woningwaardering_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        """
        Controleert of de punten voor de stelselgroep WOZ-waarde voldoen aan de minimum punten en de maximum hoeveelheid punten.
        Een correctie vindt plaats wanneer:
            - Een nieuwbouwwoning niet het minimum aantal punten heeft.
            - De punten voor WOZ-waarde meer dan 33.33% van het totaal aantal punten bedraagt en geen nieuwbouwwoning is.

        Args:
            eenheid (EenhedenEenheidbericht): De eenheid.
            woningwaardering_groep (WoningwaarderingResultatenWoningwaarderingGroep): De woningwaardering groep.
            woningwaardering_resultaat (WoningwaarderingResultatenWoningwaarderingResultaat): woningwaardering resultaten.

        Returns:
            WoningwaarderingResultatenWoningwaarderingGroep: De woningwaardering groep met eventuele correcties.
        """

        woz_punten = self._som_woz_punten(woningwaardering_groep)

        minimum_woz_punten = self._bereken_minimum_punten_nieuwbouw(
            eenheid, woningwaardering_resultaat
        )

        if (
            0.0 < woz_punten < minimum_woz_punten
            and woningwaardering_groep.woningwaarderingen is not None
        ):
            woningwaardering_groep.woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=f"Nieuwbouw: min. {minimum_woz_punten} punten",
                        id=str(
                            CriteriumId(
                                stelselgroep=self.stelselgroep,
                                criterium="nieuwbouw_minimum_punten",
                            )
                        ),
                    ),
                    punten=float(minimum_woz_punten - woz_punten),
                )
            )
            return woningwaardering_groep

        # Bereken de overige punten door de punten van alle groepen op te tellen, afgerond op 0 decimalen
        overige_punten = utils.rond_af(
            sum(
                Decimal(str(groep.punten)) or Decimal("0")
                for groep in woningwaardering_resultaat.groepen or []
                if groep.punten
            ),
            0,
        )

        totaal_punten_zonder_cap = overige_punten + utils.rond_af(woz_punten, 0)
        correctie_punten = self._cap_punten(woz_punten, overige_punten)

        if (
            correctie_punten is not None
            and minimum_woz_punten == 0.0
            and woningwaardering_groep.woningwaarderingen is not None
        ):
            totaal_punten_met_cap = totaal_punten_zonder_cap + correctie_punten

            logger.debug(
                f"Eenheid ({eenheid.id}): Waardering zonder cap: {totaal_punten_zonder_cap} punten. Na toepassing van cap: {totaal_punten_met_cap} punten."
            )

            # Wanneer een woning zonder die beperking een waardering heeft van meer dan
            # 186 punten en door deze beperking een waardering krijgt die lager is dan
            # 187 punten, geldt een waardering van 186 punten voor de woning.
            if totaal_punten_zonder_cap > 186 and totaal_punten_met_cap < 187:
                logger.info(
                    f"Eenheid ({eenheid.id}) wordt gewaardeerd met 186 punten totaal door de cap op de WOZ voor {self.stelselgroep.naam}"
                )
                correctie_punten = 186 - totaal_punten_zonder_cap
                woningwaardering_groep.woningwaarderingen.append(
                    WoningwaarderingResultatenWoningwaardering(
                        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                            naam="Maximering WOZ-punten tot 186 punten totaal",
                            id=str(
                                CriteriumId(
                                    stelselgroep=self.stelselgroep,
                                    criterium="maximering_woz_punten",
                                )
                            ),
                        ),
                        punten=utils.rond_af(correctie_punten, 2),
                    )
                )
            else:
                logger.info(
                    f"Eenheid ({eenheid.id}) wordt gewaardeerd met maximaal 33% van het totale puntenaantal van de eenheid door de cap op de WOZ voor {self.stelselgroep.naam}"
                )
                woningwaardering_groep.woningwaarderingen.append(
                    WoningwaarderingResultatenWoningwaardering(
                        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                            naam="Maximering WOZ-punten tot 33% van totaal",
                            id=str(
                                CriteriumId(
                                    stelselgroep=self.stelselgroep,
                                    criterium="maximering_woz_punten",
                                )
                            ),
                        ),
                        punten=utils.rond_af(correctie_punten, 2),
                    )
                )

        return woningwaardering_groep

    def _cap_punten(
        self,
        woz_punten: Decimal,
        overige_punten: Decimal,
    ) -> Decimal | None:
        """
        Berekent de cap op de WOZ. Maximaal 33% van het
        totale puntenaantal van een woning mag bepaald worden door de WOZ-waarde
        van de woning.

        Args:
            woz_punten (Decimal): Het aantal punten voor de stelselgroep WOZ-waarde.
            overige_punten (Decimal): Het totaal aantal punten van alle groepen behalve de stelselgroep WOZ-waarde.

        Returns:
            Decimal | None: De correctiepunten voor de stelselgroep WOZ-waarde.
        """
        drempel_cap_woz = Decimal("187")

        totaal_punten_zonder_cap = overige_punten + utils.rond_af(woz_punten, 0)

        if totaal_punten_zonder_cap < drempel_cap_woz:
            logger.info(
                f"Cap op op de WOZ wordt niet toegepast omdat het totaal aantal punten minder is dan {drempel_cap_woz}."
            )
            return None

        # Bereken het maximum aantal WOZ-punten dat toegestaan is
        max_woz_percentage = Decimal("33")
        overige_percentage = Decimal("100") - max_woz_percentage
        percentage_verhouding = overige_percentage / max_woz_percentage
        max_woz_punten = overige_punten / percentage_verhouding

        # Pas de cap toe op de WOZ-punten
        capped_woz_punten = min(
            Decimal(str(woz_punten)),
            max_woz_punten,
        )

        # Als de capped WOZ-punten gelijk zijn aan of groter zijn dan de oorspronkelijke
        # WOZ-punten, pas dan geen cap toe
        if capped_woz_punten >= Decimal(str(woz_punten)):
            return None
        else:
            # Indien het puntenaandeel voor de WOZ-waarde wordt beperkt op
            # ten hoogste 33%, wordt het aantal punten voor de WOZ-waarde afgerond naar
            # beneden op hele punten.
            correctiepunten = capped_woz_punten - Decimal(str(woz_punten))
            logger.debug(f"Cap punten: {correctiepunten}")
            afrondingscorrectie = min(
                (
                    utils.rond_af(capped_woz_punten, 0, rounding=ROUND_DOWN)
                    - capped_woz_punten
                ),
                Decimal(0.0),
            )
            logger.debug(f"Afronding punten: {afrondingscorrectie}")

            totaal_correctiepunten = correctiepunten + afrondingscorrectie

            return totaal_correctiepunten

    def _som_woz_punten(
        self, woningwaardering_groep: WoningwaarderingResultatenWoningwaarderingGroep
    ) -> Decimal:
        """
        Berekent de som van de punten voor de stelselgroep WOZ-waarde.

        Args:
            woningwaardering_groep (WoningwaarderingResultatenWoningwaarderingGroep): De woningwaardering groep voor de stelselgroep WOZ-waarde.

        Returns:
            Decimal: De som van de punten voor de stelselgroep WOZ-waarde.
        """

        return Decimal(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            )
        )

    def minimum_woz_waarde(self, woz_eenheid: EenhedenWozEenheid) -> Decimal | None:
        """
        Bepaalt de minimum WOZ-waarde.

        Args:
            woz_eenheid (EenhedenWozEenheid): De WOZ-eenheid.

        Returns:
            Decimal | None: De minimum WOZ-waarde, of None indien er geen minimum vastgesteld kan worden.

        Raises:
            ValueError: Als er iets onverwachts fout gaat bij het gebruiken van een lookup-tabel.
        """
        if woz_eenheid.vastgestelde_waarde is None:
            warnings.warn("Vastgestelde WOZ-waarde in WOZ-eenheid is None")
            return None

        if woz_eenheid.waardepeildatum is None:
            warnings.warn("Waardepeildatum in WOZ-eenheid is None")
            return None

        vastgestelde_waarde = Decimal(str(woz_eenheid.vastgestelde_waarde))

        filtered_df = self.pd_minimum_woz_waarde[
            self.pd_minimum_woz_waarde["Peildatum"]
            == pd.to_datetime(woz_eenheid.waardepeildatum)
        ]
        if len(filtered_df) != 1:
            raise ValueError(
                f"Eenheid ({woz_eenheid.id}): lookup-table gefaald voor peildatum {woz_eenheid.waardepeildatum} voor {self.stelselgroep.naam}."
            )
        minimum_woz_waarde = Decimal(str(filtered_df["Minimumwaarde"].values[0]))

        if vastgestelde_waarde < minimum_woz_waarde:
            logger.info(
                f"WOZ-waarde €{vastgestelde_waarde:.0f} is kleiner dan minimum €{minimum_woz_waarde:.0f}, minimum wordt gebruikt"
            )
            return minimum_woz_waarde

        logger.debug(
            f"WOZ-waarde €{vastgestelde_waarde:.0f} is groter dan minimum €{minimum_woz_waarde:.0f}, minimum wordt niet gebruikt"
        )

        return vastgestelde_waarde

    def bepaal_oppervlakte(
        self,
        eenheid: EenhedenEenheidbericht,
        woningwaardering_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    ) -> Decimal:
        """
        Geeft de totale oppervlakte van de stelselgroepen oppervlakte van vertrekken, oppervlakte van overige ruimten
        en de som van de oppervlakte van parkeerplekken Type I uit Rubriek 10 / het aantal adressen waar iedere parkeerplek Type I mee gedeeld wordt.

        Args:
            eenheid (EenhedenEenheidbericht): De eenheid.
            woningwaardering_resultaat (WoningwaarderingResultatenWoningwaarderingResultaat): woningwaardering resultaten object.

        Returns:
            Decimal: De totale oppervlakte van de stelselgroepen oppervlakte van vertrekken en oppervlakte van overige ruimten.
        """
        oppervlakte_stelsel_groepen = [
            groep
            for groep in (woningwaardering_resultaat.groepen or [])
            if (
                groep.criterium_groep is not None
                and groep.criterium_groep.stelselgroep
                in (
                    Woningwaarderingstelselgroep.oppervlakte_van_vertrekken,
                    Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten,
                )
            )
        ]

        oppervlakte = sum(
            (
                Decimal(str(waardering.aantal))
                for waardering in chain.from_iterable(
                    groep.woningwaarderingen or []
                    for groep in oppervlakte_stelsel_groepen
                )
                if waardering.aantal is not None
            ),
            start=Decimal("0"),
        )
        logger.info(
            f"Eenheid ({eenheid.id}): Oppervlakte stelselgroepen van {Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.naam} plus {Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten.naam} is {oppervlakte}m2"
        )

        # In dit onderdeel van de berekening dient ook het aantal m2 van parkeerplekken uit rubriek 10,
        # voor zover het een parkeerplek type I (een parkeerplek in een afgesloten parkeergarage behorende tot het complex) betreft, te worden meegenomen.
        # Hiervoor kan de standaard maatvoering van 12 m2 per plaats gehanteerd worden.
        parkeerplekken_oppervlakte = sum(
            [
                Decimal(str(ruimte.oppervlakte))
                * Decimal(str(ruimte.aantal or 1))
                / (Decimal(str(ruimte.gedeeld_met_aantal_eenheden or 2)))
                for ruimte in (eenheid.ruimten or [])
                if ruimte.detail_soort
                in [Ruimtedetailsoort.parkeervak_auto_binnen]  # Type I
                and utils.gedeeld_met_eenheden(
                    ruimte
                )  # valt anders niet onder rubriek 10
                and ruimte.oppervlakte
                and Decimal(str(ruimte.oppervlakte))
                >= 12  # valt anders niet onder rubriek 10
            ]
        )
        if parkeerplekken_oppervlakte > 0:
            logger.info(
                f"Eenheid ({eenheid.id}): Oppervlakte parkeerplekken Type I van {Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten.naam} is {parkeerplekken_oppervlakte}m2"
            )

        return oppervlakte + Decimal(str(parkeerplekken_oppervlakte))

    def _bereken_minimum_punten_nieuwbouw(
        self,
        eenheid: EenhedenEenheidbericht,
        woningwaardering_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    ) -> Decimal:
        """
        Berekent de minimum punten voor steselgroep WOZ-waarde bij nieuwbouw of hoogniveau renovatie.

        Args:
            eenheid (EenhedenEenheidbericht): De eenheid.
            woningwaardering_resultaat (WoningwaarderingResultatenWoningwaarderingResultaat): woningwaardering resultaten.

        Returns:
            Decimal: De minimum punten voor stelselgroep WOZ-waarde.
        """

        minimum_punten = Decimal("0")
        if not eenheid.bouwjaar:
            warnings.warn(
                f"Eenheid ({eenheid.id}): geen bouwjaar gevonden. Kan niet bepalen of woning onder nieuwbouw valt.",
                UserWarning,
            )

        bouwjaar = eenheid.bouwjaar

        # Indien de bouwkundige oplevering of hoogniveau renovatie van de woning heeft
        # plaatsgevonden in de jaren 2015-2019 en die woning voor de onderdelen
        # 1 t/m 10 en 12 van het woningwaarderingsstelsel minimaal 110 punten heeft
        # behaald dan worden, voor het aantal punten voor de WOZ-waarde,
        # minimaal 40 punten toegekend.
        if bouwjaar and 2015 <= bouwjaar <= 2019:
            punten_critische_stelselgroepen = sum(
                groep.punten or 0.0
                for groep in woningwaardering_resultaat.groepen or []
                if groep.punten
                and groep.criterium_groep
                and groep.criterium_groep.stelselgroep
                in (
                    Woningwaarderingstelselgroep.oppervlakte_van_vertrekken,  # 1
                    Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten,  # 2
                    Woningwaarderingstelselgroep.verkoeling_en_verwarming,  # 3
                    Woningwaarderingstelselgroep.energieprestatie,  # 4
                    Woningwaarderingstelselgroep.keuken,  # 5
                    Woningwaarderingstelselgroep.sanitair,  # 6
                    Woningwaarderingstelselgroep.woonvoorzieningen_voor_gehandicapten,  # 7
                    Woningwaarderingstelselgroep.buitenruimten,  # 8
                    Woningwaarderingstelselgroep.gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen,  # 9
                    Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten,  # 10
                    Woningwaarderingstelselgroep.bijzondere_voorzieningen,  # 12
                )
            )
            logger.debug(
                f"Eenheid ({eenheid.id}): nieuwbouw of hoogniveau renovatie in de jaren 2015-2019. Punten voor de stelselgroepen 1 t/m 10 en 12: {punten_critische_stelselgroepen}"
            )
            if punten_critische_stelselgroepen >= 110:
                minimum_punten = Decimal("40")
                logger.info(
                    f"Eenheid ({eenheid.id}): nieuwbouw of hoogniveau renovatie in de jaren 2015-2019 en >= 110 punten voor de stelselgroepen 1 t/m 10 en 12. Minimaal 40 punten voor {self.stelselgroep.naam}"
                )

        return minimum_punten

    def bepaal_woz_eenheid(
        self, eenheid: EenhedenEenheidbericht
    ) -> EenhedenWozEenheid | None:
        """
        bepaalt de WOZ-waarde voor de eenheid.

        Args:
            eenheid (EenhedenEenheidbericht): de eenheid waarvoor de WOZ-waarde wordt bepaald.

        Returns:
            EenhedenWozEenheid | None: de WOZ-waarde.
        """
        woz_eenheden = sorted(
            (
                woz_eenheid
                for woz_eenheid in (eenheid.woz_eenheden or [])
                if woz_eenheid.waardepeildatum is not None
                and woz_eenheid.waardepeildatum.year
                in [self.peildatum.year - 1, self.peildatum.year - 2]
            ),
            key=lambda x: x.waardepeildatum or date.min,
            reverse=True,
        )

        # Kies de eerste waarde uit de gesorteerde lijst
        woz_waarde = next(iter(woz_eenheden), None)

        return woz_waarde


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=PuntenVoorDeWozWaarde(peildatum=date(2025, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/generiek/input/37101000032.json")
