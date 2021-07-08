import plotly.express as px
import streamlit as st

import db_loader

st.set_page_config(
    page_title="Weather Graphs",
    page_icon="⛅",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.write(db_loader.test("db_loader test"))
