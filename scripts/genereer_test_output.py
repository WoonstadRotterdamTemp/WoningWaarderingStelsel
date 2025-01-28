import string
import sys
import warnings
from datetime import date
from importlib import import_module
from pathlib import Path

from loguru import logger
from pydantic import ValidationError

from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheidbericht,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)

logger.enable("woningwaardering")
warnings.simplefilter("default", UserWarning)
warnings.filterwarnings("ignore", category=UserWarning)

# Set logger level to INFO
logger.remove()
stdout_id = logger.add(sys.stdout, level="INFO")

PEILDATUM = date(2025, 1, 1)

DATA_DIR = Path("tests/data")

stelsels = ["zelfstandige_woonruimten", "onzelfstandige_woonruimten"]

for stelsel_naam in stelsels:
    input_file_paths = (DATA_DIR / stelsel_naam).rglob("**/input/*.json")
    output_file_paths = (DATA_DIR / stelsel_naam).rglob("**/output/*.json")
    for input_file_path in input_file_paths:
        if input_file_path.name not in [x.name for x in output_file_paths]:
            output_file_path = Path(str(input_file_path).replace("/input/", "/output/"))
            unverified_path = output_file_path.with_suffix("" + output_file_path.suffix)

            output_file_path.parent.mkdir(parents=True, exist_ok=True)

            # Get input model
            with open(input_file_path, "r+") as f:
                try:
                    eenheid_input = EenhedenEenheidbericht.model_validate_json(f.read())
                except ValidationError as e:
                    logger.error(f"Error in inputmodel van {input_file_path.name}: {e}")
                    continue

                handler_id = logger.add(
                    unverified_path.with_suffix(".log"), level="TRACE", mode="w"
                )
                # Set logger to ERROR for the stdout to avoid too much logging in the terminal during calculations
                logger.remove(stdout_id)

                if input_file_path.parent.parent.parent.name == "stelselgroepen":
                    stelselgroep_naam = input_file_path.parent.parent.name
                    stelselgroep_class = import_module(
                        f"woningwaardering.stelsels.{stelsel_naam}." + stelselgroep_naam
                    )
                    stelselgroep: Stelselgroep = getattr(
                        stelselgroep_class,
                        string.capwords(stelselgroep_naam.replace("_", " ")).replace(
                            " ", ""
                        ),
                    )(peildatum=PEILDATUM)
                    woningwaardering_resultaat = (
                        WoningwaarderingResultatenWoningwaarderingResultaat(
                            groepen=[stelselgroep.waardeer(eenheid_input)]
                        )
                    )
                else:
                    stelsel_class = import_module(
                        f"woningwaardering.stelsels.{stelsel_naam}.{stelsel_naam}"
                    )
                    stelsel = getattr(
                        stelsel_class,
                        string.capwords(stelsel_naam.replace("_", " ")).replace(
                            " ", ""
                        ),
                    )(peildatum=PEILDATUM)
                    woningwaardering_resultaat = stelsel.waardeer(eenheid_input)
                stdout_id = logger.add(sys.stdout, level="INFO")
                logger.remove(handler_id)

                # Write output model
                with open(unverified_path, "w+") as f:
                    logger.info(
                        f"Resultaat voor {input_file_path.name} is opgenomen in {unverified_path}, inclusief logs in {unverified_path.with_suffix('.log')}"
                    )
                    f.write(
                        woningwaardering_resultaat.model_dump_json(
                            by_alias=True, indent=2, exclude_none=True
                        )
                    )
                    f.write("\n")
