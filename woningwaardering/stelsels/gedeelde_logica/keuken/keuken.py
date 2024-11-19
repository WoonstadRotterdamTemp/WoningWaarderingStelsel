import warnings
from collections import Counter
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels.utils import (
    gedeeld_met_onzelfstandige_woonruimten,
    rond_af,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
)
from woningwaardering.vera.referentiedata.bouwkundigelementdetailsoort import (
    Bouwkundigelementdetailsoort,
)
from woningwaardering.vera.referentiedata.meeteenheid import Meeteenheid
from woningwaardering.vera.referentiedata.ruimtedetailsoort import Ruimtedetailsoort
from woningwaardering.vera.referentiedata.voorzieningsoort import Voorzieningsoort
from woningwaardering.vera.referentiedata.woningwaarderingstelsel import (
    Woningwaarderingstelsel,
)
from woningwaardering.vera.referentiedata.woningwaarderingstelselgroep import (
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.utils import get_bouwkundige_elementen


def waardeer_ruimte(
    ruimte: EenhedenRuimte,
    stelsel: Woningwaarderingstelsel,
) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
    if not _is_keuken(ruimte):
        logger.debug(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt niet mee voor {Woningwaarderingstelselgroep.keuken.naam}"
        )
        return

    yield from _waardeer_aanrecht(ruimte, stelsel)

    yield from _waardeer_extra_voorzieningen(ruimte)


def _is_keuken(ruimte: EenhedenRuimte) -> bool:
    """
    Controleert of de ruimte een keuken is op basis van het aanrecht.

    Args:
        ruimte (EenhedenRuimte): De ruimte om te controleren.

    Returns:
        bool: True als de ruimte een keuken is, anders False.
    """
    aanrecht_aantal = len(
        [
            aanrecht
            for aanrecht in get_bouwkundige_elementen(
                ruimte, Bouwkundigelementdetailsoort.aanrecht
            )
            if aanrecht.lengte and aanrecht.lengte >= 1000
        ]
    )

    if not ruimte.detail_soort:
        warnings.warn(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen detailsoort",
            UserWarning,
        )
        return False

    if not ruimte.detail_soort.code:
        warnings.warn(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen detailsoort.code",
            UserWarning,
        )
        return False

    if ruimte.detail_soort.code in [
        Ruimtedetailsoort.keuken.code,
        Ruimtedetailsoort.woonkamer_en_of_keuken.code,
    ]:
        if aanrecht_aantal == 0:
            warnings.warn(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) is een keuken, maar heeft geen aanrecht (of geen aanrecht met een lengte >=1000mm) en mag daardoor niet gewaardeerd worden voor {Woningwaarderingstelselgroep.keuken.naam}.",
                UserWarning,
            )
            return False  # ruimte is een keuken maar heeft geen valide aanrecht en mag dus niet als keuken gewaardeerd worden
        return True  # ruimte is een keuken met een valide aanrecht
    if ruimte.detail_soort.code not in [
        Ruimtedetailsoort.woonkamer.code,
        Ruimtedetailsoort.woon_en_of_slaapkamer.code,
        Ruimtedetailsoort.slaapkamer.code,
    ]:
        return False  # ruimte is geen ruimte dat een keuken zou kunnen zijn met een aanrecht erin

    if aanrecht_aantal == 0:  # ruimte is geen keuken want heeft geen valide aanrecht
        return False

    return True  # ruimte is een impliciete keuken vanwege een valide aanrecht


def _waardeer_aanrecht(
    ruimte: EenhedenRuimte,
    stelsel: Woningwaarderingstelsel,
) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
    """
    Waardeert de aanrechten van een keuken.

    Args:
        ruimte (EenhedenRuimte): De keuken waarvan de aanrechten gewaardeerd worden.
        stelsel (Woningwaarderingstelsel): Het stelsel waarvoor de aanrechten gewaardeerd worden.

    Yields:
        WoningwaarderingResultatenWoningwaardering: De gewaardeerde aanrechten.
    """
    for element in ruimte.bouwkundige_elementen or []:
        if not element.detail_soort or not element.detail_soort.code:
            warnings.warn(
                f"Bouwkundig element {element.id} heeft geen detailsoort.code en kan daardoor niet gewaardeerd worden.",
                UserWarning,
            )
            continue
        if element.detail_soort.code == Bouwkundigelementdetailsoort.aanrecht.code:
            if not element.lengte:
                warnings.warn(
                    f"{Bouwkundigelementdetailsoort.aanrecht.naam} {element.id} heeft geen lengte en kan daardoor niet gewaardeerd worden.",
                    UserWarning,
                )
                continue
            if element.lengte < 1000:
                aanrecht_punten = 0
            elif (
                element.lengte >= 2000
                and (
                    (  # zelfstandige keuken met aanrecht boven 2000mm is 7 punten
                        not gedeeld_met_onzelfstandige_woonruimten(ruimte)
                    )
                    or (  # onzelfstandige keuken met aanrecht tussen 2000mm en 3000mm is 7 punten
                        gedeeld_met_onzelfstandige_woonruimten(ruimte)
                        and element.lengte <= 3000
                    )
                )
            ):
                aanrecht_punten = 7
            elif (
                element.lengte > 3000
                and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten
                and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten >= 8
            ):
                aanrecht_punten = 13
            elif (
                element.lengte > 3000
                and stelsel == Woningwaarderingstelsel.onzelfstandige_woonruimten
            ):
                aanrecht_punten = 10

            else:
                aanrecht_punten = 4
            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft een aanrecht van {element.lengte}mm dat meetelt voor {Woningwaarderingstelselgroep.keuken.naam}"
            )
            yield WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=f"{ruimte.naam}: Lengte {element.naam.lower() if element.naam else 'aanrecht'}",
                    meeteenheid=Meeteenheid.millimeter.value,
                ),
                punten=aanrecht_punten,
                aantal=element.lengte,
            )


def _waardeer_extra_voorzieningen(
    ruimte: EenhedenRuimte,
) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
    """
    Waardeert de extra voorzieningen van een keuken.

    Args:
        ruimte (EenhedenRuimte): De keuken waarvan de extra voorzieningen gewaardeerd worden.

    Yields:
        WoningwaarderingResultatenWoningwaardering: De gewaardeerde extra voorzieningen.
    """
    totaal_lengte_aanrechten = sum(
        element.lengte or 0
        for element in ruimte.bouwkundige_elementen or []
        if element.detail_soort
        and element.detail_soort.code == Bouwkundigelementdetailsoort.aanrecht.code
    )
    punten_per_installatie = {
        Voorzieningsoort.inbouw_afzuiginstallatie.value: 0.75,
        Voorzieningsoort.inbouw_kookplaat_inductie.value: 1.75,
        Voorzieningsoort.inbouw_kookplaat_keramisch.value: 1.0,
        Voorzieningsoort.inbouw_kookplaat_gas.value: 0.5,
        Voorzieningsoort.inbouw_koelkast.value: 1.0,
        Voorzieningsoort.inbouw_vrieskast.value: 0.75,
        Voorzieningsoort.inbouw_oven_elektrisch.value: 1.0,
        Voorzieningsoort.inbouw_oven_gas.value: 0.5,
        Voorzieningsoort.inbouw_magnetron.value: 1.0,
        Voorzieningsoort.inbouw_vaatwasmachine.value: 1.5,
        Voorzieningsoort.extra_keukenkastruimte_boven_het_minimum.value: 0.75,
        Voorzieningsoort.eenhandsmengkraan.value: 0.25,
        Voorzieningsoort.thermostatische_mengkraan.value: 0.5,
        Voorzieningsoort.kokend_waterfunctie.value: 0.5,
    }

    voorziening_counts = Counter(
        voorziening
        for voorziening in ruimte.installaties or []
        if voorziening in punten_per_installatie
    )
    punten_voor_extra_voorzieningen = sum(
        punten_per_installatie[voorziening] * count
        for voorziening, count in voorziening_counts.items()
    )

    for voorziening, count in voorziening_counts.items():
        punten = rond_af(punten_per_installatie[voorziening] * count, decimalen=2)
        logger.info(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft een {voorziening.naam} dat meetelt voor {Woningwaarderingstelselgroep.keuken.naam}"
        )
        yield (
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=f"{voorziening.naam} (in zelfde ruimte)"
                    if count > 1
                    else voorziening.naam,
                ),
                punten=punten,
                aantal=count,
            )
        )

    max_punten_voorzieningen = 7 if totaal_lengte_aanrechten >= 2000 else 4
    if punten_voor_extra_voorzieningen > max_punten_voorzieningen:
        aftrek = max_punten_voorzieningen - punten_voor_extra_voorzieningen
        logger.info(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft te veel punten voor extra keuken voorzieningen, aftrek volgt"
        )
        yield (
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=f"Max. {max_punten_voorzieningen} punten voor voorzieningen in een (open) keuken met een aanrechtlengte van {totaal_lengte_aanrechten}mm",
                ),
                punten=aftrek,
            )
        )
