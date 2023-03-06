import streamlit as st

# entrada de texto
entrada_texto = st.text_input("Inserte texto: ")
st.write("Texto del text input: ", entrada_texto)

# entrada de números
entrada_num = st.number_input("Inserte un número: ")
st.write("el número de number input es: ", entrada_num)