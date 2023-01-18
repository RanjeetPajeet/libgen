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



with st.container():
    st.markdown("## Search")
    st.markdown("###")
    
    title_col, author_col = st.columns(2)
    with title_col:
        title = st.text_input("Book Title", "")
    with author_col:
        author = st.text_input("Author Name", "")
        

        
submit_button = st.button("Submit")
