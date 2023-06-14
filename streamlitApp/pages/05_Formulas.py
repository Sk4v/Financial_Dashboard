from modules.financialDatas import FinancialDatas
import streamlit as st

st.set_page_config(page_title='Formulas')
st.title(':pencil2: Formulas')

fin = FinancialDatas()
formulas = fin.gen_formulas()

k = formulas.keys()
selected = st.multiselect('Select formulas', options=k, default=k)
st.markdown(f'*N. of formulas:* {len(selected)}')
st.divider()

for f in selected:
    st.latex(f'{f}={formulas[f]}')
    st.divider()