from datetime import date
from pathlib import Path

import pytest

from woningwaardering.vera.bvg.generated import (
    EenhedenEenheidbericht,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "tests/data"


@pytest.fixture()
def peildatum():
    return date(2025, 1, 1)


@pytest.fixture(
    params=[
        str(p) for p in (DATA_DIR / "zelfstandige_woonruimten/input").glob("*.json")
    ]
)
def zelfstandige_woonruimten_inputmodel(request):
    file_path = request.param
    with open(file_path, "r+") as f:
        eenheid = EenhedenEenheidbericht.model_validate_json(f.read())
    return eenheid


@pytest.fixture(
    params=[
        str(p)
        for p in (DATA_DIR / "zelfstandige_woonruimten/output").rglob("*.json")
        if ".unverified" not in str(p)
    ]
)
def zelfstandige_woonruimten_input_en_outputmodel(
    request,
) -> tuple[EenhedenEenheidbericht, WoningwaarderingResultatenWoningwaarderingResultaat]:
    output_file_path = request.param
    file_name = Path(output_file_path).name
    input_file_path = DATA_DIR / "zelfstandige_woonruimten/input" / file_name

    # get input model
    with open(input_file_path, "r+") as f:
        eenheid_input = EenhedenEenheidbericht.model_validate_json(f.read())

    # get output model
    with open(output_file_path, "r+") as f:
        eenheid_output = (
            WoningwaarderingResultatenWoningwaarderingResultaat.model_validate_json(
                f.read()
            )
        )

    return eenheid_input, eenheid_output


@pytest.fixture(
    params=[
        str(p) for p in (DATA_DIR / "onzelfstandige_woonruimten/input").glob("*.json")
    ]
)
def onzelfstandige_woonruimten_inputmodel(request):
    file_path = request.param
    with open(file_path, "r+") as f:
        eenheid = EenhedenEenheidbericht.model_validate_json(f.read())
    return eenheid


@pytest.fixture(
    params=[
        str(p)
        for p in (DATA_DIR / "onzelfstandige_woonruimten/output").rglob("*.json")
        if ".unverified" not in str(p)
    ]
)
def onzelfstandige_woonruimten_input_en_outputmodel(
    request,
) -> tuple[EenhedenEenheidbericht, WoningwaarderingResultatenWoningwaarderingResultaat]:
    output_file_path = request.param
    file_name = Path(output_file_path).name
    input_file_path = DATA_DIR / "onzelfstandige_woonruimten/input" / file_name

    # get input model
    with open(input_file_path, "r+") as f:
        eenheid_input = EenhedenEenheidbericht.model_validate_json(f.read())

    # get output model
    with open(output_file_path, "r+") as f:
        eenheid_output = (
            WoningwaarderingResultatenWoningwaarderingResultaat.model_validate_json(
                f.read()
            )
        )

    return eenheid_input, eenheid_output


@pytest.fixture()
def woningwaardering_resultaat():
    return WoningwaarderingResultatenWoningwaarderingResultaat()


def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo):
    # Controleer of de test een exception heeft gegeven
    if call.excinfo is not None:
        # Controleer of de exception een NotImplementedError is
        if call.excinfo.type == NotImplementedError:
            # Maak een aangepast rapport om de test over te slaan
            rep = pytest.TestReport.from_item_and_call(item, call)
            rep.outcome = "skipped"
            rep.longrepr = call.excinfo
            return rep
