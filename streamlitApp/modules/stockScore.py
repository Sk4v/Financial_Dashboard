import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from streamlitApp.fmp.financialModelingPrep import FinancialModelingPrep
load_dotenv()

class StockScore():
    def __init__(self,ticker):
        self.fmp = FinancialModelingPrep(token=os.getenv('fmp'))
        self.ticker = ticker


    def show_rating_df(self):
        # https://site.financialmodelingprep.com/developer/docs/recommendations-formula/

        rating = self.fmp.rating(self.ticker)

        data = { 'RATING': [
            rating.ratingDetailsROERecommendation,
            rating.ratingDetailsROARecommendation,
            rating.ratingDetailsDERecommendation,
            rating.ratingDetailsPERecommendation,
            rating.ratingDetailsPBRecommendation
        ]
        }
        df = pd.DataFrame(data,index=['ROE','ROA','DE','PE','PB'])

        st.dataframe(df)

    def show_score(self):
        score = self.fmp.stock_financial_scores(self.ticker)
        c1,c2,c3 = st.columns(3)
        with c1:
            st.markdown(f':orange[Altman Z Score:] {"{:10.1f}".format(score.altmanZScore)}')
            st.markdown(f':orange[Piotroski Score:] {"{:10.1f}".format(score.piotroskiScore)}')
            st.markdown(f':orange[Working Capital:] {score.workingCapital}')
        with c2:
            st.markdown(f':orange[Total Assets:] {score.totalAssets}')
            st.markdown(f':orange[Retained Earnings:] {score.retainedEarnings}')
            st.markdown(f':orange[Ebit:] {score.ebit}')
        with c3:
            st.markdown(f':orange[Total Assets:] {score.totalAssets}')
            st.markdown(f':orange[Retained Earnings:] {score.retainedEarnings}')
            st.markdown(f':orange[Ebit:] {score.ebit}')

