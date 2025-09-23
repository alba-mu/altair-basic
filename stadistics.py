import altair as alt
import polars as pl
import streamlit as st

df = pl.DataFrame({
    'alumne': ['Anna', 'Bernat', 'Carla', 'David'],
    'examen-1': [7, 4, 10, 6],
    'examen-2': [6, 8, 7, 9],
    'examen-3': [8, 7, 9, 8]
})

df = df.with_columns(
    pl.mean_horizontal([pl.col('examen-1'), pl.col('examen-2'), pl.col('examen-3')]).alias('mitjana')
)


chart = alt.Chart(df).mark_bar().encode(
    x="mitjana",
    y="alumne"
)

st.altair_chart(chart)