import streamlit as st
from PIL import Image

st.title("app de lindas y etereas")

st.header("En este espacio comienzo a desarrollar mis aplicaciones aesthetics etereas lindas para interfaces multimodales.")
st.write("Facilmente puedo realizar backend aesthetic y frontend aesthetic.")
image = Image.open('corazoooon.jpg')

st.image(image, caption='Corazon')


texto = st.text_input('hola hermosa', 'esta es mi aapppp')
st.write('el texto escrito es', texto)

st.subheader("Ahora usemos dos columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia de usuario")
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st.write
