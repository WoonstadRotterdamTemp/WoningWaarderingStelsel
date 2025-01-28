import warnings
from datetime import date
from decimal import Decimal
from importlib.resources import files

import pandas as pd
from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.criterium_id import CriteriumId
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheidadres,
    EenhedenEenheidbericht,
    WoningwaarderingCriteriumSleutels,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Meeteenheid,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)

LOOKUP_TABEL_FOLDER = (
    "stelsels/onzelfstandige_woonruimten/punten_voor_de_woz_waarde/lookup_tabellen"
)

DATUM_FORMAT = "%d-%m-%Y"


class PuntenVoorDeWozWaarde(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.punten_voor_de_woz_waarde  # verkeerde parent, zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
        super().__init__(
            begindatum=date.fromisoformat("2024-07-01"),
            einddatum=date.max,
            peildatum=peildatum,
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
                stelselgroep=self.stelselgroep,  # verkeerde parent zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
            )
        )

        adres = eenheid.adres

        if (
            adres is None
            or not isinstance(adres, EenhedenEenheidadres)
            or (
                (adres.postcode is None or adres.huisnummer is None)
                and (adres.woonplaats is None or adres.woonplaats.code is None)
            )
        ):
            warnings.warn(
                f"Eenheid {eenheid.id}: adres met woonplaatscode of postcode en huisnummer ontbreekt, COROP-gebied kan niet bepaald worden voor gemiddelde WOZ waarde",
                UserWarning,
            )
            return woningwaardering_groep

        woz_waarde, woz_waardepeildatum = self._meest_recente_woz_eenheid(eenheid)

        if woz_waardepeildatum is None:
            warnings.warn(
                f"Eenheid {eenheid.id} kon geen waardepeildatum bepalen. Kan Punten voor de WOZ-waarde niet berekenen."
            )
            return woningwaardering_groep

        woz_waarde_voor_waardering = woz_waarde

        woningwaarderingen = list[WoningwaarderingResultatenWoningwaardering]()

        puntenwaardering_sleutel = WoningwaarderingCriteriumSleutels(
            id=str(
                CriteriumId(
                    stelselgroep=self.stelselgroep,
                    criterium="percentage_verschil",
                    is_totaal=True,
                )
            )
        )

        woningwaarderingen.append(
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=f"WOZ-waarde op waardepeildatum {woz_waardepeildatum.strftime(DATUM_FORMAT)}",
                    id=str(
                        CriteriumId(
                            stelselgroep=self.stelselgroep,
                            criterium="woz_waarde",
                        )
                    ),
                    bovenliggende_criterium=puntenwaardering_sleutel,
                ),
                aantal=woz_waarde,
            )
        )

        # 11.2 Ontbreken WOZ-waarde en minimumwaarde
        # Als geen WOZ-waarde bekend is, kan als alternatief 85% van de taxatiewaarde
        # van de woning worden gebruikt volgend uit een door een Register-Taxateur
        # opgesteld (hybride)taxatierapport. De verhuurder draagt de verantwoordelijkheid
        # voor het opstellen van dit rapport. De taxatiewaarde geldt totdat een WOZ-waarde
        # is vastgesteld en vervalt voor toepassing van deze rubriek. Als de verhuurder
        # geen taxatierapport heeft aangeleverd dan geldt de minimum WOZ-waarde.
        #
        # Minimumwaarde
        # De minimum WOZ-waarde wordt ook gebruikt voor specifieke woningen van
        # specifieke verhuurders, zoals ‘containerwoningen’ die zijn bestemd voor
        # studentenhuisvesting. In die gevallen wordt een minimum WOZ-waarde gehanteerd
        # indien de WOZ-waarde lager is dan deze minimumwaarde. Deze waarde met
        # peildatum 1 januari 2023 bedraagt € 73.607. Zie de tabel hieronder voor de
        # minimumwaarde van de afgelopen jaren.

        minimum_woz_waarde = self._minimum_woz_waarde(woz_waardepeildatum) or Decimal(
            str("0")
        )

        if minimum_woz_waarde == 0:
            warnings.warn(
                f"Eenheid {eenheid.id}: geen minimum WOZ-waarde gevonden voor waardepeildatum {woz_waardepeildatum.strftime(DATUM_FORMAT)}",
                UserWarning,
            )

        if (
            woz_waarde_voor_waardering is None
            or woz_waarde_voor_waardering < minimum_woz_waarde
        ):
            logger.info(
                f"Eenheid {eenheid.id}: minimum WOZ waarde  {minimum_woz_waarde} voor waardepeildatum {woz_waardepeildatum.strftime(DATUM_FORMAT)} wordt gebruikt"
            )
            woningwaarderingen.append(
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam="Minimum WOZ-waarde gebruikt voor berekening",
                        id=str(
                            CriteriumId(
                                stelselgroep=self.stelselgroep,
                                criterium="minimum_woz_waarde",
                            )
                        ),
                        bovenliggende_criterium=puntenwaardering_sleutel,
                    ),
                    aantal=minimum_woz_waarde,
                )
            )
            woz_waarde_voor_waardering = minimum_woz_waarde

        gebruiksoppervlakte = (
            eenheid.adresseerbaar_object_basisregistratie.bag_gebruikers_oppervlakte
            if eenheid.adresseerbaar_object_basisregistratie
            else None
        )

        if gebruiksoppervlakte is None:
            warnings.warn(
                f"Eenheid {eenheid.id}: geen gebruiksoppervlakte van het verblijfsobject gevonden. Dit dient gespecificeerd te worden in het attribuut 'adresseerbaar_object_basisregistratie.bag_gebruikers_oppervlakte' op de eenheid. Kan punten voor de WOZ-waarde niet bepalen.",
                UserWarning,
            )
            return woningwaardering_groep

        woningwaarderingen.append(
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Gebruiksoppervlakte",
                    id=str(
                        CriteriumId(
                            stelselgroep=self.stelselgroep,
                            criterium="gebruiksoppervlakte",
                        )
                    ),
                    meeteenheid=Meeteenheid.vierkante_meter_m2,
                    bovenliggende_criterium=puntenwaardering_sleutel,
                ),
                aantal=gebruiksoppervlakte,
            )
        )

        woz_waarde_per_m2 = woz_waarde_voor_waardering / gebruiksoppervlakte

        woningwaarderingen.append(
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="WOZ-waarde per m²",
                    id=str(
                        CriteriumId(
                            stelselgroep=self.stelselgroep,
                            criterium="woz_waarde_per_m2",
                        )
                    ),
                    bovenliggende_criterium=puntenwaardering_sleutel,
                ),
                aantal=woz_waarde_per_m2,
            )
        )

        woonplaats = utils.get_woonplaats(adres)

        if woonplaats is None or woonplaats.code is None:
            warnings.warn(
                f"Eenheid {eenheid.id}: Geen woonplaats gevonden voor adres {adres}. Kan punten voor de WOZ-waarde niet bepalen.",
                UserWarning,
            )
            return woningwaardering_groep

        corop_gebied = utils.get_corop_voor_woonplaats(woonplaats.code)

        if corop_gebied is None:
            warnings.warn(
                f"Eenheid {eenheid.id}: Geen COROP-gebied gevonden voor woonplaats {woonplaats.naam} met woonplaatscode {woonplaats.code}. Kan punten voor de WOZ-waarde niet bepalen.",
                UserWarning,
            )
            return woningwaardering_groep

        logger.debug(
            f"Eenheid {eenheid.id} met woonplaats {woonplaats.naam} ligt in COROP-gebied {corop_gebied['naam']}"
        )

        gemiddelde_woz_waarde_per_m2 = self._gemiddelde_woz_voor_corop_gebied(
            corop_gebied, woz_waardepeildatum.year
        )

        if gemiddelde_woz_waarde_per_m2 is None:
            warnings.warn(
                f"Eenheid {eenheid.id}: Geen gemiddelde WOZ-waarde gevonden voor COROP-gebied {corop_gebied}. Kan punten voor de WOZ-waarde niet bepalen.",
                UserWarning,
            )
            return woningwaardering_groep

        logger.debug(
            f"Gemiddelde WOZ-waarde per m² voor {corop_gebied['naam']}: {gemiddelde_woz_waarde_per_m2}"
        )
        logger.debug(f"Eenheid {eenheid.id}: WOZ-waarde per m²: {woz_waarde_per_m2}")

        woningwaarderingen.append(
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=f"Gemiddelde WOZ-waarde per m² voor {corop_gebied['naam']}",
                    id=str(
                        CriteriumId(
                            stelselgroep=self.stelselgroep,
                            criterium="gemiddelde_woz_waarde_per_m2",
                        )
                    ),
                    bovenliggende_criterium=puntenwaardering_sleutel,
                ),
                aantal=gemiddelde_woz_waarde_per_m2,
            )
        )

        verschil_percentage = (
            (woz_waarde_per_m2 / gemiddelde_woz_waarde_per_m2) - 1
        ) * 100

        logger.debug(
            f"Eenheid {eenheid.id}: verschil percentage WOZ-waarde per m² en gemiddelde WOZ-waarde per m² voor {corop_gebied['naam']}: {verschil_percentage}%"
        )

        punten = 0

        # De puntentoekenning is als volgt.
        if verschil_percentage > 10:
            # 14 punten wanneer de WOZ-waarde per m² gebruiksoppervlakte meer dan 10% hoger
            # is dan de gemiddelde WOZ-waarde per m² gebruiksoppervlakte van de woningen
            # in het COROP-gebied waarbinnen de woning is gelegen.
            punten = 14
            logger.info(
                f"Eenheid {eenheid.id}: WOZ-waarde per m² (€{woz_waarde_per_m2:.0f}) is meer dan 10% hoger dan gemiddelde WOZ-waarde per m² (€{gemiddelde_woz_waarde_per_m2:.0f}) voor {corop_gebied['naam']}. {punten} punten voor {self.stelselgroep.naam}"
            )
        elif verschil_percentage >= -10:
            # 12 punten wanneer de WOZ-waarde per m² gebruiksoppervlakte maximaal 10% hoger
            # of lager is dan de gemiddelde WOZ-waarde per m² gebruiksoppervlakte van de
            # woningen in het COROP-gebied waarbinnen de woning is gelegen.
            punten = 12
            logger.info(
                f"Eenheid {eenheid.id}: WOZ-waarde per m² (€{woz_waarde_per_m2:.0f}) is maximaal 10% hoger of lager dan gemiddelde WOZ-waarde per m² (€{gemiddelde_woz_waarde_per_m2:.0f}) voor {corop_gebied['naam']}. {punten} punten voor {self.stelselgroep.naam}"
            )
        else:
            # 10 punten wanneer de WOZ-waarde per m² gebruiksoppervlakte meer dan 10% lager
            # is dan de gemiddelde WOZ-waarde per m² gebruiksoppervlakte van de woningen
            # in het COROP-gebied waarbinnen de woning is gelegen.
            punten = 10
            logger.info(
                f"Eenheid {eenheid.id}: WOZ-waarde per m² (€{woz_waarde_per_m2:.0f}) is meer dan 10% lager dan gemiddelde WOZ-waarde per m² (€{gemiddelde_woz_waarde_per_m2:.0f}) voor {corop_gebied['naam']}. {punten} punten voor {self.stelselgroep.naam}"
            )

        woningwaarderingen.append(
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Percentage verschil",
                    id=str(
                        CriteriumId(
                            stelselgroep=self.stelselgroep,
                            criterium="percentage_verschil",
                            is_totaal=True,
                        )
                    ),
                ),
                aantal=verschil_percentage,
                punten=punten,
            )
        )

        woningwaardering_groep.woningwaarderingen = woningwaarderingen
        woningwaardering_groep.punten = float(punten)

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )
        return woningwaardering_groep

    def _meest_recente_woz_eenheid(
        self, eenheid: EenhedenEenheidbericht
    ) -> tuple[Decimal | None, date | None]:
        """
        De waardepeildatum van de WOZ-waarde ligt op 1 januari van twee kalenderjaren voorafgaand.
        """
        relevante_waardepeildatums = [
            date(self.peildatum.year - 2, 1, 1)  # T-2
            # date(self.peildatum.year - 1, 1, 1),  # T-1 Tabellen voor peildatum 1-1-2023 zijn nog niet gepubliceerd
        ]

        woz_eenheden = [
            woz_eenheid
            for woz_eenheid in eenheid.woz_eenheden or []
            if woz_eenheid.waardepeildatum is not None
            and woz_eenheid.waardepeildatum in relevante_waardepeildatums
            and woz_eenheid.vastgestelde_waarde is not None
        ]

        if not woz_eenheden:
            datums = " of ".join(
                [
                    relevante_waardepeildatum.strftime(DATUM_FORMAT)
                    for relevante_waardepeildatum in relevante_waardepeildatums
                ]
            )
            warnings.warn(
                f"Eenheid {eenheid.id}: geen WOZ-waarde gevonden met waardepeildatum {datums}",
                UserWarning,
            )
            return None, max(relevante_waardepeildatums, default=None)
        else:
            meest_recente_woz_eenheid = max(
                woz_eenheden, key=lambda x: x.waardepeildatum or date.min
            )
            woz_waarde = (
                Decimal(str(meest_recente_woz_eenheid.vastgestelde_waarde))
                if meest_recente_woz_eenheid.vastgestelde_waarde is not None
                else None
            )

            return woz_waarde, meest_recente_woz_eenheid.waardepeildatum

    def _gemiddelde_woz_voor_corop_gebied(
        self, corop_gebied: dict[str, str], jaar: int
    ) -> Decimal | None:
        df_woz = pd.read_csv(
            str(
                files("woningwaardering")
                .joinpath(LOOKUP_TABEL_FOLDER)
                .joinpath("corop_gebied_gemiddelde_woz_waarde_per_m2.csv")
            ),
            dtype={"COROP-gebiedcode": str, str(jaar): str},
        )

        woz_mask = df_woz["COROP-gebiedcode"] == corop_gebied["code"]

        if not woz_mask.any():
            return None

        gemiddelde_woz_waarde_per_m2 = df_woz.loc[woz_mask, str(jaar)].values[0]

        return Decimal(gemiddelde_woz_waarde_per_m2)

    def _minimum_woz_waarde(self, woz_waardepeildatum: date) -> Decimal | None:
        df_minimum_woz_waarde = pd.read_csv(
            str(
                files("woningwaardering")
                .joinpath(LOOKUP_TABEL_FOLDER)
                .joinpath("minimum_woz_waarde.csv")
            ),
            parse_dates=["Peildatum"],
        )

        df_minimum_woz_waarde["Peildatum"] = df_minimum_woz_waarde["Peildatum"].dt.date

        minimum_woz_waarde_mask = (
            df_minimum_woz_waarde["Peildatum"] == woz_waardepeildatum
        )
        if not minimum_woz_waarde_mask.any():
            return None

        minimum_woz_waarde = df_minimum_woz_waarde.loc[
            minimum_woz_waarde_mask, "Minimumwaarde"
        ].values[0]

        return Decimal(str(minimum_woz_waarde))


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=PuntenVoorDeWozWaarde(peildatum=date(2025, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/onzelfstandige_woonruimten/input/15004000185.json")
