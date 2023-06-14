import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
import pathlib
import sys
import os
path = pathlib.Path(__file__).parent.parent
fmp_path = os.path.join(path,'fmp')
sys.path.append(fmp_path)
from financialModelingPrep import FinancialModelingPrep



load_dotenv()
class Competitor():
    def __init__(self, ticker):
        self.fmp = FinancialModelingPrep(token=os.getenv('fmp'))
        self.ticker = ticker
        self.profile = None

    def show_competitors(self):
        competitors = self.fmp.stock_peers(self.ticker)
        competitors.peersList.append(self.ticker)
        selected_competitors = st.multiselect('Compare with competitor',options=competitors.peersList,default=self.ticker)

        data = {}
        ratio_data = {}
        balance_data = {}
        income_data = {}
        cash_data = {}

        for ticker in selected_competitors:
            # Historical Price
            price = self.fmp.historical_price_full(ticker)
            closed_value = []
            index = []
            for value in price.historical_values:
                closed_value.append(value.close)
                index.append(value.date)
            #closed_value.reverse()
            data[ticker] = closed_value

            # Ratios
            ratios = self.fmp.company_ratios(ticker,limit=1)
            ratio_data[ticker],ratios_index = self.create_data(ratios.values)
            # Balance
            balance = self.fmp.balance_sheet_statement(ticker,limit=1)
            balance_data[ticker],balance_index = self.create_data(balance.values)
            # Income
            income = self.fmp.income_statement(ticker,limit=1)
            income_data[ticker], income_index = self.create_data(income.values)
            # Cash Flow
            cash = self.fmp.cash_flow_statement(ticker,limit=1)
            cash_data[ticker], cash_index = self.create_data(cash.values)

        # Price Chart
        try:
        #st.write(data)
            chart_data = pd.DataFrame(data,index=index)
            st.line_chart(data=chart_data)
        except:
            sizes = []
            for t in data:
                sizes.append(len(data[t]))

            min_size = min(sizes)

            d = {}
            for k in data:
                v = data[k]
                d[k] = v[:min_size]

            chart_data = pd.DataFrame(d,index=index)
            st.line_chart(data=chart_data)
            pass

        st.subheader(':orange[Financial Ratios]')
        self.show_datas(ratio_data,ratios_index)

        st.subheader(':orange[Income Statements]')
        self.show_datas(income_data,income_index)

        st.subheader(':orange[Balance Statements]')
        self.show_datas(balance_data,balance_index)

        st.subheader(':orange[Cash Flow Statements]')
        self.show_datas(cash_data, cash_index)

    def create_data(self,fmp_values):
        '''
        Dalla lista di oggetti forniti in input il seguente metodo genera le liste
        degli elementi necessari per creare un dataframe
        '''
        values = []
        index = []
        for obj in fmp_values:
            for value in obj:
                #print(value)
                index.append(self.fmp.detect_name(value))
                values.append(obj[value])


        return values,index


    def show_datas(self,data,index):
        # Il seguente metodo genera la tabella visibile a front con il button per scaricare i dati
        df = pd.DataFrame(data, index=index)
        st.dataframe(df)

        csv = df.to_csv().encode('utf-8')

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='RatiosTTM.csv',
            mime='text/csv',
        )
