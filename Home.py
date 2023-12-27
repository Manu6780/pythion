import streamlit as st
import pandas

st.set_page_config(layout="wide")
st.header("The Best Company ")
st.write(""" Stakeholders are requested to ensure that the proposed name selected does not contain any word as prohibited in Section 4(2) & (3)
 of the Companies Act, 2013 read with Rule 8 of the Companies (Incorporation) Rules, 2014.""")
st.subheader("Our Team")

col1, col2, col3 = st.columns(3)
df = pandas.read_csv("data.csv", sep=",")
with col1:
    for index,row in df[0:4].iterrows():
        st.subheader(row["first name"].title()+" "+ row["last name"].title())
        st.write(row["role"])
        st.image("images/" + row["image"])
with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(row["first name"].title() + " " + row["last name"].title())
        st.write(row["role"])
        st.image("images/" + row["image"])
with col3:
    for index, row in df[8:].iterrows():
        st.subheader(row["first name"].title() + " " + row["last name"].title())
        st.write(row["role"])
        st.image("images/" + row["image"])