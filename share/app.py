#app.py

import covid19
import streamlit as st

PAGES = {
    "Covid-19 Cyprus Overview": covid19
}

st.set_page_config(page_title="Covid19-Cyprus", page_icon="🧊", layout='centered', initial_sidebar_state='auto')
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()

st.sidebar.info('andreas christoforou - 2021')
