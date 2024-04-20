import streamlit as st
st.set_page_config(
    page_title="This is my page title",
    page_icon=":smiling_face_with_sunglasses:", #get icon from https://www.webfx.com/tools/emoji-cheat-sheet/
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Contact': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

with st.container():
    st.title("This is a title header H1")
    st.header("This is a header H2")
    st.subheader("This is a subheader H3")
    st.caption("This is a caption")
    #st.image("kid.jpg")
    #st.audio("audio.mp3")
    #st.video("video.mp4")
    st.code("x=2021")
    st.write("hello world")
    st.write("[>>Xem thêm](https://markdowntohtml.com)")

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
    st.write(f"your age is {age}")

describeYourself = st.select_slider('Describe yourself', ['Bad', 'Good', 'Excellent'])
if describeYourself:
    st.write(f"yourself is {describeYourself}")

location = st.text_input("Enter your location")
if location:
    st.write(f"your location is {location}")

cbox = st.checkbox('Are you gay?')
if cbox:
    st.write(f"Checked {cbox} you are a gay")

myButton = st.button('Click here')
if myButton:
    st.write(f"{myButton} - You have just clicked 'Click here' button")

myRadio = st.radio('Pick your gender',['Male','Female'])
if myRadio:
    st.write(f"Choose {myRadio}")

mySelectbox = st.selectbox('Pick your gender',['Male','Female'])
if mySelectbox:
    st.write(f"Seleted {mySelectbox}")

myMultiselect = st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
if myMultiselect:
    st.write(f"Seleted {myMultiselect}")
