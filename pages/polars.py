import polars as pl
import streamlit as st
import altair as alt
from datetime import date

df = pl.DataFrame(
    {
        "name": ["Alice Archer", "Ben Brown", "Chloe Cooper", "Daniel Donovan"],
        "birthdate": [
            date(1997, 1, 10),
            date(1985, 2, 15),
            date(1983, 3, 22),
            date(1981, 4, 30),
        ],
        "weight": [57.9, 72.5, 53.6, 83.1],  # (kg)
        "height": [1.56, 1.77, 1.65, 1.75],  # (m)
    }
)
st.header("Dataframe manipulation with POLARS")
st.write("Testing dataframe:")
st.write(df)

weight = alt.Chart(df).mark_bar().encode(
    alt.Y("weight:Q", axis=alt.Axis(title="Weight (kg)")),
    alt.X("name:N", axis=alt.Axis(title=None))
).properties( width=300, height=400 )


height = alt.Chart(df).mark_bar().encode(
    alt.Y("height:Q", axis=alt.Axis(title="Height")),
    alt.X("name:N", axis=alt.Axis(title=None)),
).properties( width=300, height=400 )

chart = weight | height

st.altair_chart(chart)

st.write("Testing dataframe manipulation with POLARS")
bmi_expr = pl.col("weight") / (pl.col("height") ** 2)

result = df.select(
    pl.col("name"),
    bmi=bmi_expr,
    avg_bmi = bmi_expr.mean(),
)
st.write("BMI STUDY")
st.write(result)

bmi = alt.Chart(result).mark_bar().encode(
    alt.Y("bmi:Q", axis=alt.Axis(title="BMI")),
    alt.X("name:N", axis=alt.Axis(title=None)),
)

bmi_mean = alt.Chart(result).mark_line().encode(
    alt.Y("avg_bmi:Q"),
    alt.X("name:N", axis=alt.Axis(title=None)),
)

chart = bmi + bmi_mean
st.write(chart)


