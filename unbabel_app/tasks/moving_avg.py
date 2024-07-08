# check if it is >1
from pydantic import BaseModel, ValidationError
from pydantic import field_validator
import pandas as pd

import config

class WindowSize(BaseModel):
    """"BaseModel to check param window_size."""
    window_size: int

    @field_validator("window_size")
    @classmethod
    def window_size_natural_number(cls, v: int) -> int:
        if not v > 0:
            raise ValueError


def moving_average(window_size: int, nr_words: bool, df_transl_resample: pd.DataFrame) -> dict:
    """Calculate moving average delivery time and average_nr_words if nr_words is True."""
    _validate_window_size(window_size)

    ws_mnts = f"{window_size}min"

    moving_avg_delivery_time = (
        df_transl_resample.total_duration.rolling(ws_mnts).sum() /
        df_transl_resample.nb_translations.rolling(ws_mnts).sum()
    ).fillna(0)

    if nr_words:
        moving_avg_nr_words = (
            df_transl_resample.total_words.rolling(ws_mnts).sum() /
            df_transl_resample.nb_translations.rolling(ws_mnts).sum()
        ).fillna(0)

        moving_avg_delivery_time = pd.concat([moving_avg_delivery_time, moving_avg_nr_words], axis=1)

    return _prepare_output(moving_avg_delivery_time, nr_words)


def _prepare_output(moving_avg: pd.DataFrame, nr_words: bool) -> dict:
    """Transform timestamp to str and transform data to dictionary."""
    moving_avg.index = moving_avg.index.strftime('%Y-%m-%d %X')
    moving_avg = moving_avg.reset_index()

    cols_list = config.cols_output

    if nr_words:
        cols_list.extend(config.col_nr_words)

    moving_avg.columns = cols_list

    return moving_avg.apply(lambda x: x.to_dict(), axis=1)


def _validate_window_size(window_size: int) -> None:
    """Validate input_file is a path."""
    try:
        WindowSize(window_size=window_size)

    except ValidationError:
        raise ValueError(f"Given {window_size=} is not a natural number.")
