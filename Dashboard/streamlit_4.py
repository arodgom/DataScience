import streamlit as st

radio = st.radio(("tener en cuenta los Outliers"),
                 ("Sí", "No"))
if radio == "Sí":
    st.write("No eliminaremos los Outliers")
else:
    st.write("Eliminaremos los Outliers")