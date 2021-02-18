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
    st.title('⛽ Coming Soon... 📈')
    st.info('')

    col1, col2, col3 = st.beta_columns(3)

    with col1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg", use_column_width=True)

    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg", use_column_width=True)

    with col3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg", use_column_width=True)

    st.text("")
    st.text("")
    st.info('Out of columns')
