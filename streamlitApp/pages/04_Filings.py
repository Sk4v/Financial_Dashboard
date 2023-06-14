import streamlit as st
from modules.filings import Filings
import os
from fmp.financialModelingPrep import FinancialModelingPrep
from dotenv import load_dotenv

load_dotenv()
def check_ticker(ticker):
    try:
        fmp = FinancialModelingPrep(token=os.getenv('fmp'))
        profile = fmp.company_profile(ticker)
        if profile.isActivelyTrading == True:
            return True
        else:
            return False
    except Exception as e:
        return False


st.set_page_config(page_title='Filings', layout="wide")
st.title(':green[Filings]'.upper())

if 'ticker' in st.experimental_get_query_params():
    ticker = st.experimental_get_query_params()['ticker'][0]
    ticker = st.text_input(label='Ticker', placeholder='Search...', value=ticker).upper()
    if not check_ticker(ticker):
        st.error('TICKET NOT FOUND')

else:
    ticker = st.text_input(label='Ticker', placeholder='Search...').upper()

filings = Filings(ticker)
filings.show_sec_filings()
