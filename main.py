import polars as pl
import streamlit as st
import altair as alt

df = pl.DataFrame({
    'city': ['Seattle', 'Seattle', 'Seattle', 'New York', 'New York', 'New York', 'Chicago', 'Chicago', 'Chicago'],
    'month': ['Apr', 'Aug', 'Dec', 'Apr', 'Aug', 'Dec', 'Apr', 'Aug', 'Dec'],
    'precip': [2.68, 0.87, 5.31, 3.94, 4.13, 3.58, 3.62, 3.98, 2.56]
})


chart = alt.Chart(df).mark_point().encode(
    x='max(precip)',
    y='city'
)
st.altair_chart(chart)
