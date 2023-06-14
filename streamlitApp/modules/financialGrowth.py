import streamlit as st
import os
from dotenv import load_dotenv
from streamlitApp.fmp.financialModelingPrep import FinancialModelingPrep
import pandas as pd
load_dotenv()

class FinancialGrowth():
    def __init__(self,ticker):
        self.fmp = FinancialModelingPrep(token=os.getenv('fmp'))
        self.ticker = ticker
        self.ignore_keys = ['date','symbol','period','cik','reportedCurrency','acceptedDate','calendarYear','fillingDate']

    def show_growth(self):
        selected = st.radio('Select params', options=['Income Growth','Balance Growth','Cash Flow Growth'],horizontal=True)
        if selected == 'Income Growth':
            growth = self.fmp.income_statement(self.ticker)
        if selected == 'Balance Growth':
            growth = self.fmp.balance_sheet_statement(self.ticker)
        if selected == 'Cash Flow Growth':
            growth = self.fmp.cash_flow_statement(self.ticker)

        keys = list(dict(growth.values[0]).keys())
        options = {}
        for k in keys:
            if k not in self.ignore_keys:
                options[k] = (self.fmp.detect_name(k))

        selected = st.multiselect('Select params',options=list(options.values()))
        selected_converted = []
        data = {}
        index = []
        for o in options:
            if options[o] in selected:
                selected_converted.append(o)
                data[self.fmp.detect_name(o)] = []

        for value in growth.values:
            for k in value:
                if k in selected_converted:
                    data[self.fmp.detect_name(k)].append(value[k])
                    index.append(value['date'])

        #st.write(data)
        for x in data: data[x].reverse()
        df = pd.DataFrame(data)
        df2 = pd.DataFrame(data,index=index)

        #st.line_chart(df)
        st.dataframe(df2)

if __name__ == '__main__':
    f = FinancialGrowth('AAPL')
    f.show_growth()