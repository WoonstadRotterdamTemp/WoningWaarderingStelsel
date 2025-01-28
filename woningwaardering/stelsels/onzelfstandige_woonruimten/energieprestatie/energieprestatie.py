import warnings
from collections import defaultdict
from datetime import date, datetime
from decimal import Decimal
from importlib.resources import files

import pandas as pd
from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.criterium_id import CriteriumId
from woningwaardering.stelsels.gedeelde_logica.energieprestatie import (
    get_energieprestatievergoeding,
    monument_correctie,
)
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.utils import classificeer_ruimte
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheidbericht,
    EenhedenEnergieprestatie,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Energieprestatiesoort,
    Meeteenheid,
    Ruimtesoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)

LOOKUP_TABEL_FOLDER = (
    "stelsels/onzelfstandige_woonruimten/energieprestatie/lookup_tabellen"
)


class Energieprestatie(Stelselgroep):
    lookup_mapping = {
        "label_ei": pd.read_csv(
            str(
                files("woningwaardering").joinpath(
                    f"{LOOKUP_TABEL_FOLDER}/label_en_energie-index.csv"
                )
            )
        ),
        "bouwjaar": pd.read_csv(
            str(
                files("woningwaardering").joinpath(
                    f"{LOOKUP_TABEL_FOLDER}/bouwjaar.csv"
                )
            )
        ),
    }

    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        self.stelsel = Woningwaarderingstelsel.onzelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.energieprestatie  # verkeerde parent, zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/151
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
                stelselgroep=self.stelselgroep,
            )
        )

        woningwaardering_groep.woningwaarderingen = []

        if not eenheid.ruimten:
            warnings.warn(f"Eenheid ({eenheid.id}): geen ruimten gevonden")
            return woningwaardering_groep

        if eenheid.monumenten is None:
            warnings.warn(
                f"Eenheid ({eenheid.id}): 'monumenten' is niet gespecificeerd. Indien de eenheid geen monumentstatus heeft, geef dit dan expliciet aan door een lege lijst toe te wijzen aan het 'monumenten'-attribuut.",
                UserWarning,
            )
            eenheid = utils.update_eenheid_monumenten(eenheid)

        oppervlakte_van_vertrekken = self._oppervlakte_vertrekken(eenheid)

        woningwaardering = WoningwaarderingResultatenWoningwaardering()

        energieprestatievergoeding = get_energieprestatievergoeding(
            self.peildatum, eenheid
        )

        energieprestatie = utils.energieprestatie_met_geldig_label(
            self.peildatum, eenheid
        )

        if energieprestatievergoeding:
            logger.info(f"Eenheid ({eenheid.id}): energieprestatievergoeding gevonden.")
            woningwaardering.criterium = (
                WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Energieprestatievergoeding",
                    id=str(
                        CriteriumId(
                            stelselgroep=self.stelselgroep,
                            criterium="energieprestatievergoeding",
                        )
                    ),
                    meeteenheid=Meeteenheid.vierkante_meter_m2,
                )
            )
            woningwaardering.aantal = float(
                utils.rond_af(oppervlakte_van_vertrekken, decimalen=2)
            )
            woningwaardering.punten = float(
                utils.rond_af(
                    Decimal("0.5") * Decimal(str(oppervlakte_van_vertrekken)),
                    decimalen=2,
                )
            )

        elif energieprestatie:
            woningwaardering = self._bereken_punten_met_label(
                eenheid,
                oppervlakte_van_vertrekken,
                energieprestatie,
                woningwaardering,
            )

        elif eenheid.bouwjaar:
            woningwaardering = self._bereken_punten_met_bouwjaar(
                eenheid, oppervlakte_van_vertrekken, woningwaardering
            )

        woningwaardering_groep.woningwaarderingen.append(woningwaardering)

        # Voor rijks-, provinciale en gemeentelijke monumenten geldt dat de waardering voor energieprestatie minimaal 0 punten is.
        if monument_correctie_waardering := monument_correctie(
            eenheid, woningwaardering
        ):
            woningwaardering_groep.woningwaarderingen.append(
                monument_correctie_waardering
            )

        punten_totaal = Decimal(
            utils.rond_af_op_kwart(
                sum(
                    Decimal(str(woningwaardering.punten))
                    for woningwaardering in (
                        woningwaardering_groep.woningwaarderingen or []
                    )
                    if woningwaardering.punten is not None
                )
            )
        )

        woningwaardering_groep.punten = float(punten_totaal)

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt in totaal {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )

        return woningwaardering_groep

    def _bereken_punten_met_label(
        self,
        eenheid: EenhedenEenheidbericht,
        oppervlakte: float,
        energieprestatie: EenhedenEnergieprestatie,
        woningwaardering: WoningwaarderingResultatenWoningwaardering,
    ) -> WoningwaarderingResultatenWoningwaardering:
        if (
            not energieprestatie.soort
            or not energieprestatie.label
            or not energieprestatie.label.code
            or not energieprestatie.registratiedatum
        ):
            return woningwaardering

        label = energieprestatie.label.code
        criterium_naam = f"{label}"
        df = Energieprestatie.lookup_mapping["label_ei"]

        waarderings_label = label

        if (
            energieprestatie.registratiedatum >= datetime(2015, 1, 1).astimezone()
            and energieprestatie.registratiedatum < datetime(2021, 1, 1).astimezone()
            and energieprestatie.soort == Energieprestatiesoort.energie_index
        ):
            if energieprestatie.waarde is not None:
                energie_index = float(energieprestatie.waarde)

                filtered_df = df[
                    (df["Ondergrens (exclusief)"] < energie_index)
                    & (energie_index <= (df["Bovengrens (inclusief)"]))
                ]
                if len(filtered_df) != 1:
                    raise ValueError(
                        f"Eenheid ({eenheid.id}): lookup-table gefaald voor energie-index {energie_index} voor {self.stelselgroep.naam}."
                    )

                waarderings_label_index = filtered_df["Label"].values[0]

                # wanneer de energie-index afwijkt van het label, geef voorkeur aan energie-index want de index is in deze tijd afgegeven
                if label != waarderings_label_index:
                    criterium_naam += f" -> {waarderings_label_index} (Energie-index)"
                    waarderings_label = waarderings_label_index
                else:
                    criterium_naam += " (Energie-index)"

        filtered_df = df[(df["Label"] == waarderings_label)]
        if len(filtered_df) != 1:
            raise ValueError(
                f"Eenheid ({eenheid.id}): lookup-table gefaald voor label {waarderings_label} voor {self.stelselgroep.naam}."
            )

        punten_per_m2 = filtered_df["PuntenPerM2"].values[0]

        woningwaardering.criterium = (
            WoningwaarderingResultatenWoningwaarderingCriterium(
                naam=criterium_naam,
                id=str(
                    CriteriumId(
                        stelselgroep=self.stelselgroep,
                        criterium="label",
                    )
                ),
                meeteenheid=Meeteenheid.vierkante_meter_m2,
            )
        )

        woningwaardering.aantal = float(utils.rond_af(oppervlakte, decimalen=2))
        woningwaardering.punten = float(
            utils.rond_af(
                Decimal(str(punten_per_m2)) * Decimal(str(oppervlakte)), decimalen=2
            )
        )

        logger.info(
            f"Eenheid ({eenheid.id}): krijgt {woningwaardering.punten} punten op basis van label {label} voor {self.stelselgroep.naam}."
        )

        return woningwaardering

    def _bereken_punten_met_bouwjaar(
        self,
        eenheid: EenhedenEenheidbericht,
        oppervlakte: float,
        woningwaardering: WoningwaarderingResultatenWoningwaardering,
    ) -> WoningwaarderingResultatenWoningwaardering:
        """
        Berekent de punten voor Energieprestatie op basis van het bouwjaar.

        Args:
            eenheid (EenhedenEenheidbericht): Eenheid
            oppervlakte (float): Oppervlakte
            woningwaardering (WoningwaarderingResultatenWoningwaardering): De waardering voor Energieprestatie tot zover.

        Returns:
            WoningwaarderingResultatenWoningwaardering: De waardering met aangepaste criteriumnaam en punten.

        Raises:
            ValueError: Als er iets onverwachts fout gaat bij het gebruiken van een lookup-tabel.
        """
        criterium_naam = f"Bouwjaar {eenheid.bouwjaar}"

        df = Energieprestatie.lookup_mapping["bouwjaar"]
        filtered_df = df[
            (df["BouwjaarMin"] <= eenheid.bouwjaar)
            & ((df["BouwjaarMax"] >= eenheid.bouwjaar) | df["BouwjaarMax"].isnull())
        ]
        if len(filtered_df) != 1:
            raise ValueError(
                f"Eenheid ({eenheid.id}): lookup-table gefaald voor bouwjaar {eenheid.bouwjaar} voor {self.stelselgroep.naam}."
            )

        punten_per_m2 = filtered_df["PuntenPerM2"].values[0]

        woningwaardering.criterium = (
            WoningwaarderingResultatenWoningwaarderingCriterium(
                naam=criterium_naam,
                id=str(
                    CriteriumId(
                        stelselgroep=self.stelselgroep,
                        criterium="bouwjaar",
                    )
                ),
                meeteenheid=Meeteenheid.vierkante_meter_m2,
            )
        )

        woningwaardering.aantal = float(utils.rond_af(oppervlakte, decimalen=2))
        woningwaardering.punten = float(
            utils.rond_af(
                Decimal(str(punten_per_m2)) * Decimal(str(oppervlakte)), decimalen=2
            )
        )

        logger.info(
            f"Eenheid ({eenheid.id}): krijgt {woningwaardering.punten} punten op basis van bouwjaar {eenheid.bouwjaar} voor {self.stelselgroep.naam}."
        )

        return woningwaardering

    def _oppervlakte_vertrekken(self, eenheid: EenhedenEenheidbericht) -> float:
        """
        Berekent de oppervlakte van de vertrekken in de eenheid.

        Args:
            eenheid (EenhedenEenheidbericht): Eenheid

        Returns:
            float: Oppervlakte van de vertrekken.
        """
        oppervlakte_gedeeld_met_counter: defaultdict[int, Decimal] = defaultdict(
            Decimal
        )

        for ruimte in eenheid.ruimten or []:
            if ruimte.oppervlakte is None:
                warnings.warn(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen oppervlakte.",
                    UserWarning,
                )
                continue

            if classificeer_ruimte(ruimte) == Ruimtesoort.vertrek:
                oppervlakte_gedeeld_met_counter[
                    ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
                ] += utils.rond_af(
                    Decimal(str(ruimte.oppervlakte)), decimalen=2
                )  # beleidsboek geeft expliciet aan dat moet worden afgerond op 2 decimalen

        return float(
            sum(
                utils.rond_af(
                    # op hele m2 afronden per categorie (aantal gedeeld met)
                    (utils.rond_af(oppervlakte, decimalen=0) / Decimal(str(aantal))),
                    decimalen=2,
                )
                for aantal, oppervlakte in oppervlakte_gedeeld_met_counter.items()
            )
        )


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=Energieprestatie(peildatum=date(2025, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/onzelfstandige_woonruimten/input/15004000185.json")
