from datetime import datetime
from zoneinfo import ZoneInfo
import pytest

from woningwaardering.stelsels.stelsel import Stelsel
from woningwaardering.stelsels.stelselgroep import Stelselgroep


@pytest.mark.parametrize(
    "peildatum, stelsel, aantal_geldige_stelselgroepen",
    [
        (
            datetime(2025, 1, 1, tzinfo=ZoneInfo("Europe/Amsterdam")).date(),
            "zelfstandig",
            2,
        )
    ],
)
def test_select_geldige_stelselgroepen(
    peildatum, stelsel, aantal_geldige_stelselgroepen
):
    geldigige_stelselgroepen = Stelsel.select_geldige_stelselgroepen(
        peildatum=peildatum, stelsel=stelsel
    )
    assert (
        len(geldigige_stelselgroepen) == aantal_geldige_stelselgroepen
    ), "Aantal geldige stelselgroepen is niet correct."
    for stelselgroep in geldigige_stelselgroepen:
        assert isinstance(
            stelselgroep, Stelselgroep
        ), f"Stelselgroep '{stelselgroep}' is geen instance van Stelselgroep"