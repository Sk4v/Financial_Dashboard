import streamlit as st
from fmp.financialModelingPrep import FinancialModelingPrep
import os
from dotenv import load_dotenv

load_dotenv()


class StockPrice():
    def __init__(self, ticker):
        self.fmp = FinancialModelingPrep(token=os.getenv('fmp'))
        self.ticker = ticker

    def show_stock_price_change_columns(self, ticker):
        priceChange = self.fmp.stock_price_change(ticker)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("1D", ' ', delta="{:10.2f} %".format(priceChange.V1D))
            st.metric("5D", ' ', delta="{:10.2f} %".format(priceChange.V5D))
            st.metric("YTD", ' ', delta="{:10.2f} %".format(priceChange.Vytd))
        with col2:
            st.metric("1M", ' ', delta="{:10.2f} %".format(priceChange.V1M))
            st.metric("3M", ' ', delta="{:10.2f} %".format(priceChange.V3M))
            st.metric("6M", ' ', delta="{:10.2f} %".format(priceChange.V6M))
        with col3:
            st.metric("1Y", ' ', delta="{:10.2f} %".format(priceChange.V1Y))
            st.metric("3Y", ' ', delta="{:10.2f} %".format(priceChange.V3Y))
            st.metric("5Y", ' ', delta="{:10.2f} %".format(priceChange.V5Y))
            # col10.metric("10Y", ' ', delta=priceChange.V10Y)
            st.metric("MAX", ' ', delta="{:10.2f} %".format(priceChange.Vmax))

    def show_stock_price_change(self, ticker):
        priceChange = self.fmp.stock_price_change(ticker)
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("1D", ' ', delta=priceChange.V1D)
        col2.metric("5D", ' ', delta=priceChange.V5D)
        col3.metric("1M", ' ', delta=priceChange.V1M)
        col4.metric("3M", ' ', delta=priceChange.V3M)
        col5.metric("6M", ' ', delta=priceChange.V6M)

        col7, col8, col9, col10, col11 = st.columns(5)
        col10.metric("YTD", ' ', delta=priceChange.Vytd)
        col7.metric("1Y", ' ', delta=priceChange.V1Y)
        col8.metric("3Y", ' ', delta=priceChange.V3Y)
        col9.metric("5Y", ' ', delta=priceChange.V5Y)
        # col10.metric("10Y", ' ', delta=priceChange.V10Y)
        col11.metric("MAX", ' ', delta=priceChange.Vmax)

    def show_stock_price_change_sidebar(self):
        price_change = self.fmp.stock_price_change(self.ticker)
        dict__ = price_change.__dict__
        for v in dict__:
            if v != 'symbol' and v != 'response' and dict__[v] is not None:
                if dict__[v] >= 0:
                    st.subheader(f'{v[1:].upper()}: :green[{dict__[v]} %]')
                else:
                    st.subheader(f'{v[1:].upper()}: :red[{dict__[v]} %]')



if __name__ == '__main__':
    s = StockPrice('AAPL')
    s.show_stock_price_change_sidebar()
