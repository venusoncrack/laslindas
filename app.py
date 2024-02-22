import streamlit as st
from PIL import Image

st.title("app de lindas y etereas")

st.header("En este espacio comienzo a desarrollar mis aplicaciones aesthetics etereas lindas para interfaces multimodales.")
st.write("Facilmente puedo realizar backend aesthetic y frontend aesthetic.")
image = Image.open('corazoooon.jpg')

st.image(image, caption='Corazon')

