import polars as pl
import streamlit as st
import altair as alt

df = pl.DataFrame(
    {  # As of 14th October 2024, ~3pm UTC
        "ticker": ["AAPL", "NVDA", "MSFT", "GOOG", "AMZN"],
        "company_name": ["Apple", "NVIDIA", "Microsoft", "Alphabet (Google)", "Amazon"],
        "price": [229.9, 138.93, 420.56, 166.41, 188.4],
        "day_high": [231.31, 139.6, 424.04, 167.62, 189.83],
        "day_low": [228.6, 136.3, 417.52, 164.78, 188.44],
        "year_high": [237.23, 140.76, 468.35, 193.31, 201.2],
        "year_low": [164.08, 39.23, 324.39, 121.46, 118.35],
    }
)


st.header("Conversor de moneda")

def show_usd():
    st.write(df)
    st.write("\n")

def show_eur():
    eur_usd_rate = 1.09
    df_eur = df.select(
        pl.col("ticker", "company_name"),
        (
                pl.col(
                    "price",
                    "day_high",
                    "day_low",
                    "year_high",
                    "year_low",
                ) / eur_usd_rate
        ).round(2)
    )
    st.write(df_eur)
    st.write("\n")

def show_gbp():
    gbp_usd_rate = 1.35
    df_gbp = df.select(
        pl.col("ticker", "company_name"),
        (
                pl.col(
                    "price",
                    "day_high",
                    "day_low",
                    "year_high",
                    "year_low",
                ) / gbp_usd_rate
        ).round(2)
    )
    st.write(df_gbp)
    st.write("\n")

def show_jpy():
    jpy_usd_rate = 0.0068
    df_jpy = df.select(
        pl.col("ticker", "company_name"),
        (
                pl.col(
                    "price",
                    "day_high",
                    "day_low",
                    "year_high",
                    "year_low",
                ) / jpy_usd_rate
        ).round(2)
    )
    st.write(df_jpy)
    st.write("\n")


option = st.selectbox(
    "Escoge la moneda a usar:",
    ("USD", "EUR", "GBP", "JPY"),
)
st.write("\n")

if option == "USD":
    show_usd()
elif option == "EUR":
    show_eur()
elif option == "GBP":
    show_gbp()
elif option == "JPY":
    show_jpy()
