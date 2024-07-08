from pydantic import BaseModel, FilePath, ValidationError
from pydantic import field_validator
import pandas as pd

class InputFile(BaseModel):
    """"BaseModel for check param input file."""
    input_file: FilePath

    @field_validator("input_file")
    @classmethod
    def path_must_end_json(cls, v: str) -> str:
        if not str(v).endswith(".json"):
            raise ValueError


def load_data(input_file: str) -> pd.DataFrame:
    """Read json file using pandas."""
    _validate_input_file(input_file)

    return pd.read_json(input_file, lines=True)


def _validate_input_file(input_file: str) -> None:
    """Validate input_file is a path."""
    try:
        InputFile(input_file=input_file)

    except ValidationError:
        raise ValueError(f"Given {input_file=} is not a json path.")
