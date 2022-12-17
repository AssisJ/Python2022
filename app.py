import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import geopandas as gpd
import numpy as np
# Icono y configuracion basico del tablero digital
#__________________________________________________________________________________________________________________________________________________
st.set_page_config(layout="wide",
                   page_icon="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png",
                   page_title="Dashboard")
#@st.cache(allow_output_mutation=True)
def load_data(filename: str):
    return pd.read_csv(filename, sep=";")
st.sidebar.image("logo.jpeg")


datos = load_data("cintia.csv")


st.markdown("# Cantidad de ID's ordenados por fecha")
def grafico_line(datos_bar):
    annios = datos_bar["datecreated"]
    datos_bar = datos_bar.set_index("datecreated")
    fig = px.line(
        datos_bar.groupby([datos_bar.index])["id"]
        .count(),
        y="id",
        text='id',
    )
    return fig
varfig = grafico_line(datos)
st.plotly_chart(
    varfig,
    use_container_width=True
)
