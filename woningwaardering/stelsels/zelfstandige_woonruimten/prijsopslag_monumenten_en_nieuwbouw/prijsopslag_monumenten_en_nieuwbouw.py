from datetime import date
from decimal import Decimal
from typing import Iterator

from dateutil.relativedelta import relativedelta
from loguru import logger

from woningwaardering.stelsels._dev_utils import DevelopmentContext
from woningwaardering.stelsels.criterium_id import CriteriumId
from woningwaardering.stelsels.gedeelde_logica.prijsopslag_monumenten import (
    check_monumenten_attribuut,
    opslag_beschermd_stads_of_dorpsgezicht,
    opslag_gemeentelijk_of_provinciaal_monument,
    opslag_rijksmonument,
)
from woningwaardering.stelsels.stelsel import Stelsel
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheidbericht,
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


class PrijsopslagMonumentenEnNieuwbouw(Stelselgroep):
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
        self.stelselgroep = (
            Woningwaarderingstelselgroep.prijsopslag_monumenten_en_nieuwbouw
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

        woningwaardering_groep.woningwaarderingen = list(
            woningwaardering
            for woningwaardering in self._genereer_woningwaarderingen(
                eenheid, woningwaardering_resultaat
            )
            if woningwaardering is not None
        )

        opslagpercentage = float(
            sum(
                Decimal(str(woningwaardering.opslagpercentage))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.opslagpercentage is not None
            )
        )

        woningwaardering_groep.opslagpercentage = opslagpercentage

        punten = float(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            )
        )

        if opslagpercentage > 0:
            logger.info(
                f"Eenheid ({eenheid.id}) krijgt een opslagpercentage van {opslagpercentage}% voor {self.stelselgroep.naam}."
            )
        else:
            logger.info(
                f"Eenheid ({eenheid.id}) krijgt geen opslagpercentage voor {self.stelselgroep.naam}."
            )

        woningwaardering_groep.punten = punten
        return woningwaardering_groep

    def _genereer_woningwaarderingen(
        self,
        eenheid: EenhedenEenheidbericht,
        woningwaardering_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat
        | None,
    ) -> Iterator[WoningwaarderingResultatenWoningwaardering | None]:
        check_monumenten_attribuut(eenheid)

        yield opslag_rijksmonument(self.peildatum, eenheid, self.stelselgroep)
        yield opslag_gemeentelijk_of_provinciaal_monument(eenheid, self.stelselgroep)
        yield opslag_beschermd_stads_of_dorpsgezicht(eenheid, self.stelselgroep)
        yield self._opslag_nieuwbouw(eenheid, woningwaardering_resultaat)

    def _opslag_nieuwbouw(
        self,
        eenheid: EenhedenEenheidbericht,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaardering | None:
        """Bepaalt de prijsopslag voor nieuwbouw.

        Een prijsopslag van 10% wordt toegekend als:
        - De bouwdatum voor 1-1-2028 ligt
        - De in exploitatiedatum na 1-7-2024 ligt
        - De in exploitatiedatum niet ouder is dan 20 jaar t.o.v. de peildatum
        - Het puntentotaal tussen 144 en 186 punten ligt

        Args:
            eenheid (EenhedenEenheidbericht): De te waarderen eenheid
            woningwaardering_resultaat (WoningwaarderingResultatenWoningwaarderingResultaat | None, optional):
                Bestaand waarderingsresultaat. Defaults to None.

        Returns:
            WoningwaarderingResultatenWoningwaardering | None: De waardering met prijsopslag, of None als niet aan de voorwaarden wordt voldaan
        """
        if (
            eenheid.begin_bouwdatum is not None
            and eenheid.begin_bouwdatum < date(2028, 1, 1)
            and eenheid.in_exploitatiedatum is not None
            and eenheid.in_exploitatiedatum
            > date(
                2024, 7, 1
            )  # TODO: https://github.com/woonstadrotterdam/woningwaardering/issues/105
            and eenheid.in_exploitatiedatum > self.peildatum - relativedelta(years=20)
        ):
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
                    negeer_stelselgroep=Woningwaarderingstelselgroep.prijsopslag_monumenten_en_nieuwbouw,
                )

            puntentotaal = (
                woningwaardering_resultaat is not None
                and Stelsel.bereken_puntentotaal(woningwaardering_resultaat)
                or None
            )

            if puntentotaal is not None and 144 <= puntentotaal <= 186:
                logger.info(
                    f"Eenheid ({eenheid.id}) is nieuwbouw en krijgt 10% opslag op de maximale huurprijs voor {self.stelselgroep}."
                )

                return WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam="Nieuwbouw",
                        id=str(
                            CriteriumId(
                                stelselgroep=self.stelselgroep,
                                criterium="nieuwbouw",
                            )
                        ),
                    ),
                    opslagpercentage=0.1,
                )

            else:
                logger.debug(
                    f"Eenheid ({eenheid.id}) is nieuwbouw, maar valt buiten het puntenbereik om in aanmerking te komen voor een opslagpercentage voor {self.stelselgroep.naam}."
                )
        else:
            logger.debug(f"Eenheid ({eenheid.id}) is geen nieuwbouw.")
        return None


if __name__ == "__main__":  # pragma: no cover
    with DevelopmentContext(
        instance=PrijsopslagMonumentenEnNieuwbouw(peildatum=date(2025, 1, 1)),
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    ) as context:
        context.waardeer("tests/data/generiek/input/37101000032.json")
