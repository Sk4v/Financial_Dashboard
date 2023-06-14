from modules.dcf import DCF
import streamlit as st
import os
from fmp.financialModelingPrep import FinancialModelingPrep
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
    st.title(':green[Discounted Cash Flow]'.upper())
    if 'ticker' in st.experimental_get_query_params():
        ticker = st.experimental_get_query_params()['ticker'][0]
        ticker = st.text_input(label='Ticker', placeholder='Search...', value=ticker).upper()
    else:
        ticker = st.text_input(label='Ticker', placeholder='Search...').upper()

    if check_ticker(ticker):
        dcf = DCF(ticker)
        dcf.show_all()

main()
