import pandas as pd

from const import *


def pre_process_data(df):

    df["datetime"] = pd.to_datetime(df["timestamp"], unit="ns") - pd.Timedelta(
        "03:00:00"
    )

    return df
