import pandas as pd
import streamlit as st
import json
import pathlib
import random


class FinancialDatas():

    @staticmethod
    def gen_formulas():
        path = pathlib.Path(__file__).parent
        file = path.joinpath('formulas.json')
        formulas = json.load(open(file))
        return formulas

    def show_formulas(self):
        formulas = self.gen_formulas()
        st.subheader('Formulas')
        searched_formula = st.text_input("Search formula")
        if searched_formula != '':
            if searched_formula in formulas:
                st.latex(f'{searched_formula}={formulas[searched_formula]}')
            else:
                st.error('Formula not found')
        #for x in formulas:
        #   st.latex(f'{x}={formulas[x]}')


    def create_statement_table(self, statements,ignore_keys=[]):
        datas = {}
        for value in statements:
            values = []
            index = []
            for key in value:
                if key not in ignore_keys:
                    index.append(self.fmp.detect_name(key))
                    values.append(value[key])
            datas[value["date"]] = values

        df = pd.DataFrame(datas, index=index)
        st.dataframe(df)
        return df

    def create_statement_growth_table(self,statements,ignore_keys=[]):
        datas = {}
        for value in statements:
            values = []
            index = []
            if value['date'] not in datas:
                for key in value:
                    if key not in ignore_keys:
                        index.append(f'{self.fmp.detect_name(key)} %')
                        if type(value[key]) != str:
                            values.append("{:10.2f} %".format(value[key]*100))
                        else: values.append(value[key])
                    datas[value["date"]] = values

        df = pd.DataFrame(datas, index=index)
        st.dataframe(df)
        return df

    def gen_button(self,df,name):
        #Button
        csv = df.to_csv().encode('utf-8')
        st.download_button(
            label=f"{name} CSV",
            data=csv,
            file_name=f'{name}.csv',
            mime='text/csv',
            key = self.random()
        )

    @staticmethod
    def random():
        randomlist = []
        for x in range(0,10):
            n = random.randint(1,200)
            randomlist.append(str(n))
        return "".join(randomlist)

