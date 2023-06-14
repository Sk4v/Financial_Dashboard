from modules.competitor import  Competitor
import streamlit as st
import pathlib
import sys
import os
path = pathlib.Path(__file__).parent.parent
fmp_path = os.path.join(path,'fmp')
sys.path.append(fmp_path)
from financialModelingPrep import FinancialModelingPrep
from dotenv import load_dotenv


load_dotenv()
fmp = FinancialModelingPrep(token=os.getenv('fmp'))
def check_ticker(ticker):
    try:
        profile = fmp.company_profile(ticker)
        if profile.isActivelyTrading == True:
            return True
        else:
            return False
    except Exception as e:
        return False

def main():
    st.title(':green[Competitors]'.upper())
    if 'ticker' in st.experimental_get_query_params():
        ticker = st.experimental_get_query_params()['ticker'][0]
        ticker = st.text_input(label='Ticker', placeholder='Search...', value=ticker).upper()
        if check_ticker(ticker):
            competitor = Competitor(ticker=ticker)
            competitor.show_competitors()
        else:
            st.error('TICKET NOT FOUND')
    else:
        ticker = st.text_input(label='Ticker', placeholder='Search...').upper()


main()



