import polars as pl
from datetime import date
import streamlit as st
import altair as alt


df = pl.DataFrame({
    "name": [
        "Lucía Sánchez", "Javier Morales", "Carla Domínguez", "Miguel Ortega",
        "Ana Beltrán", "Sergio Martín", "Nuria Fernández", "Pablo Navarro",
        "Claudia Romero", "Diego Castro", "Marina Ruiz", "Óscar Herrera",
        "Isabel Vázquez", "Raúl Iglesias", "Elena Cabrera", "Adrián Paredes",
        "Patricia León", "Héctor Serrano", "Rosa Molina", "Alberto Blanco",
        "Laura Ramos", "Andrés Gil", "Beatriz Medina", "Tomás Peña",
        "Sara Campos"
    ],
    "dob": [
        "05/02/1990", "17/11/1990",
        "22/08/1983", "09/01/1983", "26/12/1983",
        "30/05/1995", "03/10/1995",
        "14/07/1981", "19/09/1981",
        "07/06/1972", "25/02/1972",
        "16/12/1988", "04/03/1988",
        "12/05/2004", "23/07/2004",
        "28/01/1984", "05/06/1984",
        "13/11/1968", "18/02/1968",
        "30/09/1992", "11/03/1992",
        "10/04/2000", "30/05/2000",
        "14/07/1978", "08/08/1978"
    ]
})

hoy = date.today()

df_con_edad = df.with_columns(
    (hoy.year - pl.col("dob").str.strptime(pl.Date, "%d/%m/%Y").dt.year()).alias("edad"),
)

st.header("Dataframe con edades calculadas a partir de la fecha de nacimiento")
st.write(df_con_edad)

edades = df_con_edad.select(
    pl.col("edad").unique().alias("edad"),
    pl.col("edad").unique_counts().alias("edad_counts"),
)

st.header("Dataframe con recuento de edades distintas")
st.write(edades)

chart = alt.Chart(edades).mark_bar().encode(
    x=alt.X("edad:Q"),
    y=alt.Y("edad_counts:Q"),
)
st.altair_chart(chart)