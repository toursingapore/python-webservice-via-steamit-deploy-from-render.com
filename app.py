import streamlit as st
st.title("This is my hello world app")
st.header("This is a header")
st.subheader("This is a subheader")
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

age = st.slider("Enter your age")
if age:
    st.write(f"your name is {age}")

location = st.text_input("Enter your location")
if location:
    st.write(f"your name is {location}")
