# covid19.py

import streamlit as st
import altair as alt
import pandas as pd
import streamlit.components.v1 as components
from datetime import date


def app():
    st.title('😷 Covid19 - Cyprus Overview 🧼')
    st.info('This app demostrates an overview of the Covid-19 data for Cyprus 🇨🇾')

    st.text("")
    st.text("")

    with st.spinner(text='Loading Data! Please wait...'):
    	cyprus_df = load_data()

    
    st.text("")

    features = ['daily new cases', 'daily deaths', 'Hospitalised Cases', 'Cases In ICUs', 'total_daily tests performed']

    #features = ["new_cases","new_deaths","icu_patients","hosp_patients","new_tests","people_vaccinated","people_fully_vaccinated"]

    multiselection = st.multiselect("Select features:", features, default=features)

    if len(multiselection) > 0:
    	with st.beta_expander("See raw data",expanded=False):
    		st.dataframe(cyprus_df[["date"]+multiselection])

    	plot_date(cyprus_df, multiselection)

    st.subheader('Rapid test units for '+date.today().strftime('%d-%m-%Y'))

    components.iframe("https://www.google.com/maps/d/embed?mid=1AXahGyHjpt6CPhFE00_02Oo9u992VaZA",height=480,scrolling=False)



@st.cache(ttl=60*60*1)
def load_data():
	#df = pd.read_csv('https://raw.githubusercontent.com/xristofo/streamlit/main/share/data/owid-covid-data-cy.csv',error_bad_lines=False)
	df = pd.read_csv('https://www.data.gov.cy/node/4844/download',error_bad_lines=False)

	return df

def plot_date(df, selection):
	st.line_chart(df[selection],use_container_width=True)