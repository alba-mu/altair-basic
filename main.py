import streamlit as st

weather = st.Page("weather.py", title="weather")
cars = st.Page("cars.py", title="cars")
airports = st.Page("airports.py", title="airports")
countries = st.Page("countries.py", title="countries")
bacteria = st.Page("bacteria.py", title="bacteria")

pg = st.navigation([weather, cars, airports, countries, bacteria])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()