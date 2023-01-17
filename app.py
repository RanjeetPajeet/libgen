"""
app.py
======

Main file.
"""

from api import *
import streamlit as st


st.set_page_config(
    layout     = "centered",
#     page_icon  = ":moneybag:",
    page_title = "Libgen",
)

st.title("Libgen library")
st.markdown("---")
