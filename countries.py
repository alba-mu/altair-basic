import streamlit as st
import vega_datasets
import altair as alt

#Cargar y mostrar dataset de la libreria vega_datasets
@st.cache_data
def load_data():
    return vega_datasets.data.countries()

countries = load_data()
if st.checkbox("Show dataset"):
    st.write("Dataset with information regarding diferent countries:")
    st.write(countries)
    st.write("\n")

st.write("\n")
chart = alt.Chart(countries).mark_point().encode(
    x='average(fertility)',
    y='year',
    color='country',
    tooltip=['country', 'year']
).interactive()

st.altair_chart(chart)

# create an interval selection over an x-axis encoding
brush = alt.selection_interval(encodings=['x'])

# determine opacity based on brush
opacity = alt.condition(brush, alt.value(0.9), alt.value(0.1))

# an overview histogram of countries per year
# add the interval brush to select countries over time
overview = alt.Chart(countries).mark_bar().encode(
    alt.X('year:O', timeUnit='year', # extract year unit, treat as ordinal
      axis=alt.Axis(title=None, labelAngle=0) # no title, no label angle
    ),
    alt.Y('count(country)', title=None), # counts, no axis title
    opacity=opacity
).add_params(
    brush      # add interval brush selection to the chart
).properties(
    width=400, # set the chart width to 400 pixels
    height=50  # set the chart height to 50 pixels
)


# a detail scatterplot of fertility vs. life expentancy
# modulate point opacity based on the brush selection
detail = alt.Chart(countries).mark_point().encode(
    alt.X('fertility'),
    alt.Y('life_expect'),
    # set opacity based on brush selection
    opacity=opacity
).properties(width=400) # set chart width to match the first chart

# vertically concatenate (vconcat) charts using the '&' operator
chart = overview & detail
st.write(chart)
