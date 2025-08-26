import streamlit as st
st.title("Mi primera aplicación")
from PIL import Image

st.write("Facilmente puedo realizar backend y frontend")
image = Image.open('U factory relleno.png')
st.image( image, caption=('Interfaces multimodales')
