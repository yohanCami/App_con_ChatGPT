# Importar la librería de Streamlit
import streamlit as st

# Título y autor de la app
st.title("Mi primera app")
st.write("Esta app fue elaborada por Yohan Camilo Sánchez")

# Preguntar el nombre al usuario
nombre_usuario = st.text_input("Por favor, introduce tu nombre")

# Imprimir mensaje de bienvenida
if nombre_usuario:
    st.write(f"{nombre_usuario}, te doy la bienvenida a mi primera app.")
