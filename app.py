import streamlit as st
from PIL import Image

st.title("Aplicacion para mujeres lindas y etereas")

st.header("Hola, tal vez te preguntas ¿por qué me encuentro aquí? Bueno... realmente yo tampoco sé por qué, estamos aprendiendo ambas.")
st.write("Te dejo estos corazones para animar tu día")
image = Image.open('corazoooon.jpg')

st.image(image, caption='¡Espero que te hayan gustado!')


texto = st.text_input("Escribe tu correo electrónico para dejarte un lindo mensaje", "correo@gmail.com")
st.write("Verifica, tu correo es:", texto)


col1, col2 = st.columns(2)

with col1: 
  st.subheader("¿Te gustaría recibir mis mensajes por correo?")
  st.write("Será por lo menos 1 mensaje al mes ;)")
  resp = st.checkbox("")
  if resp:
      st.write("Gracias, te estaré contactando")

with col2: 
  st.subheader("En otros temas... ¿Cuál es tu género de pelis favorito?")
  modo = st.radio("Es una difícil decisión, lo sé.", ("Fantasía", "Ciencia ficción", "Romance"))
  if modo == "Fantasía":
    st.write("Que buenos gustos, lo tendré en cuenta.")
  if modo == "Ciencia ficción":
    st.write("Gracias, lo tendré en cuenta.")
  if modo == "Romance":
    st.write("Con que eres románticaaaa, eso me gusta.")
