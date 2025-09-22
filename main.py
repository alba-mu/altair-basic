import streamlit as st

create_page = st.Page("weather.py", title="weather")
delete_page = st.Page("cars.py", title="cars")

pg = st.navigation([create_page, delete_page])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()