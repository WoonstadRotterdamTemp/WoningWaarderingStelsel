import warnings
from datetime import date

from loguru import logger

from woningwaardering.stelsels.criterium_id import CriteriumId
from woningwaardering.stelsels.utils import update_eenheid_monumenten
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
)
from woningwaardering.vera.referentiedata import (
    Eenheidmonument,
    Woningwaarderingstelselgroep,
    WoningwaarderingstelselgroepReferentiedata,
)


def opslag_rijksmonument(
    peildatum: date,
    eenheid: EenhedenEenheid,
    stelselgroep: WoningwaarderingstelselgroepReferentiedata,
) -> WoningwaarderingResultatenWoningwaardering | None:
    """Bepaalt de prijsopslag of puntentoeslag voor een rijksmonument.

    Voor huurovereenkomsten vanaf 1 juli 2024 geldt een prijsopslag van 35%.
    Voor eerdere huurovereenkomsten geldt:
    - 50 punten voor zelfstandige woonruimten
    - 10 punten voor onzelfstandige woonruimten

    Args:
        peildatum (date): De datum waarop de waardering wordt uitgevoerd
        eenheid (EenhedenEenheid): De te waarderen eenheid
        stelselgroep (WoningwaarderingstelselgroepReferentiedata): De stelselgroep waarvoor de prijsopslag wordt berekend

    Returns:
        WoningwaarderingResultatenWoningwaardering | None: De waardering met prijsopslag of puntentoeslag, of None als de eenheid geen rijksmonument is
    """
    if Eenheidmonument.rijksmonument in (eenheid.monumenten or []):
        datum_afsluiten_huurovereenkomst = eenheid.datum_afsluiten_huurovereenkomst
        if datum_afsluiten_huurovereenkomst is None:
            warnings.warn(
                f"Eenheid ({eenheid.id}): 'datum_afsluiten_huurovereenkomst' is niet gespecificeerd voor dit rijksmonument.",
                UserWarning,
            )
            logger.warning(
                f"Eenheid ({eenheid.id}): Voor de waardering van dit rijksmonument wordt de peildatum {peildatum} gebruikt in plaats van de datum van de afsluiting van de huurovereenkomst."
            )
            datum_afsluiten_huurovereenkomst = peildatum

        woningwaardering = WoningwaarderingResultatenWoningwaardering(
            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                naam="Rijksmonument",
                id=str(
                    CriteriumId(
                        stelselgroep=Woningwaarderingstelselgroep.prijsopslag_monumenten,
                        criterium="rijksmonument",
                    )
                ),
            ),
        )

        if datum_afsluiten_huurovereenkomst >= date(2024, 7, 1):
            logger.info(
                f"Eenheid ({eenheid.id}) is een rijksmonument en krijgt 35% opslag op de maximale huurprijs voor {stelselgroep.naam}."
            )
            woningwaardering.opslagpercentage = 0.35
        elif (
            stelselgroep
            == Woningwaarderingstelselgroep.prijsopslag_monumenten_en_nieuwbouw
        ):
            # 50 punten voor zelfstandige woonruimten
            logger.info(
                f"Eenheid ({eenheid.id}) is een rijksmonument en krijgt 50 punten voor {stelselgroep.naam}."
            )
            woningwaardering.punten = 50.0
        elif stelselgroep == Woningwaarderingstelselgroep.prijsopslag_monumenten:
            # 10 punten voor onzelfstandige woonruimten
            logger.info(
                f"Eenheid ({eenheid.id}) is een rijksmonument en krijgt 10 punten voor {stelselgroep.naam}."
            )
            woningwaardering.punten = 10.0

        return woningwaardering

    logger.debug(f"Eenheid ({eenheid.id}) behoort niet tot een rijksmonument.")
    return None


def opslag_gemeentelijk_of_provinciaal_monument(
    eenheid: EenhedenEenheid, stelselgroep: WoningwaarderingstelselgroepReferentiedata
) -> WoningwaarderingResultatenWoningwaardering | None:
    """Bepaalt de prijsopslag voor een gemeentelijk of provinciaal monument.

    Voor gemeentelijke en provinciale monumenten geldt een prijsopslag van 15%.

    Args:
        eenheid (EenhedenEenheid): De te waarderen eenheid
        stelselgroep (WoningwaarderingstelselgroepReferentiedata): De stelselgroep waarvoor de prijsopslag wordt berekend

    Returns:
        WoningwaarderingResultatenWoningwaardering | None: De waardering met prijsopslag, of None als de eenheid geen gemeentelijk of provinciaal monument is
    """
    if any(
        monument
        in (
            Eenheidmonument.gemeentelijk_monument,
            Eenheidmonument.provinciaal_monument,
        )
        for monument in eenheid.monumenten or []
    ):
        logger.info(
            f"Eenheid ({eenheid.id}) is gemeentelijk of provinciaal monument en krijgt 15% opslag op de maximale huurprijs voor {stelselgroep.naam}."
        )
        return WoningwaarderingResultatenWoningwaardering(
            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                naam="Gemeentelijk of provinciaal monument",
                id=str(
                    CriteriumId(
                        stelselgroep=Woningwaarderingstelselgroep.prijsopslag_monumenten_en_nieuwbouw,
                        criterium="gemeentelijk_of_provinciaal_monument",
                    )
                ),
            ),
            opslagpercentage=0.15,
        )
    else:
        logger.debug(
            f"Eenheid ({eenheid.id}) behoort niet tot een gemeentelijk of provinciaal monument."
        )
    return None


def opslag_beschermd_stads_of_dorpsgezicht(
    eenheid: EenhedenEenheid, stelselgroep: WoningwaarderingstelselgroepReferentiedata
) -> WoningwaarderingResultatenWoningwaardering | None:
    """Bepaalt de prijsopslag voor een rijksbeschermd stads- of dorpsgezicht.

    Een prijsopslag van 5% wordt toegekend als:
    - De woonruimte behoort tot een rijksbeschermd stads- of dorpsgezicht
    - De woonruimte is gebouwd voor 1965
    - De woonruimte is geen rijks-, gemeentelijk of provinciaal monument

    Args:
        eenheid (EenhedenEenheid): De te waarderen eenheid
        stelselgroep (WoningwaarderingstelselgroepReferentiedata): De stelselgroep waarvoor de prijsopslag wordt berekend

    Returns:
        WoningwaarderingResultatenWoningwaardering | None: De waardering met prijsopslag, of None als niet aan de voorwaarden wordt voldaan
    """
    # check of de eenheid een rijksbeschermd stads- of dorpsgezicht is
    if not any(
        monument
        in (
            Eenheidmonument.rijksbeschermd_dorpsgezicht,
            Eenheidmonument.rijksbeschermd_stadsgezicht,
        )
        for monument in eenheid.monumenten or []
    ):
        logger.debug(
            f"Eenheid ({eenheid.id}) behoort niet tot een rijksbeschermd stads- of dorpsgezicht."
        )
        return None

    logger.info(
        f"Eenheid ({eenheid.id}) behoort tot een rijksbeschermd stads- of dorpsgezicht."
    )

    # check of de eenheid geen rijks-, gemeentelijk of provinciaal monument is
    if any(
        monument
        in (
            Eenheidmonument.rijksmonument,
            Eenheidmonument.gemeentelijk_monument,
            Eenheidmonument.provinciaal_monument,
        )
        for monument in eenheid.monumenten or []
    ):
        logger.info(
            f"Eenheid ({eenheid.id}) is een rijks-, gemeentelijk of provinciaal monument. Er wordt geen opslagpercentage voor rijksbeschermd stads- of dorpsgezicht toegepast."
        )
        return None

    # check of de eenheid een bouwjaar heeft
    if eenheid.bouwjaar is None:
        warnings.warn(
            f"Eenheid ({eenheid.id}): geen bouwjaar gevonden",
            UserWarning,
        )
        return None

    # check of de eenheid gebouwd is voor 1965
    if eenheid.bouwjaar >= 1965:
        logger.info(
            f"Eenheid ({eenheid.id}) behoort tot een rijksbeschermd stads- of dorpsgezicht, maar is niet gebouwd voor 1965. Er wordt geen opslagpercentage toegepast."
        )
        return None

    logger.info(
        f"Eenheid ({eenheid.id}) behoort tot een rijksbeschermd stads- of dorpsgezicht en krijgt 5% opslag op de maximale huurprijs voor {stelselgroep.naam}."
    )
    return WoningwaarderingResultatenWoningwaardering(
        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
            naam="Rijksbeschermd stads- of dorpsgezicht",
            id=str(
                CriteriumId(
                    stelselgroep=Woningwaarderingstelselgroep.prijsopslag_monumenten_en_nieuwbouw,
                    criterium="rijksbeschermd_stads_of_dorpsgezicht",
                )
            ),
        ),
        opslagpercentage=0.05,
    )


def check_monumenten_attribuut(eenheid: EenhedenEenheid) -> None:
    """Controleert of het monumenten-attribuut correct is gespecificeerd.

    Geeft een waarschuwing als het attribuut None is en zoekt vervolgens de monumentstatus op basis van de gegevens in de eenheid.

    Args:
        eenheid (EenhedenEenheid): De te controleren eenheid
    """
    if eenheid.monumenten is None:
        warnings.warn(
            f"Eenheid ({eenheid.id}): 'monumenten' is niet gespecificeerd. Indien de eenheid geen monumentstatus heeft, geef dit dan expliciet aan door een lege lijst toe te wijzen aan het 'monumenten'-attribuut.",
            UserWarning,
        )
        update_eenheid_monumenten(eenheid)
