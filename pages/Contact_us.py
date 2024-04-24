import streamlit as st
from send_email import send_email
import pandas


df_topics = pandas.read_csv('topics.csv')

with st.form(key='email_form'):
    user_email = st.text_input('Your email address')
    option = st.selectbox('What topic do you want to discuss?', df_topics)
    raw_message = st.text_area('Text')
    message = f"""\
   Subject: new email from {user_email}

From: {user_email}
Topic: {option}
{raw_message}
"""
    send_button = st.form_submit_button('Send')


    if send_button:
        send_email(raw_message)
        st.info('Your message was sent')

