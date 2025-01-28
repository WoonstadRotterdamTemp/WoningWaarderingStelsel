import warnings
from functools import reduce
from operator import getitem
from typing import Any

from pydantic import (
    BaseModel,
    ValidationError,
    ValidationInfo,
    ValidatorFunctionWrapHandler,
    field_validator,
)


class _EenhedenEenheid(BaseModel):
    @field_validator("*", mode="wrap")
    @classmethod
    def warning_bij_validatiefout(
        cls, value: Any, handler: ValidatorFunctionWrapHandler, info: ValidationInfo
    ) -> Any:  # pragma: no cover
        validation_error: ValidationError | None = None

        try:
            return handler(value)
        except ValidationError as err:
            validation_error = err

        if validation_error:
            errors: list[str] = []
            # Loop door alle fouten in de ValidationError
            for error in validation_error.errors():
                # Haal het pad naar het veld op waar de fout optrad
                locs = tuple(error.get("loc", []))
                # Maak een leesbaar pad door veldnamen met punten te verbinden
                field_path = ".".join(str(loc) for loc in (info.field_name,) + locs)
                # Haal de foutmelding op, of gebruik 'Onbekende fout' als er geen melding is
                error_msg = error.get("msg", "Onbekende fout")

                readable_error = (
                    f"Validatiefout in attribuut '{field_path}'. {error_msg}"
                )
                errors.append(readable_error)

            warnings.warn(" ".join(errors), UserWarning)

            # Verwijder het veld met de fout
            for error in validation_error.errors():
                locs = tuple(error.get("loc", []))
                parent_object = reduce(getitem, locs[:-1], value)
                if isinstance(parent_object, dict):
                    del parent_object[locs[-1]]
                else:
                    delattr(parent_object, str(locs[-1]))

            # Probeer de waarde opnieuw te valideren
            return handler(value)
