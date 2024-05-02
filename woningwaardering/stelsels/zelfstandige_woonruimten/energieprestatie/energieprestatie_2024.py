import datetime
from decimal import Decimal
import zoneinfo
from loguru import logger

from woningwaardering.stelsels.stelselgroepversie import Stelselgroepversie
from woningwaardering.stelsels.utils import (
    dataframe_heeft_een_rij,
    filter_dataframe_op_peildatum,
    lees_csv_als_dataframe,
    naar_tabel,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenEnergieprestatie,
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
from woningwaardering.vera.referentiedata.energieprestatiestatus import (
    Energieprestatiestatus,
)

LOOKUP_TABEL_FOLDER = "woningwaardering/stelsels/zelfstandige_woonruimten/energieprestatie/lookup_tabellen"


class Energieprestatie2024(Stelselgroepversie):
    lookup_mappping = {
        "nieuw_0-25": lees_csv_als_dataframe(
            f"{LOOKUP_TABEL_FOLDER}/nieuw_0-25m2_energielabel_punten.csv"
        ),
        "nieuw_25-40": lees_csv_als_dataframe(
            f"{LOOKUP_TABEL_FOLDER}/nieuw_25-40m2_energielabel_punten.csv"
        ),
        "nieuw_40+": lees_csv_als_dataframe(
            f"{LOOKUP_TABEL_FOLDER}/nieuw_40m2+_energielabel_punten.csv"
        ),
        "oud": lees_csv_als_dataframe(
            f"{LOOKUP_TABEL_FOLDER}/oud_energielabel_punten.csv"
        ),
        "bouwjaar": lees_csv_als_dataframe(
            f"{LOOKUP_TABEL_FOLDER}/bouwjaar_punten.csv"
        ),
    }

    @staticmethod
    def bereken(
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=Woningwaarderingstelsel.zelfstandige_woonruimten.value,
                stelselgroep=Woningwaarderingstelselgroep.energieprestatie.value,
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        # TODO:
        # oppervlakte? waar kom die vandaan?
        # eengezins of meergezinswoning?
        oppervlakte = 40

        energieprestatie = (
            Energieprestatie2024._krijg_energieprestatie_met_geldig_label(eenheid)
        )

        if not (energieprestatie or eenheid.bouwjaar):
            logger.warning(
                f"Eenheid {eenheid.id} heeft geen geldig energielabel en geen bouwjaar en komt daarom niet in aanmerking voor stelselgroep {Woningwaarderingstelselgroep.energieprestatie.naam}"
            )
            return woningwaardering_groep

        woningwaardering = WoningwaarderingResultatenWoningwaardering()

        if energieprestatie and energieprestatie.label and oppervlakte:
            if (
                energieprestatie.registratiedatum
                and energieprestatie.registratiedatum
                >= datetime.datetime(
                    2021, 1, 1, tzinfo=zoneinfo.ZoneInfo("EUROPE/AMSTERDAM")
                )
            ):
                critetium_naam = f"Energielabel {energieprestatie.label.naam} + oppervlakte {oppervlakte}m2"
                woningwaardering.criterium = (
                    WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=critetium_naam,
                    )
                )
                if oppervlakte < 25.0:
                    lookup_key = "nieuw_0-25"

                elif 25.0 <= oppervlakte < 40.0:
                    lookup_key = "nieuw_25-40"

                else:
                    lookup_key = "nieuw_40+"

            else:
                critetium_naam = (
                    f"Energielabel {energieprestatie.label.naam} (voor 2021-01-01)"
                )
                woningwaardering.criterium = (
                    WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=critetium_naam,
                    )
                )
                lookup_key = "oud"

            df = Energieprestatie2024.lookup_mappping[lookup_key].pipe(
                filter_dataframe_op_peildatum, peildatum=datetime.date(2024, 1, 1)
            )

            filtered_df = df[(df["Label"] == energieprestatie.label.naam)]

            if dataframe_heeft_een_rij(filtered_df):
                punten = filtered_df["Eengezinswoning"].values[0]
                logger.debug(
                    f"Eenheid {eenheid.id} met {critetium_naam} krijgt {punten} punten voor stelselgroep {Woningwaarderingstelselgroep.energieprestatie.naam}."
                )
                woningwaardering.punten = float(punten)

        elif eenheid.bouwjaar and not energieprestatie:
            woningwaardering.criterium = (
                WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=f"Eenheid met bouwjaar {eenheid.bouwjaar}",
                )
            )
            df = Energieprestatie2024.lookup_mappping["bouwjaar"].pipe(
                filter_dataframe_op_peildatum, datetime.date(2024, 1, 1)
            )

            filtered_df = df[
                ((df["BouwjaarMin"] <= eenheid.bouwjaar) | df["BouwjaarMin"].isnull())
                & ((df["BouwjaarMax"] >= eenheid.bouwjaar) | df["BouwjaarMax"].isnull())
            ]
            if dataframe_heeft_een_rij(filtered_df):
                punten = filtered_df["Eengezinswoning"].values[0]

                logger.debug(
                    f"Eenheid {eenheid.id} met bouwjaar {eenheid.bouwjaar} krijgt {punten} punten voor stelselgroep {Woningwaarderingstelselgroep.energieprestatie.naam}."
                )
                woningwaardering.punten = float(punten)

        woningwaardering_groep.woningwaarderingen.append(woningwaardering)
        punten_totaal = Decimal(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in (
                    woningwaardering_groep.woningwaarderingen or []
                )
                if woningwaardering.punten is not None
            )
        )

        woningwaardering_groep.punten = float(punten_totaal)
        return woningwaardering_groep

    @staticmethod
    def _krijg_energieprestatie_met_geldig_label(
        eenheid: EenhedenEenheid,
    ) -> EenhedenEnergieprestatie | None:
        """
        Returnt de eerste geldige energieprestatie met een energielabel van een eenheid.

        Args:
            eenheid (EenhedenEenheid): De eenheid met mogelijke energieprestaties.

        Returns:
            EenhedenEnergieprestatie | None: De eerste geldige energieprestatie met een energielabel en None Wanneer er geen geldige energieprestatie met label is gevonden.
        """
        if eenheid.energieprestaties is not None:
            for energieprestatie in eenheid.energieprestaties:
                if (
                    energieprestatie.registratiedatum is not None
                    and (
                        (
                            energieprestatie.begindatum is not None
                            and energieprestatie.einddatum is not None
                            and energieprestatie.label is not None
                            and energieprestatie.registratiedatum is not None
                        )
                        and (
                            energieprestatie.begindatum
                            < datetime.date.today()
                            < energieprestatie.einddatum
                        )
                        or (
                            energieprestatie.label is not None
                            and energieprestatie.status is not None
                            and energieprestatie.status.code
                            == Energieprestatiestatus.definitief.code
                        )
                    )
                    and (
                        # Check of de registratie niet ouder is dan 10 jaar
                        energieprestatie.registratiedatum
                        > (
                            (datetime.datetime.now()).astimezone(
                                zoneinfo.ZoneInfo("EUROPE/AMSTERDAM")
                            )
                            - datetime.timedelta(weeks=520)
                        )
                    )
                ):
                    logger.debug("Energieprestatie met geldig label gevonden")
                    return energieprestatie

        logger.debug("Geen geldige energieprestatie met label gevonden")
        return None


if __name__ == "__main__":
    logger.enable("woningwaardering")

    energieprestatie = Energieprestatie2024()
    with open(
        "tests/data/input/zelfstandige_woonruimten/23003000050.json",
        "r+",
    ) as file:
        eenheid = EenhedenEenheid.model_validate_json(file.read())

    woningwaardering_resultaat = energieprestatie.bereken(eenheid)

    print(
        woningwaardering_resultaat.model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )

    tabel = naar_tabel(woningwaardering_resultaat)

    print(tabel)

    energieprestatie2 = Energieprestatie2024()
