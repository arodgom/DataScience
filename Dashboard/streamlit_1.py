# Para ejecutar streamlit run <nombre del scritp>

import pandas as pd
import streamlit as st

st.write("Primera Aplicación con Streamlit")
st.write("Podemos escribir lo que queramos, texto, en esta ocasión")

st.write("Incluso un Dataframe como a continuación")
df = pd.DataFrame({"a": [10, 20 ,30 , 40, 10], "b": [40, 20 ,10 , 60, 50]})

st.write(df)
st.write("Podemos plotear")
st.bar_chart(df)