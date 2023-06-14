import openai
import streamlit as st


def ask_to_gpt(api_key):
    openai.api_key=api_key
    if openai.api_key is None or openai.api_key == '':
        st.error('OPENAI API NOT FOUND !')

    st.subheader(":robot_face: Finance GPT")
    prompt = st.text_input("I'll help you on your Financial analysis")

    st.write("ex: *What is it Ebitda ?*")

    if prompt:
        r = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages= [
            {"role": "system", "content": "You are an helpful financial assistant. You can only answer financial and economic questions "},
            {"role": "system", "content": "Your name is Finance GPT"},
            {"role": "user", "content": prompt}
            ]

        )
        st.write(r['choices'][0]['message']['content'])


def chat_to_gpt(api_key):
    openai.api_key = api_key
    if openai.api_key is None or openai.api_key == '':
        st.error('OPENAI API NOT FOUND !')

    prompt = st.text_input("I'll help you on your Financial analysis")

    if prompt:
        r = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages= [
            {"role": "system", "content": "You are an helpful financial assistant. You can only answer financial and economic questions "},
            {"role": "system", "content": "Your name is Finance GPT"},
            {"role": "user", "content": prompt}
            ]
        )
        result = r['choices'][0]['message']['content']

        return prompt,result
    else: return None,None