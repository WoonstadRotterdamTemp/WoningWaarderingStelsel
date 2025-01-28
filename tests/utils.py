import difflib
from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from pathlib import Path
from typing import Iterator

import pytest
from pytest import fail

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.utils import naar_tabel, normaliseer_ruimte_namen
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheidbericht,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelselgroep,
)


def get_stelselgroep_resultaten(
    resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    stelselgroep: Woningwaarderingstelselgroep,
) -> list[WoningwaarderingResultatenWoningwaarderingGroep]:
    resultaten = [
        groep
        for groep in resultaat.groepen or []
        if groep.criterium_groep.stelselgroep == stelselgroep
    ]
    assert (
        len(resultaten) < 2
    ), f"Meer dan 1 stelselgroepresultaat gevonden voor {stelselgroep.naam}: {resultaten}"
    assert (
        len(resultaten) == 1
    ), f"Geen stelselgroepresultaat gevonden voor: {stelselgroep.naam}"
    return resultaten


def assert_output_model(
    resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    verwacht_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    stelselgroep: Woningwaarderingstelselgroep | None = None,
):
    if stelselgroep:
        verwachte_groepen = get_stelselgroep_resultaten(
            verwacht_resultaat, stelselgroep
        )
        verwacht_resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(
            groepen=verwachte_groepen
        )

        groepen = get_stelselgroep_resultaten(resultaat, stelselgroep)
        resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(groepen=groepen)

    difflines = list(
        difflib.unified_diff(
            fromfile="verwacht",
            tofile="testresultaat",
            a=naar_tabel(verwacht_resultaat).get_string().split("\n"),
            b=naar_tabel(resultaat).get_string().split("\n"),
            lineterm="",
            n=3,
        )
    )

    colored_diff = "\n".join(kleur_diff(difflines, use_loguru_colors=True))

    if colored_diff != "":
        fail(reason=f"Output komt niet overeen\n{colored_diff}", pytrace=False)

    difflines_json = list(
        difflib.unified_diff(
            fromfile="verwacht",
            tofile="testresultaat",
            a=verwacht_resultaat.model_dump_json(indent=2, exclude_none=True).split(
                "\n"
            ),
            b=resultaat.model_dump_json(indent=2, exclude_none=True).split("\n"),
            lineterm="",
            n=3,
        )
    )

    colored_diff_json = "\n".join(kleur_diff(difflines_json, use_loguru_colors=True))

    if colored_diff_json != "":
        fail(
            reason=f"Json output komt niet overeen\n{colored_diff_json}", pytrace=False
        )

    assert_som_bovenliggend_criterium(resultaat)


def laad_specifiek_input_en_output_model(
    module_path: Path,
    output_json_path: Path,
) -> tuple[EenhedenEenheidbericht, WoningwaarderingResultatenWoningwaarderingResultaat]:
    file_name = output_json_path.name
    input_path = module_path / f"input/{file_name}"
    with open(input_path, "r+") as f:
        eenheid_input = EenhedenEenheidbericht.model_validate_json(f.read())

    with open(output_json_path, "r+") as f:
        eenheid_output = (
            WoningwaarderingResultatenWoningwaarderingResultaat.model_validate_json(
                f.read()
            )
        )

    return eenheid_input, eenheid_output


def kleur_diff(diffresult: list[str], use_loguru_colors: bool = True) -> Iterator[str]:
    green = "\x1b[92m"
    red = "\x1b[91m"
    reset = "\x1b[0m"

    return (
        (green + diff + reset)
        if diff.startswith("+")
        else (red + diff + reset)
        if diff.startswith("-")
        else diff
        for diff in diffresult
    )


@dataclass
class WarningConfig:
    file: str
    peildatum: date
    warnings: dict[type[Warning], str]


def assert_stelselgroep_warnings(
    warning_config: WarningConfig, peildatum: date, stelselgroep_class: Stelselgroep
):
    """
    Generieke functie om warnings voor stelselgroepen te testen

    Args:
        warning_config (WarningConfig): WarningConfig object met waarschuwing test configuratie
        peildatum (date): peildatum
        stelselgroep_class (Stelselgroep): Class van de stelselgroep om te testen
    """
    if peildatum < warning_config.peildatum:
        pytest.skip(f"Warning is niet van toepassing op peildatum: {peildatum}")

    with open(warning_config.file, "r+") as f:
        eenheid_input = EenhedenEenheidbericht.model_validate_json(f.read())

    with pytest.warns() as records:
        stelselgroep = stelselgroep_class(peildatum=peildatum)
        stelselgroep.waardeer(eenheid_input)

        warning_message = [(r.category, str(r.message)) for r in records]
        for warning_type, warning_message in warning_config.warnings.items():
            assert any(
                [
                    warning_type == r.category and warning_message in str(r.message)
                    for r in records
                ]
            ), f"Geen {warning_type} met message '{warning_message}' geraised"


def assert_stelselgroep_output(
    input_en_output_model: tuple[
        EenhedenEenheidbericht, WoningwaarderingResultatenWoningwaarderingResultaat
    ],
    peildatum: date,
    stelselgroep_class: Stelselgroep,
):
    eenheid_input, eenheid_output = input_en_output_model
    normaliseer_ruimte_namen(eenheid_input)

    stelselgroep = stelselgroep_class(peildatum=peildatum)

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    assert isinstance(
        resultaat, WoningwaarderingResultatenWoningwaarderingResultaat
    ), "Resultaat is geen WoningwaarderingResultatenWoningwaarderingResultaat"
    resultaat.groepen = [stelselgroep.waardeer(eenheid_input)]

    assert_output_model(
        resultaat,
        eenheid_output,
        stelselgroep.stelselgroep,
    )

    assert_som_bovenliggend_criterium(resultaat)


def assert_stelselgroep_specifiek_output(
    specifieke_input_en_output_model: tuple[
        EenhedenEenheidbericht, WoningwaarderingResultatenWoningwaarderingResultaat
    ],
    peildatum: date,
    stelselgroep_class: Stelselgroep,
):
    """
    Generieke functie om specifieke output voor stelselgroepen te testen

    Args:
        specifieke_input_en_output_model (tuple[EenhedenEenheidbericht, WoningwaarderingResultatenWoningwaarderingResultaat]): Tuple van input en verwachte output
        peildatum (date): peildatum
        stelselgroep_class (Stelselgroep): Class van de stelselgroep om te testen
    """
    eenheid_input, eenheid_output = specifieke_input_en_output_model
    stelselgroep = stelselgroep_class(peildatum=peildatum)

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    resultaat.groepen = [stelselgroep.waardeer(eenheid_input)]

    assert_output_model(
        resultaat,
        eenheid_output,
        stelselgroep.stelselgroep,
    )

    assert_som_bovenliggend_criterium(resultaat)


def maak_specifieke_input_en_output_model_fixture(base_path: Path) -> pytest.fixture:
    """
    Factory functie die een pytest fixture maakt voor het laden van specifieke test cases.

    Args:
        base_path (Path): Pad naar de directory waarin de test file zich bevindt

    Returns:
        pytest.fixture: Een pytest fixture die een tuple van input en output model retourneert
    """

    @pytest.fixture(params=[str(p) for p in (base_path / "output").rglob("*.json")])
    def specifieke_input_en_output_model(request):
        current_file_path = Path(request.fspath).parent
        output_file_path = request.param
        return laad_specifiek_input_en_output_model(
            current_file_path, Path(output_file_path)
        )

    return specifieke_input_en_output_model


def assert_som_bovenliggend_criterium(
    resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
):
    """
    Controleert of de som van de punten van woningwaarderingen met een bovenliggend criterium
    overeenkomt met de punten van de woningwaardering van het bovenliggende criterium
    """
    for groep in resultaat.groepen or []:
        # Dictionaries voor punten van bovenliggende en onderliggende criteria
        punten_bovenliggend: dict[str, Decimal] = {}
        punten_onderliggend: dict[str, Decimal] = {}

        for waardering in groep.woningwaarderingen or []:
            # Sla waarderingen zonder punten over
            if waardering.punten is None:
                continue

            # Als er een bovenliggend criterium is, tel de punten op bij onderliggende punten
            if waardering.criterium and waardering.criterium.bovenliggende_criterium:
                bovenliggend_id = waardering.criterium.bovenliggende_criterium.id
                if bovenliggend_id is None:
                    continue

                punten_onderliggend[bovenliggend_id] = punten_onderliggend.get(
                    bovenliggend_id, Decimal("0")
                ) + Decimal(str(waardering.punten))

            # Als dit een bovenliggend criterium is, sla de punten op
            if (
                waardering.criterium
                and waardering.criterium.id
                and any(
                    woningwaardering.criterium
                    and woningwaardering.criterium.bovenliggende_criterium
                    and woningwaardering.criterium.bovenliggende_criterium.id
                    == waardering.criterium.id
                    for woningwaardering in groep.woningwaarderingen or []
                )
            ):
                punten_bovenliggend[waardering.criterium.id] = Decimal(
                    str(waardering.punten)
                )

        # Vergelijk de sommen voor elk bovenliggend criterium
        for bovenliggend_id, verwachte_punten in punten_bovenliggend.items():
            if bovenliggend_id in punten_onderliggend:
                assert (
                    punten_onderliggend[bovenliggend_id] == verwachte_punten
                    or utils.rond_af_op_kwart(punten_onderliggend[bovenliggend_id])
                    == verwachte_punten
                ), (
                    f"Punten komen niet overeen voor {bovenliggend_id} "
                    f"in groep {groep.criterium_groep and groep.criterium_groep.stelselgroep and groep.criterium_groep.stelselgroep.naam}: "
                    f"Som van onderliggende punten ({punten_onderliggend[bovenliggend_id]}) "
                    f"!= Punten bovenliggend criterium ({verwachte_punten})"
                )
