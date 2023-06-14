from streamlitApp.fmp.financialModelingPrep import FinancialModelingPrep
import streamlit as st
import pandas as pd

fmp = FinancialModelingPrep(token="869cd49e1f0765ce1fcf59116b52c105")
st.sidebar.markdown('pippo')
st.title('Company Financial Ratios')
st.markdown("This endpoint returns financial ratios for companies to help in company analysis. This endpoint computes ratios for each financial statement presented by the company (you can find those on our financial statements endpoint). This endpoint supports all of our API's companies. Visit our formula page to learn more about how we calculate those ratios. We also recommend that you look at our key metrics and enterprise value endpoints!")
ratio = fmp.company_ttm_ratios('AAPL')
values=[]
index=[]
for value in ratio.__dict__:
    #if 'Response' not in fmp.detect_name(value):
        index.append(fmp.detect_name(value))
        values.append(ratio.__dict__[value])

data = {
  "Value": values,
    "Formula": ["CurrentAssets/CurrentLiabilities" for x in index],
  "Info": [f"info about {x}..." for x in index]

}
df = pd.DataFrame(data, index = index)
st.dataframe(df)  # Same as st.write(df)

csv = df.to_csv().encode('utf-8')

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='RatiosTTM.csv',
    mime='text/csv',
)