import streamlit as st
import vega_datasets
import altair as alt

#Cargar y mostrar dataset de la libreria vega_datasets
@st.cache_data
def load_data():
    return vega_datasets.data.cars()

cars = load_data()
st.write("Dataset with information regarding diferent car names and their characteristics:")
st.write(cars)
st.write("\n")

#Superposición de 2 graficos
st.write("Chart showing the avarage miles/galon")
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

#Concatenacion horizontal de 2 graficos
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

st.write("\n")
st.write("Box-plot") #buscar "altair box-plot" per trobar la documentació al respecte

chart = alt.Chart(cars).mark_boxplot().encode(
    alt.X('Miles_per_Gallon').scale(zero = False),
    alt.Y('Origin:N'),
    alt.Tooltip('mean(Miles_per_Gallon)')
)

st.write(chart)
st.write("\n")

