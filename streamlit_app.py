import plotly.express as px
import streamlit as st
import pandas as pd

from pre_processer import pre_process_data
from cleaner import clean_data
from loader import load_data
from const import *

st.set_page_config(
    page_title="Weather Graphs",
    page_icon="⛅",
    layout="wide",
    initial_sidebar_state="expanded",
)

selected_parameter = st.selectbox(
    "Select a parameter",
    tuple(PARAMETERS_MAP.keys()),
)


@st.cache(ttl=300)
def load_df() -> pd.DataFrame:
    df = load_data()
    df = pre_process_data(df)
    df = clean_data(df)
    return df


df = load_df()

fig = px.scatter(
    df,
    x="datetime",
    y=PARAMETERS_MAP[selected_parameter],
    color="station_id",
)

fig.update_layout(height=750)

st.plotly_chart(fig, use_container_width=True)
