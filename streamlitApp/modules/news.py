import streamlit as st
from fmp.financialModelingPrep import FinancialModelingPrep
import os
from dotenv import load_dotenv
load_dotenv()


class News():
    def __init__(self,ticker):
        self.fmp = FinancialModelingPrep(token=os.getenv('fmp'))
        self.ticker = ticker

    def show_news(self):

        c1,c2 = st.columns(2)
        # Stock news
        with c1:

            if self.ticker:
                st.header(f':orange[{self.ticker} NEWS]')
                StockNews_List = self.fmp.stock_news(symbol=self.ticker)
            else:
                st.header(':orange[NEWS]')
                StockNews_List = self.fmp.latest_stock_news(10)

            for news in StockNews_List.values:
                st.header(f'[{news["title"]}]({news["url"]})')
                try:
                    st.image(news["image"],width=200)
                except:
                    pass
                st.write(news["text"])
                st.divider()




