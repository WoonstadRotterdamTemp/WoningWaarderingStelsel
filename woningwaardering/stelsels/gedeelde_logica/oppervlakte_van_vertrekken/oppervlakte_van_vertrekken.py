import warnings
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels.utils import (
    classificeer_ruimte,
    rond_af,
    voeg_oppervlakte_kasten_toe_aan_ruimte,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
)
from woningwaardering.vera.referentiedata.meeteenheid import Meeteenheid
from woningwaardering.vera.referentiedata.ruimtesoort import Ruimtesoort
from woningwaardering.vera.referentiedata.woningwaarderingstelselgroep import (
    Woningwaarderingstelselgroep,
)


def waardeer(
    ruimte: EenhedenRuimte,
) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
    if not classificeer_ruimte(ruimte) == Ruimtesoort.vertrek:
        logger.debug(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt niet mee voor {Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.naam}"
        )
        return

    if not ruimte.oppervlakte:
        warnings.warn(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen oppervlakte",
            UserWarning,
        )
        return

    criterium_naam = voeg_oppervlakte_kasten_toe_aan_ruimte(ruimte)

    logger.info(
        f"Ruimte '{ruimte.naam}' ({ruimte.id}) van {ruimte.oppervlakte}m2 telt mee voor {Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.naam}"
    )

    woningwaardering = WoningwaarderingResultatenWoningwaardering()
    woningwaardering.criterium = WoningwaarderingResultatenWoningwaarderingCriterium(
        meeteenheid=Meeteenheid.vierkante_meter_m2.value,
        naam=criterium_naam,
    )
    woningwaardering.aantal = float(rond_af(ruimte.oppervlakte, decimalen=2))

    yield woningwaardering
