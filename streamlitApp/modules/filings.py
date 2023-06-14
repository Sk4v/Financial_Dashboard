import streamlit as st
from dotenv import load_dotenv
import pathlib
import sys
import os
path = pathlib.Path(__file__).parent.parent
fmp_path = os.path.join(path,'fmp')
sys.path.append(fmp_path)
from financialModelingPrep import FinancialModelingPrep

load_dotenv()

class Filings():
    def __init__(self, ticker):
        self.fmp = FinancialModelingPrep(token=os.getenv('fmp'))
        self.ticker = ticker


    '''
    TODO SEC filings 
    https://site.financialmodelingprep.com/developer/docs/#SEC-Filings
    st.radio(horizontal=True) -- scegliere tra 10-K | 10-Q | 8-K | 20-F | 6-K
    Nella sezione 10-K, dare la possibilità di scaricare il xlsx
    '''

    def show_sec_filings(self):
        type = st.radio('Choose type',options=['10-K','10-Q','8-K','20-F','6-K'],horizontal=True)
        self.sec_filings(type)


    def sec_filings(self,type):
        if self.ticker == '': return
        filings = self.fmp.sec_filings(self.ticker,type)
        for fil in filings.values:
            date = fil['fillingDate'].split()[0]
            url = fil['finalLink']
            st.subheader(f'{self.ticker} {date} :red[{type}]')
            st.markdown(f'[Link]({url})')
            if type == '10-K':
                year = date.split('-')[0]
                url = f'https://financialmodelingprep.com/api/v4/financial-reports-dates?symbol={self.ticker}&year={year}&period=FY&apikey={os.getenv("fmp")}'
                st.markdown(f'[Dowload as xslx]({url})')
            st.divider()



    '''
    Sec RSS Feeds, nel main.
    '''