import streamlit as st
from modules.financeGPT import chat_to_gpt
from pathlib import Path
import os
from dotenv import load_dotenv

path = Path(__file__).parent.parent
path = os.path.join(path,'.env')
print(path)
load_dotenv(path)

# Load your API key from an environment variable or secret management service
api_key = os.getenv("OPENAIAPIKEY")

st.set_page_config(page_title='Finance GPT')
st.title(':robot_face: FinanceGPT')
st.write('Simple GPT based assistant that helps you to understandand finance.\n '
            'Finance GPT is a custom model based on openAI serivice. \n'
            '**WARNINGS:** This is not financial advice !!!')


prompt,result = chat_to_gpt(api_key)
if prompt!=None and result!=None:
    st.info(result)