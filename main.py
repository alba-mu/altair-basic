import streamlit as st

weather = st.Page("pages/weather.py", title="weather")
cars = st.Page("pages/cars.py", title="cars")
airports = st.Page("pages/airports.py", title="airports")
countries = st.Page("pages/countries.py", title="countries")
bacteria = st.Page("pages/bacteria.py", title="bacteria")
stadistics = st.Page("pages/stadistics.py", title="stadistics")
polars = st.Page("pages/polars.py", title="polars")
edades = st.Page("pages/edades.py", title="edades")
conversor = st.Page("pages/conversor_moneda.py", title="conversor de moneda")

pg = st.navigation([weather, cars, airports, countries, bacteria, stadistics, polars, edades, conversor])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()