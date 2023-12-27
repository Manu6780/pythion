import streamlit as st
import pandas
from send_msg_funct import send_message


with st.form(key="Email Forum"):
    cust_email_addr = st.text_input("Your Email Address", key="email_addr")
    df = pandas.read_csv("topics.csv")
    topic = st.selectbox('What topic do you want to discuss', df["topic"], key="selectbox")
    raw_message = st.text_area("text",key="message")
    button = st.form_submit_button("Submit")
    st.session_state

    message = f'''\
Subject: new email {cust_email_addr}


From: {cust_email_addr}
Topic {topic}
{raw_message}
'''
    if button:
        send_message(message)
        st.info("Message Sent")


