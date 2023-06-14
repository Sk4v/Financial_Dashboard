from modules.transcripts import Transcripts
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

st.set_page_config(page_title='Transcripts', layout="wide")
st.title(':green[Transcripts]'.upper())
if 'ticker' in st.experimental_get_query_params():
    ticker = st.experimental_get_query_params()['ticker'][0]
    ticker = st.text_input(label='Ticker', placeholder='Search...', value=ticker).upper()
    if not check_ticker(ticker):
        st.error('TICKET NOT FOUND')
else:
    ticker = st.text_input(label='Ticker', placeholder='Search...').upper()

transcripts = Transcripts(ticker)
transcripts.show_transcripts()


