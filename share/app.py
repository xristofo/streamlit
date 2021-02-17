#app.py

import covid19
import streamlit as st

PAGES = {
    "Covid-19 Cyprus Overview": covid19
}

st.set_page_config(page_title="Covid19-Cyprus", page_icon="🧊", layout='centered', initial_sidebar_state='auto')
st.sidebar.title('🧭 Navigation')
selection = st.sidebar.radio("", list(PAGES.keys()))
page = PAGES[selection]
page.app()

st.sidebar.text("")
st.sidebar.text("")

st.sidebar.title("🔗 Sources")
st.sidebar.info('[Cyprus National Open Data Portal](https://www.data.gov.cy/)')

st.sidebar.title("🛈 About") 
st.sidebar.info('This web-app was created and maintained by andreas christoforou')
