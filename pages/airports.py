import streamlit as st
import vega_datasets
import altair as alt


# Cargar y mostrar dataset de la libreria vega_datasets
@st.cache_data
def load_data():
    return vega_datasets.data.airports()


airports = load_data()
st.write("Dataset with information regarding diferent car names and their characteristics:")

st.write(airports)
st.write("\n")

line = alt.Chart(airports).mark_bar().encode(
    alt.X('state'),
    alt.Y('count(name)', axis=alt.Axis(title='Number of airports', labelAngle=0)),
)

st.write(line)

