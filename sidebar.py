# importar la librería streamlit
import streamlit as st
# Título de la aplicación
st.title(" Mi primera App con Streamlit")
# crea una barra lateral
sidebar = st.sidebar

# Titulo de la barra lateral
sidebar.title("Esta es la barra lateral")
sidebar.write('Aqui van los elementos de entrada')
# subtitulos
st.header("Información sobre el conjunto de datos")
st.header('Descripción de los datos')
st.write("""Esta app predice mis datos
ejemplo de app para predecir""")