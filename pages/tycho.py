from io import BytesIO
from zipfile import ZipFile
import os
import polars as pl
import urllib3
import streamlit as st

filepath = "data/tycho-mini.csv"

if not os.path.isfile(filepath):
    load = st.text('Loading data...')
    resp = urllib3.request(
        "GET",
        "https://gitlab.com/xtec/python/data/-/raw/main/tycho-mini.zip",
    )
    zipfile = ZipFile(BytesIO(resp.data))
    zipfile.extractall(path="data")
    load.text('Loading data... done!')

#En carregar el csv canviem el tipus de dada de les variables que són dates
df = pl.scan_csv(filepath, schema_overrides={"from_date": pl.Date, "to_date": pl.Date})


st.header("PROJECT TYCHO DATASET")
st.write(df.head())
st.write(df.schema)

st.write("\n")
st.write(df.select(pl.col("event").unique(), pl.col("event").unique_counts().alias("number")))

st.write("\n")

st.write("Llista de totes les ciutats que surten al fitxer, que no es repeteixin i ordenades per ordre alfabètic")
cities = (df.filter(
    pl.col("loc_type") == "CITY"
).select(
    pl.col("loc").unique().sort().alias("city")
))

st.write(cities)
st.write("\n")

st.write("Llista el número total de morts de cada malaltia, ordenada pel número de morts.")

deaths_by_disease = (df.filter(pl.col("event") == "DEATHS").
    group_by(pl.col("disease")).
    agg(pl.col("number").sum().alias("deaths")).
    sort("deaths", descending=True))

st.write(deaths_by_disease)
st.write("\n")

st.write("Mostra el número de morts per la tuberculosi, a Nova York, l’any 1910: 32403")
st.write("\n")

#============acabaaaaar================
'''
result = not df.filter(
    (pl.col("loc") == "NEW YORK")
    (pl.col("disease") == "TUBERCULOSIS [PHTHISIS PULMONALIS]")
).
'''





