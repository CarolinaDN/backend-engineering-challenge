import pandas as pd
import pandas.testing as pd_testing
import unittest

from unbabel_app.tasks.cleandata import clean_data
from unbabel_app.tasks.dataload import load_data


class TestCleandata(unittest.TestCase):
    def setUp(self):
        self.df = load_data("test_input.json")

    def test_clean_data(self):
        df_return = clean_data(self.df)

        df_expected = pd.DataFrame(
            index = [
                '2024-07-08 10:51:00', '2024-07-08 10:52:00',
                '2024-07-08 10:53:00', '2024-07-08 10:54:00',
                '2024-07-08 10:55:00', '2024-07-08 10:56:00',
                '2024-07-08 10:57:00', '2024-07-08 10:58:00',
                '2024-07-08 10:59:00', '2024-07-08 11:00:00',
                '2024-07-08 11:01:00'],
            data = {
                "nb_translations": [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                "total_duration":[0, 37, 78, 69, 45, 49, 74, 45, 1, 6, 36],
                "total_words": [0, 39, 88, 106, 128, 93, 50, 125, 132, 63, 40]
            }
        )
        df_expected.index = pd.to_datetime(df_expected.index)
        df_expected.index.name = "timestamp"

        try:
            pd_testing.assert_frame_equal(df_expected, df_return)
        except AssertionError as error:
            raise self.failureException(error)
