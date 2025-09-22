import polars as pl
import streamlit as st
import altair as alt

df = pl.DataFrame({
    'city': ['Seattle', 'Seattle', 'Seattle', 'New York', 'New York', 'New York', 'Chicago', 'Chicago', 'Chicago'],
    'month': ['Apr', 'Aug', 'Dec', 'Apr', 'Aug', 'Dec', 'Apr', 'Aug', 'Dec'],
    'precip': [2.68, 0.87, 5.31, 3.94, 4.13, 3.58, 3.62, 3.98, 2.56]
})

st.write(df)

chart = alt.Chart(df).mark_bar().encode(
    x='average(precip)',
    y='city'
)
st.altair_chart(chart)

import streamlit as st
import vega_datasets

@st.cache_data
def load_data():
    return vega_datasets.data.cars()

cars = load_data()
st.write(cars)

chart = alt.Chart(cars).mark_line().encode(
    alt.X('Year'),
    alt.Y('average(Miles_per_Gallon)')
)

st.altair_chart(chart)

line = alt.Chart(cars).mark_line().encode(
    alt.X('Year'),
    alt.Y('average(Miles_per_Gallon)')
)

point = alt.Chart(cars).mark_circle().encode(
    alt.X('Year'),
    alt.Y('average(Miles_per_Gallon)')
)

chart = line + point
st.altair_chart(chart)


mpg = alt.Chart(cars).mark_line(point=True).encode(
    alt.X('Year'),
    alt.Y('average(Miles_per_Gallon)')
)

hp = alt.Chart(cars).mark_line(point=True).encode(
    alt.X('Year'),
    alt.Y('average(Horsepower)')
)

chart = mpg | hp

st.altair_chart(chart)

chart = alt.Chart(cars).mark_point().encode(
    x='Weight_in_lbs',
    y='Miles_per_Gallon',
    color='Origin',
    tooltip=['Name', 'Origin'] # show Name and Origin in a tooltip
).interactive()

st.altair_chart(chart)
