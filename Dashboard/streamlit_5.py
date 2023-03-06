import streamlit as st

opcion = st.selectbox("tu lenguaje de programación favorito", 
                      ("Python", "C++", "Matlab"))
st.write("Seleccionaste", opcion)