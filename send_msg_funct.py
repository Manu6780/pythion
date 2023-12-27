import smtplib
import ssl

import streamlit as st

def send_message(message):
    host = "smtp.gmail.com"
    username = "shawn.manu@gmail.com"
    password = "vlzxxkgigafbtbpv"
    port = "465"
    reciever = "shawn.manu@gmail.com"
    context = ssl.SSLContext()

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever,message)


