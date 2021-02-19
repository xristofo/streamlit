# covid19.py

import streamlit as st
import altair as alt
import pandas as pd
import streamlit.components.v1 as components
import datetime
from datetime import date
from bokeh.plotting import figure, output_file, show
from bokeh.palettes import Category10
import numpy as np


def app():
    st.title('😷 Covid19 - Cyprus Overview 🧼')
    st.info('This app demostrates an overview of the Covid-19 data for Cyprus')

    st.text("")
    st.text("")

    st.sidebar.text("")
    st.sidebar.text("")

    st.sidebar.title("🔗 Sources")
    st.sidebar.info('[Cyprus National Open Data Portal](https://www.data.gov.cy/)'+'\r'+'[Our World in Data](https://ourworldindata.org/)')
    

    st.sidebar.title("🛈 About") 
    st.sidebar.info('Created and maintained by:'+'\r'+'[andreas christoforou](xristofo@gmail.com)')

    with st.spinner(text='Loading Data! Please wait...'):
        cyprus_df = load_data()
        cyprus_vac_df = load_data_vac()
       
    st.text("")

    features = ['daily new cases', 'daily deaths', 'Hospitalised Cases', 'Cases In ICUs', 'total_daily tests performed']
    colors_dict = {'daily new cases':'#1f77b4','daily deaths':'#2ca02c','Hospitalised Cases':'#9467bd','Cases In ICUs':'#e377c2','total_daily tests performed':'#bcbd22'}

    #features = ["new_cases","new_deaths","icu_patients","hosp_patients","new_tests","people_vaccinated","people_fully_vaccinated"]
    col1, col2, col3, col4 = st.beta_columns(4)
    col5, col6, col7 = st.beta_columns(3)
    
    with col1:
        st.warning('Confirmed cases: '+str(int(cyprus_df['total cases'].iloc[-1])))

    with col2:
        st.success('Total tests: '+str(int(cyprus_df['total tests'].iloc[-1])))

    with col3:
        st.error('Deaths: '+str(int(cyprus_df['total deaths'].iloc[-1])))

    with col4:
        st.info('Population Fully Vaccinated: '+str('{0:.2f}'.format(int(cyprus_vac_df['people_fully_vaccinated'].iloc[-1])*100/875899))+"%")


    with col5:
        st.subheader("Dates")
        from_date = st.date_input("From Date:",datetime.date(2020, 9, 1))
        to_date = st.date_input("To Date:",datetime.date.today())
        filtered_df = cyprus_df[cyprus_df["date"].isin(pd.date_range(from_date, to_date))]

    with col6:
        st.subheader("Options")
        if st.checkbox('Logarithmic scale'):
            yaxistype="log"
        else:
            yaxistype="linear"

        if st.checkbox('5 Days Moving Average'):
            plot_df = filtered_df.rolling(5, win_type=None).mean()
        else:
            plot_df = filtered_df

    with col7:
        st.subheader("Features")
        multiselection = st.multiselect("", features, default=features)

    


    plot_df['date']=filtered_df["date"]

    if len(multiselection) > 0:
    	with st.beta_expander("Raw data",expanded=False):
    		st.dataframe(plot_df[["date"]+multiselection])

    	plot_date(plot_df, multiselection, colors_dict, yaxistype)

    st.subheader('Rapid test units for '+date.today().strftime('%d-%m-%Y'))

    components.iframe("https://covidmap.cy/",height=480,scrolling=False)



@st.cache(ttl=60*60*1,allow_output_mutation=True)
def load_data():
	#df = pd.read_csv('https://raw.githubusercontent.com/xristofo/streamlit/main/share/data/owid-covid-data-cy.csv',error_bad_lines=False)
    df = pd.read_csv('https://www.data.gov.cy/node/4844/download',error_bad_lines=False)
    df = data_cleaning(df)

    return df

@st.cache(ttl=60*60*1,allow_output_mutation=True)
def load_data_vac():
    #df = pd.read_csv('https://raw.githubusercontent.com/xristofo/streamlit/main/share/data/owid-covid-data-cy.csv',error_bad_lines=False)
    df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/Cyprus.csv',error_bad_lines=False)
    df = data_cleaning(df)

    return df

def plot_date(df, selection, colors_dict, yaxistype):
	#st.line_chart(df[selection],use_container_width=True)
    plot = figure(title='',plot_width=700, plot_height=450, x_axis_type="datetime", y_axis_type=yaxistype)

    for selected_column in selection:
        linecolor = colors_dict[selected_column]
        plot.line(df['date'], df[selected_column], legend_label=selected_column, line_width=2, alpha=0.5, color=linecolor)

    plot.legend.location = "top_left"
    st.bokeh_chart(plot, use_container_width=True)

def data_cleaning(df):
    
    for column in df:
        df[column].replace(["NaN",":"],0, inplace=True)
        df[column] = df[column].fillna(0)

    df['date']= pd.to_datetime(df['date'],exact=False,dayfirst=True)

    return df
