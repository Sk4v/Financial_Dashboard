import streamlit as st
from dotenv import load_dotenv
from modules.majorsIndex import MajorsIndex
from modules.news import News
from utilities.overview import FoundamentalsData
load_dotenv()


def home():
    st.set_page_config(page_title='EasyStocks',layout="wide",page_icon='logo/ES_icon2.png')
    st.title(':green[Fundamentals]'.upper())
    ticker = st.text_input(label='Ticker', placeholder='Search...',args=['A','b']).upper()

    if ticker:
        fa = FoundamentalsData(ticker)
        fa.show_all()

    else:
        tab1,tab2 = st.tabs(['Top Indexes', 'Generic News'])
        with tab1:
            majorIndexs = MajorsIndex()
            majorIndexs.show_indexes(filter=None)
        with tab2:
            news = News(ticker=None)
            news.show_news()

home()