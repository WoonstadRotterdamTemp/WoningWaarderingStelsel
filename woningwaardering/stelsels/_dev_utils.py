from __future__ import annotations

import sys
import warnings
from typing import Any, Optional

import loguru
from loguru import logger

from woningwaardering._logging import verkort_path
from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelsel import Stelsel
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheidbericht,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


class DevelopmentContext:
    """
    Een context manager voor het opzetten van een context voor woningwaardering.

    Deze class stelt een context in voor het uitvoeren van woningwaarderingsberekeningen,
    met aanpasbare logging en waarschuwingsinstellingen.

    Parameters:
        instance (Stelselgroep | Stelsel): Het stelsel of de stelselgroep waarvoor de berekeningen worden uitgevoerd.
        strict (bool): Bepaalt of waarschuwingen worden geraised. Standaard is False.
        log_level (str): Het logniveau voor de uitgevoerde berekeningen. Standaard is "DEBUG".

    Usage:
        with DevelopmentContext(stelsel_instance, strict=True, log_level="INFO") as context:
            resultaat = context.waardeer(eenheid)
    """

    def __init__(
        self,
        instance: Stelselgroep | Stelsel,
        strict: bool = False,
        log_level: str = "DEBUG",
    ):
        self.instance = instance
        self.strict = strict
        self.log_level = log_level

    def __enter__(self) -> "DevelopmentContext":
        self._setup_logging()
        self._setup_warnings()
        return self

    def __exit__(
        self,
        exc_type: Optional[type],
        exc_val: Optional[Exception],
        exc_tb: Optional[Any],
    ) -> None:
        pass

    def _setup_logging(self) -> None:
        def custom_dev_filter(record: loguru.Record) -> bool:
            record["extra"]["formatted_name_with_line"] = verkort_path(
                str(record["name"]), record["line"], dev=True
            )
            return True

        logger.enable("woningwaardering")
        logger.remove()
        logger.add(
            sys.stderr,
            format="<level>{level: <7}</level> | <cyan>{extra[formatted_name_with_line]}</cyan> | <level>{message}</level>",
            level=self.log_level,
            filter=custom_dev_filter,
        )

    def _setup_warnings(self) -> None:
        def warning_to_logger(
            message: Warning | str,
            category: type[Warning],
            filename: str,
            lineno: int,
            file: Optional[Any] = None,
            line: Optional[str] = None,
        ) -> None:
            logger.opt(depth=2).warning(
                f"{category.__name__}: {message}",
            )

        if not self.strict:
            warnings.filterwarnings("default", category=UserWarning)
            warnings.showwarning = warning_to_logger

    def _load_eenheid(
        self, eenheid_input: EenhedenEenheidbericht | str
    ) -> EenhedenEenheidbericht:
        if isinstance(eenheid_input, str):
            with open(eenheid_input, "r") as file:
                return EenhedenEenheidbericht.model_validate_json(file.read())
        return eenheid_input

    def waardeer(
        self, eenheid_input: EenhedenEenheidbericht | str
    ) -> WoningwaarderingResultatenWoningwaarderingResultaat:
        """
        Berekent de punten voor een stelselgroep of stelsel voor een eenheid en print het resultaat

        Args:
            eenheid_input (EenhedenEenheidbericht | str): Het eenheid object of het pad naar het eenheid object in een json bestand.

        Returns:
            WoningwaarderingResultatenWoningwaarderingResultaat: Het resultaat van de berekening.
        """
        eenheid = self._load_eenheid(eenheid_input)
        resultaat = self.instance.waardeer(eenheid)

        if isinstance(resultaat, WoningwaarderingResultatenWoningwaarderingGroep):
            resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(
                groepen=[resultaat]
            )

        self._print_resultaat(resultaat)
        return resultaat

    def _print_resultaat(
        self, resultaat: WoningwaarderingResultatenWoningwaarderingResultaat
    ) -> None:
        print(resultaat.model_dump_json(by_alias=True, indent=2, exclude_none=True))
        tabel = utils.naar_tabel(resultaat)
        print(tabel)
