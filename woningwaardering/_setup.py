import os
import sys
import time
import warnings
from decimal import BasicContext, setcontext
from types import TracebackType

from loguru import logger

# Set context for all calculations to avoid rounding errors
# See https://docs.python.org/3/library/decimal.html#rounding
setcontext(BasicContext)

default_timezone = "Europe/Amsterdam"


def setup_timezone() -> None:
    timezone = os.environ.get("TZ")

    if timezone is None:
        logger.info('Geen environment variable "TZ" gevonden')
        logger.info(f"Tijdzone wordt ingesteld op {default_timezone}")
        os.environ["TZ"] = default_timezone
        time.tzset()
    else:
        logger.debug(f'Tijdzone ingesteld via environment variable "TZ": {timezone}')


def handle_unhandled_exception(
    exception_type: type[BaseException],
    exception_value: BaseException,
    exception_traceback: TracebackType | None,
) -> None:
    """
    Deze functie zorgt ervoor dat onverwachte uitzonderingen gelogged worden
    en negeert daarbij uitzonderingen die ontstaan zijn door een KeyboardInterrupt.
    Als de uitzondering van het type `KeyboardInterrupt` is, wordt de uitvoering
    onderbroken zonder enige verdere actie.
    Een voorbeeld van een `KeyboardInterrupt` is wanneer een gebruiker op Ctrl+C drukt.
    """
    if issubclass(exception_type, KeyboardInterrupt):
        return
    logger.error(exception_value)
    sys.__excepthook__(exception_type, exception_value, exception_traceback)


def log_userwarning(message, category, filename, lineno, file=None, line=None):
    """
    Log a UserWarning message.
    """
    logger.warning(f"{UserWarning.__name__}: {message}")
    warnings._showwarning_original(message, category, filename, lineno, file, line)


def initialize() -> None:
    logger.disable("woningwaardering")
    setup_timezone()
    sys.excepthook = handle_unhandled_exception
    # warnings.simplefilter("once", UserWarning) # TODO: bepalen of dit wenselijk is
    warnings.simplefilter("error", UserWarning)
    warnings._showwarning_original = warnings.showwarning
    warnings.showwarning = log_userwarning