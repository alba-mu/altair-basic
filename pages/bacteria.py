import streamlit as st
import vega_datasets
import altair as alt



# Cargar y mostrar dataset de la libreria vega_datasets
@st.cache_data
def load_data():
    return vega_datasets.data.burtin()


bacteria = load_data()
st.write("Dataset with comparative of the performance of three antibiotics against 16 different bacteria:")

st.write(bacteria)
st.write("\n")

