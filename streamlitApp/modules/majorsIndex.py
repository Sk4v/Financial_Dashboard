import streamlit as st
from dotenv import load_dotenv
import os
from fmp.financialModelingPrep import FinancialModelingPrep

load_dotenv()

class MajorsIndex:
    def __init__(self):
        self.fmp = FinancialModelingPrep(token=os.getenv('fmp'))
        self.favourites = ['NDX','SP500TR',]

    def show_indexes(self,filter=False):
        st.header("TOP INDEXES")
        st.write("\n\n")
        indexes = self.fmp.majors_indexes()
        if filter:
            indexes.values = self.filter_indexes(indexes.values)

        matrix = self.__to_matrix(indexes.values)

        for index in matrix:
            try:
                col0,col1, col2, col3 = st.columns(4)
                col0.write(index[0]['name'].upper())
                col0.metric(index[0]["symbol"].replace("^",""), index[0]["price"], index[0]["changesPercentage"])

                col1.write(index[1]['name'])
                col1.metric(index[1]["symbol"].replace("^",""), index[1]["price"], index[1]["changesPercentage"])

                col2.write(index[2]['name'])
                col2.metric(index[2]["symbol"].replace("^",""), index[2]["price"], index[2]["changesPercentage"])

                col3.write(index[3]['name'])
                col3.metric(index[3]["symbol"].replace("^",""), index[3]["price"], index[3]["changesPercentage"])

                st.divider()
            except:
                pass


    @staticmethod
    def __to_matrix(indexes):
        mat = []
        while indexes != []:
            mat.append(indexes[:4])
            indexes = indexes[4:]
        return mat

    @staticmethod
    def __to_symbols(indexes):
        symbols = []
        for x in indexes:
            symbols.append(x["symbol"].replace("^",""))
        return symbols


    def filter_indexes(self,indexes):
        index = []
        for i in indexes:
            for v in i:
                if v == "symbol" and i[v].replace("^","") in self.favourites:
                    index.append(i)
        return index

