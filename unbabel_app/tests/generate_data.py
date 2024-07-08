from datetime import datetime 
import os
import numpy as np
import pandas as pd
import uuid
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def generate_test_data():

    nb_rows = 10
    datetime_fmt = "%Y-%m-%d %H:%M:%S.%f"

    df_test = pd.DataFrame(
        {
            "timestamp": pd.date_range(datetime.today(), periods=nb_rows, freq="min"),
            "translation_id": [uuid.uuid4() for _ in range(nb_rows)],
            "source_language": np.random.choice(["en"], nb_rows),
            "target_language": np.random.choice(["fr"], nb_rows),
            "client_name": np.random.choice(["airliberty", "taxi-eats"], nb_rows),
            "event_name": np.random.choice(["translation_delivered"], nb_rows),
            "nr_words": np.random.randint(1, 150, size=nb_rows),
            "duration": np.random.randint(1, 100, size=nb_rows),
        }
    )
    df_test["timestamp"] = df_test["timestamp"].dt.strftime(datetime_fmt)

    (
        df_test
        .apply(lambda x: x.to_dict(), axis=1)
        .to_json(path_or_buf="test_input.json", orient="records", default_handler=str, lines=True)
    )


generate_test_data()