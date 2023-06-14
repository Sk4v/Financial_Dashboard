from dotenv import load_dotenv
import os
from fmp.financialModelingPrep import FinancialModelingPrep
import pandas as pd
import streamlit as st

load_dotenv()

class DCF():
    def __init__(self, ticker):
        self.fmp = FinancialModelingPrep(token=os.getenv('fmp'))
        self.ticker = ticker
        self.ignore_keys = ['year','symbol']

    def show_all(self):
        st.subheader('Historical DCF')
        limit = st.slider('Years ago',min_value=1,max_value=50,value=10)
        self.show_historical_dcf(limit=limit)

        c1,c2 = st.columns(2)
        with c1:
            st.subheader('Discounted Cash Flow Projection including WACC')
            self.adv_dcf()
        with c2:
            st.subheader('Levered Discounted Cash Flow Projection including WACC')
            self.adv_dcf_wacc()

    def show_historical_dcf(self,limit=None):
        historical = self.fmp.historical_discounted_cash_flow(self.ticker,limit=limit)
        price = []
        dcf = []
        index = []
        for v in historical.values:
            price.append(v['price'])
            dcf.append(v['dcf'])
            index.append(v['date'])

        data = {
            'Price': price,
            'Dcf': dcf
        }
        df = pd.DataFrame(data,index=index)
        st.bar_chart(df)


    def adv_dcf(self):
        dcf = self.fmp.advanced_discounted_cash_flow(self.ticker)
        df = self.__create_df(dcf.values, self.ignore_keys)
        st.dataframe(df)
        l = ['revenue','ebitda','ebit','depreciation','total cash','receivables','inventories','payable']
        key = st.radio('Select options',options=[x.upper() for x in l],horizontal=True,)
        df_line = self.__create_line_chart_df(dcf.values,[key.lower()])
        st.line_chart(df_line)

    def adv_dcf_wacc(self):
        dcf = self.fmp.advanced_levered_discounted_cash_flow(self.ticker)
        df = self.__create_df(dcf.values, self.ignore_keys)
        st.dataframe(df)
        l = ['revenue', 'capital expenditure ', 'diluted shares outstanding ', 'costof debt ', 'tax rate ', 'after tax cost of debt ', 'total debt', 'total equity', 'total capital', 'operating cash flow']
        key = st.radio('Select options', options=[x.upper() for x in l], horizontal=True)
        df_line = self.__create_line_chart_df(dcf.values, [key.lower()])
        st.line_chart(df_line)



    def __create_df(self, statements, ignore_keys=[]):
        datas = {}
        for value in statements:
            values = []
            index = []
            for key in value:
                if key not in ignore_keys and 'Percentage' not in key:
                    index.append(self.fmp.detect_name(key))
                    values.append(value[key])
            datas[value["year"]] = values

        Keys = list(datas.keys())
        Keys.sort()
        new_dict = {key: datas[key] for key in Keys}
        df = pd.DataFrame(new_dict, index=index)
        return df

    def __create_line_chart_df(self,statements,keys=[]):
        datas = {}
        index = []
        for value in statements:
            for k in value:
                if 'Percentage' not in k and k in keys:
                    if k in datas:
                        datas[k].append(value[k])
                    else:
                        datas[k] = [value[k]]
            index.append(value['year'])
        #st.write(datas)
        df = pd.DataFrame(datas,index=index)
        return df
