import pandas as pd

def clean_data(df_translations: pd.DataFrame) -> pd.DataFrame:
    """Clean data following these steps:
        - keep only the most relevant columns
        - resample to have date for each minute in the period
        - aggregate data
    """
    df_resample = (
        df_translations
        [["timestamp", "duration", "nr_words"]]
        .resample("1Min", on="timestamp", label="left", closed="right")
    )
    first_minute_secs_resample = df_resample.count().index[0]
    first_minute_secs_data = df_translations.timestamp[0].floor('s')

    # Bug in pandas resampling: it wasn't resampling to obtain 0 translations on the first minute,
    # 2018-12-26 18:11:00, considering that the first datetime is 2018-12-26 18:11:08.
    # The implementation below helped to overcome the issue.
    # It checks if first minute+second in resample matches the first minute+second in data
    # and adds a row with 0 values if it doesn't.
    if first_minute_secs_resample != first_minute_secs_data:
        df_resample_agg = (
            df_translations
            [["timestamp", "duration", "nr_words"]]
            .resample("1Min", on="timestamp", label="right", closed="right")
            .agg(
                nb_translations=("duration", "count"),
                total_duration=("duration", "sum"),
                total_words=("nr_words", "sum"))
            )
        df_resample_agg.loc[first_minute_secs_resample] = 0
        df_resample_agg = df_resample_agg.sort_index()

    else:
        df_resample_agg = (
            df_resample
            .agg(
                nb_translations=("duration", "count"),
                total_duration=("duration", "sum"),
                total_words=("nr_words", "sum"))
        )

    return df_resample_agg
