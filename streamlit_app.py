import plotly.express as px
import streamlit as st

from db_loader import db_load

st.set_page_config(
    page_title="Weather Graphs",
    page_icon="⛅",
    layout="wide",
    initial_sidebar_state="expanded",
)

data = db_load()

st.write(len(data))
