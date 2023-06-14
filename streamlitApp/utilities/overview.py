from modules.stockPriceChanges import StockPrice
from .charts import show_historical_price
from modules.financialStatements import FinancialStatements
from modules.majorsIndex import MajorsIndex
from modules.news import News
from modules.dcf import DCF
import streamlit as st
from dotenv import load_dotenv
import os
from fmp.financialModelingPrep import FinancialModelingPrep
load_dotenv()

class FoundamentalsData():
    def __init__(self, ticker):
        self.fmp = FinancialModelingPrep(token=os.getenv('fmp'))
        self.ticker = ticker


    def show_all(self):
        fin_overview_tab, financials_tab,news_tab = st.tabs(['OVERVIEW','FINANCIALS','NEWS'])

        st.experimental_set_query_params(ticker=[self.ticker])

        if self.check_ticker(ticker=self.ticker):
            # Overview Tab
            with fin_overview_tab:
                self.__show_profile()

            # Financials
            with financials_tab:
                statements = FinancialStatements(self.ticker)
                statements.show_all_statements()

            # News
            with news_tab:
                news = News(self.ticker)
                news.show_news()
        else:
            # Ticker not found
            st.error('TICKER NOT FOUND')
            majorIndexs = MajorsIndex()
            majorIndexs.show_indexes(filter=None)


    def __show_profile(self):
        try:
            outlook = self.fmp.company_outlook(self.ticker).json()
            #st.write(outlook)
            profile = outlook['profile']
            keyExecutives = outlook['keyExecutives']
            metrics = outlook['metrics']
            stockDividend = outlook['stockDividend']
            news = outlook['stockNews']

            col1, col2 = st.columns(2)
            with col1:
                st.title(f'{profile["companyName"]} - {profile["symbol"]} :red[{profile["price"]}$]')

                st.write(profile["exchangeShortName"])
                price_df = show_historical_price(self.ticker)
                st.line_chart(price_df)


                t1, t2, t3 = st.tabs(['CIK', 'ISIN', 'CUSIP'])
                t1.write(f':orange[CIK:] {profile["cik"]}')
                t2.write(f':orange[ISIN:] {profile["isin"]}')
                t3.write(f':orange[CUSIP:] {profile["cusip"]}')

                metrices_data = {'DATAS': {
                    'VOLUME': metrics['volume'],
                    'YEAR HIGH': metrics['yearHigh'],
                    'YEAR LOW': metrics['yearLow']
                }}

                st.table(metrices_data)

                st.subheader('Historical DCF')
                dcf = DCF(self.ticker)
                dcf.show_historical_dcf(limit=10)

            with col2:
                st.image(profile['image'],width=100)
                st.markdown(profile["description"])

                st.divider()
                st.subheader("Key Executives")
                for k in keyExecutives:
                    st.markdown(f'**:orange[{k["title"]}]**: {k["name"]}')

            with st.sidebar:
                st.title(f'{profile["symbol"]} :red[{profile["price"]}$]')
                st_price = StockPrice(self.ticker)
                st_price.show_stock_price_change_sidebar()

        except Exception as e:
           st.error(e)

    def check_ticker(self,ticker):
        try:
            profile = self.fmp.company_profile(ticker)
            if profile.isActivelyTrading == True:
                return True
            else:
                return False
        except Exception as e:
            return False