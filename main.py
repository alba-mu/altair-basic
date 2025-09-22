import streamlit as st

weather = st.Page("weather.py", title="weather")
cars = st.Page("cars.py", title="cars")
airports = st.Page("airports.py", title="airports")

pg = st.navigation([weather, cars, airports])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()