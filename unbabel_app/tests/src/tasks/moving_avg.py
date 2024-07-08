import pandas as pd
import pandas.testing as pd_testing
import unittest

from unbabel_app.tasks.moving_avg import moving_average


class TestCleandata(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame(
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
        self.df.index = pd.to_datetime(self.df.index)
        self.df.index.name = "timestamp"

    def test_moving_average(self):
        df_expected = pd.DataFrame.from_records(
            [{'date': '2024-07-08 10:51:00', 'average_delivery_time': 0.0, 'average_nr_words': 0.0},
             {'date': '2024-07-08 10:52:00', 'average_delivery_time': 37.0, 'average_nr_words': 39.0},
             {'date': '2024-07-08 10:53:00', 'average_delivery_time': 57.5, 'average_nr_words': 63.5},
             {'date': '2024-07-08 10:54:00', 'average_delivery_time': 61.333333333333336, 'average_nr_words': 77.66666666666667},
             {'date': '2024-07-08 10:55:00', 'average_delivery_time': 57.25, 'average_nr_words': 90.25},
             {'date': '2024-07-08 10:56:00', 'average_delivery_time': 55.6, 'average_nr_words': 90.8},
             {'date': '2024-07-08 10:57:00', 'average_delivery_time': 58.666666666666664, 'average_nr_words': 84.0},
             {'date': '2024-07-08 10:58:00', 'average_delivery_time': 56.714285714285715, 'average_nr_words': 89.85714285714286},
             {'date': '2024-07-08 10:59:00', 'average_delivery_time': 49.75, 'average_nr_words': 95.125},
             {'date': '2024-07-08 11:00:00', 'average_delivery_time': 44.888888888888886, 'average_nr_words': 91.55555555555556},
             {'date': '2024-07-08 11:01:00', 'average_delivery_time': 44.0, 'average_nr_words': 86.4}
        ])
        df_expected = df_expected.apply(lambda x: x.to_dict(), axis=1)
        df_return = moving_average(window_size=10, nr_words=True, df_transl_resample=self.df)

        try:
            pd_testing.assert_series_equal(df_expected, df_return)
        except AssertionError as error:
            raise self.failureException(error)
