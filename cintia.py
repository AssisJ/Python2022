import streamlit as st
import requests
import pandas as pd
import plotly.express as px
#475953 filas × 38 columnas
st.set_page_config(layout="wide",
                   page_icon="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png",
                   page_title = "My App")

@st.cache
def cargar_datos(filename: str):
    return pd.read_csv(filename)

datos = cargar_datos("user_loggedin.csv")
# Sidebar
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png")
st.sidebar.markdown("# Selectores de datos para estimador de id")
st.sidebar.markdown("---")
id = st.sidebar.slider(
    label = "id", min_value=50521214, max_value=58824449)
Potencia = st.sidebar.slider(
    label="usr_id", min_value=40, max_value=24984, value=475953
)
Clase = st.sidebar.selectbox(
    label="prog_programa", options=["INGENIERIA AMBIENTAL", "Licenciatura En Educación Infantil", "INGENIERIA MECÁNICA", "QUÍMICA","FINGENIERIA DE ALIMENTOS", "ADMINISTRACIÓN EN SALUD", "ACUICULTURA","LIC EN LITERATURA Y LENGUA CASTELLANA",
"Ingeniería de Alimentos","Matemáticas","Adminis. en Finanzas y Negocios Internac","Física","Medicina Veterinaria y Zootecnia",
"GEOGRAFÍA","INGENIERÍA DE SISTEMAS","Ingeniería Agronómica","LIC EN LENGUAS EXTRAN CON ENFA EN INGLES","Lic en Ciencias Naturales y Edu Ambienta","BACTERIOLOGÍA","ESTADÍSTICA","LICENCIATURA EN  INFORMATICA","Derecho","BIOLOGÍA"]