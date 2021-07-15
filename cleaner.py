import pandas as pd

from const import *


def clean_data(df):
    df = df[df["last_updated"] < 60]

    return df
