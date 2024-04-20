import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="This is my Page title", page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)

#--- HEADERS ---
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

#--- FUNC LOAD ANIMATION IMAGE FROM lottie ---
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")

#--- 3 COLUMNS ---
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
       st.header("A cat")
       st.image("https://static.streamlit.io/examples/cat.jpg")
       st.write(
           """
            ### Make Money Online using Python + Streamlit            
            Learn how to make money online using Python! In this video, you will see how to create a website using Streamlit and sell digital products. To collect the payment, we will be using Stripe. You do not need HTML, CSS or Javascript knowledge to make the website.         
            [Xem thêm](https://mytoolbelt.onrender.com/)
           """
       ) 
    with col2:
       st.header("A dog")
       st.image("https://static.streamlit.io/examples/dog.jpg")
       st_lottie(lottie_coding, height=300, key="my-coding")
    with col3:
       st.header("An owl")
       st.image("https://static.streamlit.io/examples/owl.jpg")

#--- 2 COLUMNS như Blog Postings ---
with st.container():
    col1, col2 = st.columns((1,2))
    with col1:
       st.image("https://res.klook.com/image/upload/fl_lossy.progressive,q_85/c_fill,w_400,h_260/v1713528071/whnuihuknsylm6iy1m93.webp")
    with col2:
       st.subheader("Tất Tần Tật Kinh Nghiệm Du Lịch Ở Phuket Thái Lan Mà Bạn Chưa Biết")
       st.write(
           """
            Tất Tần Tật Kinh Nghiệm Du Lịch Ở Phuket Thái Lan Mà Bạn Chưa Biết.         
            [Xem thêm](https://haidangtravel.com/tin-tuc/phuket-thai-lan)
           """
       )         
with st.container():
    col1, col2 = st.columns((1,2))
    with col1:
       st.image("https://haidangtravel.com/image/Top-8-Cho-Noi-Thai-Lan-duoc-Du-Khach-Du-Lich-Ghe-den-den-Nhieu-Nhat-hinh-1.jpg")
    with col2:
       st.subheader("Khám Phá Đảo Koh Phi Phi - Thiên Đường Nghỉ Dưỡng Tại Thái Lan")
       st.write(
           """
            Khám Phá Đảo Koh Phi Phi - Thiên Đường Nghỉ Dưỡng Tại Thái Lan.         
            [Xem thêm](https://haidangtravel.com/tin-tuc/dao-koh-phi-phi)
           """
       )         

#--- MARKDOWN convert to HTML website ---
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

HTMLcode = '<iframe width="560" height="315" src="https://www.youtube.com/embed/VqgUkExPvLY?si=AhRA4pAkjbWduMDo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
st.components.v1.html(HTMLcode, width=None, height=None, scrolling=False)
