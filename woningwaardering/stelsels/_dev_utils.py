import warnings

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelsel import Stelsel
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


def bereken(
    instance: Stelselgroep | Stelsel,
    eenheid_input: EenhedenEenheid | str,
    strict: bool = False,
) -> WoningwaarderingResultatenWoningwaarderingResultaat:
    """
    Berekent de punten voor een stelselgroep of stelsel voor een eenheid.

    Args:
        instance (Stelselgroep | Stelsel): Het stelselgroep of stelsel object dat gebruikt wordt voor de berekening.
        eenheid_input (EenhedenEenheid | str): Het eenheid object of het pad naar het eenheid object in een json bestand.
        strict (bool, optional): Of er warnings geraised moeten worden. Defaults to False.

    Returns:
        WoningwaarderingResultatenWoningwaarderingResultaat: Het resultaat van de berekening.
    """
    logger.enable("woningwaardering")
    if not strict:
        warnings.filterwarnings("ignore", category=UserWarning)

    if isinstance(eenheid_input, str):
        with open(eenheid_input, "r+") as file:
            eenheid = EenhedenEenheid.model_validate_json(file.read())
    else:
        eenheid = eenheid_input

    if isinstance(instance, Stelselgroep):
        resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(
            groepen=[instance.bereken(eenheid)]
        )
    elif isinstance(instance, Stelsel):
        resultaat = instance.bereken(eenheid)

    print(resultaat.model_dump_json(by_alias=True, indent=2, exclude_none=True))

    tabel = utils.naar_tabel(resultaat)

    print(tabel)

    return resultaat
