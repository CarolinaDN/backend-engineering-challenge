import json
import pandas as pd

def output_data(moving_avg: pd.DataFrame) -> None:
    moving_avg.to_json(path_or_buf="moving_avg.json", orient="records")
