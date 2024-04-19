import streamlit as st

st.write("hello world")

#This markdown for showing html website
"""
# This is my login form

In this form will collect info following as below
* Name
* Age
* Location

_We do not sell these data_
"""

name = st.text_input("Enter your name")
if name:
    st.write(f"your name is {name}")

