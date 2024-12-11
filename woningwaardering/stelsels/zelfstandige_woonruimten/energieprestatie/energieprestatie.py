import warnings
from datetime import date, datetime
from importlib.resources import files

import pandas as pd
from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.gedeelde_logica.energieprestatie import (
    get_energieprestatievergoeding,
    monument_correctie,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
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
    Energieprestatiesoort,
    Oppervlaktesoort,
    Pandsoort,
    PandsoortReferentiedata,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)

LOOKUP_TABEL_FOLDER = (
    "stelsels/zelfstandige_woonruimten/energieprestatie/lookup_tabellen"
)


class Energieprestatie(Stelselgroep):
    lookup_mapping = {
        "overgangsrecht_0-25": pd.read_csv(
            files("woningwaardering").joinpath(
                f"{LOOKUP_TABEL_FOLDER}/overgangsrecht_0-25m2.csv"
            )
        ),
        "overgangsrecht_25-40": pd.read_csv(
            files("woningwaardering").joinpath(
                f"{LOOKUP_TABEL_FOLDER}/overgangsrecht_25-40m2.csv"
            )
        ),
        "energieprestatievergoeding": pd.read_csv(
            files("woningwaardering").joinpath(
                f"{LOOKUP_TABEL_FOLDER}/energieprestatievergoeding.csv"
            )
        ),
        "label_ei": pd.read_csv(
            files("woningwaardering").joinpath(
                f"{LOOKUP_TABEL_FOLDER}/label_en_energie-index.csv"
            )
        ),
        "bouwjaar": pd.read_csv(
            files("woningwaardering").joinpath(f"{LOOKUP_TABEL_FOLDER}/bouwjaar.csv")
        ),
    }

    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        super().__init__(
            begindatum=date(2024, 7, 1),
            einddatum=date.max,
            peildatum=peildatum,
        )
        self.stelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.energieprestatie

    def _bereken_punten_met_label(
        self,
        eenheid: EenhedenEenheid,
        energieprestatie: EenhedenEnergieprestatie,
        pandsoort: PandsoortReferentiedata,
        woningwaardering: WoningwaarderingResultatenWoningwaardering,
    ) -> WoningwaarderingResultatenWoningwaardering:
        woningwaardering.criterium = (
            WoningwaarderingResultatenWoningwaarderingCriterium()
        )
        """
        Berekent de punten voor Energieprestatie op basis van het energielabel.

        Args:
            eenheid: Eenheid
            energieprestatie: EenhedenEnergieprestatie
            pandsoort: Pandsoort
            woningwaardering: WoningwaarderingResultatenWoningwaardering

        Returns:
            WoningwaarderingResultatenWoningwaardering
        """

        if (
            not energieprestatie.soort
            or not energieprestatie.label
            or not energieprestatie.label.naam
            or not energieprestatie.registratiedatum
        ):
            return woningwaardering

        label = energieprestatie.label.naam
        woningwaardering.criterium.naam = f"{label}"
        lookup_key = "label_ei"

        if (
            energieprestatie.soort
            == Energieprestatiesoort.primair_energieverbruik_woningbouw
            and energieprestatie.registratiedatum >= datetime(2021, 1, 1).astimezone()
            and energieprestatie.registratiedatum < datetime(2024, 7, 1).astimezone()
            and self.peildatum
            < date(2025, 1, 1)  # Overgangsrecht kleine woningen < 40 m2 vervalt in 2025
        ):
            gebruiksoppervlakte_thermische_zone = next(
                (
                    float(oppervlakte.waarde)
                    for oppervlakte in eenheid.oppervlakten or []
                    if oppervlakte.soort
                    == Oppervlaktesoort.gebruiksoppervlakte_thermische_zone
                    and oppervlakte.waarde is not None
                ),
                None,
            )

            if gebruiksoppervlakte_thermische_zone is None:
                warnings.warn(
                    f"Eenheid ({eenheid.id}): voor de berekening van de energieprestatie met een nieuw energielabel dient de gebruiksoppervlakte van de thermische zone bekend te zijn",
                    UserWarning,
                )
                return woningwaardering

            woningwaardering.criterium.naam = label

            woningwaardering.aantal = gebruiksoppervlakte_thermische_zone

            if gebruiksoppervlakte_thermische_zone < 25.0:
                logger.info(
                    f"Eenheid ({eenheid.id}) heeft een gebruiksoppervlakte thermische zone van {gebruiksoppervlakte_thermische_zone:.2f}m2: wordt gewaardeerd volgens het 'Overgangsrecht kleine woningen < 25m2.'"
                )
                lookup_key = "overgangsrecht_0-25"
                woningwaardering.criterium.naam += " <25m2"

            elif 25.0 <= gebruiksoppervlakte_thermische_zone < 40.0:
                logger.info(
                    f"Eenheid ({eenheid.id}) heeft een gebruiksoppervlakte thermische zone van {gebruiksoppervlakte_thermische_zone:.2f}m2: wordt gewaardeerd volgens het 'Overgangsrecht kleine woningen ≥ 25m2 en < 40m2.'"
                )
                lookup_key = "overgangsrecht_25-40"
                woningwaardering.criterium.naam += " 25-40m2"

            else:
                logger.info(
                    f"Eenheid ({eenheid.id}) heeft een gebruiksoppervlakte thermische zone van {gebruiksoppervlakte_thermische_zone:.2f}m2: wordt gewaardeerd volgens de puntentelling van 'Oud en Nieuw' energielabel."
                )

        df = Energieprestatie.lookup_mapping[lookup_key]

        waarderings_label: str | None = label

        if (
            lookup_key == "label_ei"
            and energieprestatie.registratiedatum >= datetime(2015, 1, 1).astimezone()
            and energieprestatie.registratiedatum < datetime(2021, 1, 1).astimezone()
            and energieprestatie.soort == Energieprestatiesoort.energie_index
        ):
            if energieprestatie.waarde is not None:
                logger.info(
                    f"Eenheid ({eenheid.id}): {Woningwaarderingstelselgroep.energieprestatie.naam} wordt gewaardeerd op basis van energie-index."
                )

                energie_index = float(energieprestatie.waarde)
                filtered_df = df[
                    (df["Ondergrens (exclusief)"] < energie_index)
                    & (energie_index <= (df["Bovengrens (inclusief)"]))
                ]
                if len(filtered_df) != 1:
                    raise ValueError(
                        f"Eenheid ({eenheid.id}): lookup-table gefaald voor energie-index {energie_index}."
                    )

                waarderings_label_index = filtered_df["Label"].values[0]

                # wanneer de energie-index afwijkt van het label, geef voorkeur aan energie-index want de index is in deze tijd afgegeven
                if label != waarderings_label_index:
                    woningwaardering.criterium.naam += (
                        f" -> {waarderings_label_index} (Energie-index)"
                    )
                    waarderings_label = waarderings_label_index
                else:
                    woningwaardering.criterium.naam += " (Energie-index)"

        filtered_df = df[(df["Label"] == waarderings_label)]
        if len(filtered_df) != 1:
            raise ValueError(
                f"Eenheid ({eenheid.id}): lookup-table gefaald voor label {waarderings_label} voor {self.stelselgroep.naam}."
            )

        woningwaardering.punten = float(filtered_df[pandsoort.naam].values[0])

        return woningwaardering

    def _bereken_punten_met_bouwjaar(
        self,
        eenheid: EenhedenEenheid,
        pandsoort: PandsoortReferentiedata,
        woningwaardering: WoningwaarderingResultatenWoningwaardering,
    ) -> WoningwaarderingResultatenWoningwaardering:
        """
        Berekent de punten voor Energieprestatie op basis van het bouwjaar.

        Args:
            eenheid (EenhedenEenheid): Eenheid
            pandsoort (PandsoortReferentiedata): Pandsoort
            woningwaardering (WoningwaarderingResultatenWoningwaardering): De waardering voor Energieprestatie tot zover.

        Returns:
            WoningwaarderingResultatenWoningwaardering: De waardering met aangepaste criteriumnaam en punten.

        Raises:
            ValueError: Als er iets onverwachts fout gaat bij het gebruiken van een lookup-tabel.
        """

        logger.info(
            f"Eenheid ({eenheid.id}): punten voor stelselgroep {Woningwaarderingstelselgroep.energieprestatie.naam} worden berekend op basis van bouwjaar."
        )

        criterium_naam = f"Bouwjaar {eenheid.bouwjaar}"

        df = Energieprestatie.lookup_mapping["bouwjaar"]
        filtered_df = df[
            ((df["BouwjaarMin"] <= eenheid.bouwjaar) | df["BouwjaarMin"].isnull())
            & ((df["BouwjaarMax"] >= eenheid.bouwjaar) | df["BouwjaarMax"].isnull())
        ]
        if len(filtered_df) != 1:
            raise ValueError(
                f"Eenheid ({eenheid.id}): lookup-table gefaald voor bouwjaar {eenheid.bouwjaar} voor {self.stelselgroep.naam}."
            )

        woningwaardering.criterium = (
            WoningwaarderingResultatenWoningwaarderingCriterium(naam=criterium_naam)
        )
        woningwaardering.punten = float(filtered_df[pandsoort.naam].values[0])

        return woningwaardering

    def waardeer(
        self,
        eenheid: EenhedenEenheid,
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

        energieprestatie = utils.energieprestatie_met_geldig_label(
            self.peildatum, eenheid
        )

        if eenheid.monumenten is None:
            warnings.warn(
                f"Eenheid ({eenheid.id}): 'monumenten' is niet gespecificeerd. Indien de eenheid geen monumentstatus heeft, geef dit dan expliciet aan door een lege lijst toe te wijzen aan het 'monumenten'-attribuut.",
                UserWarning,
            )
            eenheid = utils.update_eenheid_monumenten(eenheid)

        pandsoort = (
            Pandsoort.meergezinswoning
            if any(
                pand.soort == Pandsoort.meergezinswoning
                for pand in eenheid.panden or []
            )
            else Pandsoort.eengezinswoning
            if any(
                pand.soort == Pandsoort.eengezinswoning for pand in eenheid.panden or []
            )
            else None
        )

        if pandsoort and not pandsoort.naam:
            warnings.warn(
                f"Eenheid ({eenheid.id}) heeft een geldige pandsoort, maar de naam is niet gespecificeerd. Voeg {Pandsoort.eengezinswoning.naam} of {Pandsoort.meergezinswoning.naam} toe aan de naam van het 'pandsoort'-attribuut.",
                UserWarning,
            )
            return woningwaardering_groep

        if not pandsoort:
            warnings.warn(
                f"Eenheid ({eenheid.id}) heeft geen pandsoort {Pandsoort.eengezinswoning.naam} of {Pandsoort.meergezinswoning.naam} en komt daarom niet in aanmerking voor waardering onder stelselgroep {Woningwaarderingstelselgroep.energieprestatie.naam}.",
                UserWarning,
            )
            return woningwaardering_groep

        if not (energieprestatie or eenheid.bouwjaar):
            warnings.warn(
                f"Eenheid ({eenheid.id}) heeft geen energieprestatie of bouwjaar en komt daarom niet in aanmerking voor waardering onder stelselgroep {Woningwaarderingstelselgroep.energieprestatie.naam}.",
                UserWarning,
            )
            return woningwaardering_groep

        woningwaardering = WoningwaarderingResultatenWoningwaardering()

        energieprestatievergoeding = get_energieprestatievergoeding(
            self.peildatum, eenheid
        )

        if energieprestatievergoeding:
            logger.info(f"Eenheid ({eenheid.id}): energieprestatievergoeding gevonden.")
            woningwaardering.criterium = (
                WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=f"Energieprestatievergoeding {pandsoort.naam}"
                )
            )
            woningwaardering.punten = float(
                Energieprestatie.lookup_mapping["energieprestatievergoeding"][
                    pandsoort.naam
                ].values[0]
            )

        elif energieprestatie:
            woningwaardering = self._bereken_punten_met_label(
                eenheid,
                energieprestatie,
                pandsoort,
                woningwaardering,
            )

        elif eenheid.bouwjaar and not energieprestatie:
            woningwaardering = self._bereken_punten_met_bouwjaar(
                eenheid, pandsoort, woningwaardering
            )

        woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        if monument_correctie_waardering := monument_correctie(
            eenheid, woningwaardering
        ):
            woningwaardering_groep.woningwaarderingen.append(
                monument_correctie_waardering
            )

        punten_totaal = sum(
            woningwaardering.punten
            for woningwaardering in (woningwaardering_groep.woningwaarderingen or [])
            if woningwaardering.punten is not None
        )

        woningwaardering_groep.punten = punten_totaal

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}."
        )

        return woningwaardering_groep


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=Energieprestatie(),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/generiek/input/37101000032.json")
