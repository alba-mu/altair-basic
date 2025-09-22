import streamlit as st

page_1 = st.Page("page_1.py", title="page_1")
page_2 = st.Page("page_2.py", title="page_2")

pg = st.navigation([page_1, page_2])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()