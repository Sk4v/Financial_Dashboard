import streamlit as st
import pandas as pd
import os
from fmp.financialModelingPrep import FinancialModelingPrep
from dotenv import load_dotenv

load_dotenv()
fmp = FinancialModelingPrep(token=os.getenv('fmp'))

def show_historical_price(ticker):
    price = fmp.historical_price_full(ticker)
    closed_value = []
    dates = []
    for value in price.historical_values:
        closed_value.append(value.close)
        dates.append(value.date)

    closed_value.reverse()
    dates.reverse()

    df = pd.DataFrame(
        {
            ticker: closed_value,
        },index=dates)

    return df


def show_historical_dcf(historical_dcf):
    tab1, tab2 = st.tabs(["Chart", "Data"])

    price = []
    dcf = []
    index = []
    for value in historical_dcf.values:
        price.append(value["price"])
        dcf.append(value["dcf"])
        index.append(value['date'])

    price.reverse()
    dcf.reverse()

    df_chart = pd.DataFrame(
        {
            'Price': price,
            'Dcf': dcf
        }, index=index.reverse())

    df_table = pd.DataFrame(
        {
            'Price': price,
            'Dcf': dcf
        }, index=index)

    tab1.bar_chart(df_chart)
    tab2.table(df_table)


