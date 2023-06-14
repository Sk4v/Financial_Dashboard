import streamlit as st
from dotenv import load_dotenv
import os
from fmp.financialModelingPrep import FinancialModelingPrep
from .financialDatas import FinancialDatas
from modules.financeGPT import ask_to_gpt
import pandas as pd
load_dotenv()


class FinancialStatements(FinancialDatas):
    def __init__(self,ticker):
        self.fmp = FinancialModelingPrep(token=os.getenv('fmp'))
        self.ticker = ticker
        self.to_ignore_key = ['date','reportedCurrency','fillingDate', 'acceptedDate','calendarYear','link','finalLink','response']

    def show_all_statements(self):
        c1, c2 = st.columns((1, 3))
        with c1:
            self.show_ratio_ttm()
        with c2:
            t1, t2 = st.tabs(['Formulas', 'Finance GPT'])
            with t1:
                self.show_formulas()
            with t2:
                ask_to_gpt()

        st.subheader(':orange[Financial statements]')
        self.show_all_table()

        st.subheader(':orange[Financial growth]')
        self.show_all_growth()

    def show_all_growth(self):
        ig,balance_growth,cash_growth = st.tabs(['Income Growth','Balance Growth','Cash Flow Growth'])
        with ig:
            ig = self.fmp.income_statement_growth(self.ticker)
            self.show_statements_growth(ig)
        with balance_growth:
            bg = self.fmp.balance_sheet_statement_growth(self.ticker)
            self.show_statements_growth(bg)
        with cash_growth:
            cg = self.fmp.cash_flow_statements_growth(self.ticker)
            self.show_statements_growth(cg)


    def show_all_table(self):
        selected_period = ['YEAR']
        ratio_tab,income_tab, balance_tab, cashFlow_tab = st.tabs(['Ratios Statements','Income Statements', 'Balance Statements', 'Cash Flow Statements'])
        with ratio_tab:
            ratio_statements = self.fmp.company_ratios(self.ticker)
            self.__show_statements(selected_period, ratio_statements, 'Ratio-Statements')
        with income_tab:
            income_statements = self.fmp.income_statement(self.ticker)
            self.__show_statements(selected_period, income_statements, 'Income-Statements')
        with balance_tab:
            balance_statements = self.fmp.balance_sheet_statement(self.ticker)
            self.__show_statements(selected_period, balance_statements, 'Balance-Statements')
        with cashFlow_tab:
            cashflow_statements = self.fmp.cash_flow_statement(self.ticker)
            self.__show_statements(selected_period, cashflow_statements, 'CashFlow-Statements')

    def __show_statements(self, selected_period, statements, button_name):
        if selected_period == ['YEAR']:
            df = self.create_statement_table(statements.values,self.to_ignore_key)
            self.gen_button(df,name=button_name)
        elif selected_period == ['QUARTER']:
            df = self.create_statement_table(statements.values,self.to_ignore_key)
            self.gen_button(df,name=button_name)
        else:
            st.info("Select only one of them")

    def show_ratio_ttm(self):
        st.subheader(':orange[Financial Ratios TTM]')
        ratio_statements = [self.fmp.ratios_ttm(self.ticker).__dict__]
        df = self.create_ratiottm_df(ratio_statements)
        self.gen_button(df,'RatiosTTM-Statements')

    def create_ratiottm_df(self,statements):
        datas = {}
        for value in statements:
            values = []
            index = []
            for key in value:
                if key != 'response':
                    index.append(self.fmp.detect_name(key))
                    values.append(value[key])
            datas[self.ticker] = values

        df = pd.DataFrame(datas, index=index)
        st.dataframe(df)
        return df


    def show_statements_growth(self, growth):
        values = [growth.values[0]]
        for i in range(1,len(growth.values)-1):
            if growth.values[i]['date'] != growth.values[i-1]['date']:
                values.append(growth.values[i])
        df = self.create_statement_growth_table(values,self.to_ignore_key)
        return df


