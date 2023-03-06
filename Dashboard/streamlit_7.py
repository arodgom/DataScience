import streamlit as st
from datetime import time

# slider - ejemplo
# declaramos el texto del slider, el número de inicio, 
# número de fin y el paso en el que empieza
lenguajes = st.slider("Cuántos frameworks conoces de PYthon?", 
                      0, 15, 1)
st.write("Conoces", lenguajes, " Framework de Python")

# slider - ejemplo 2
# declaramos el texto del slider, el número de inicio, 
# número de fin y el intervalo a señalar
rango = st.slider("Seleccionamos un rango de valores", 
                  0.0, 100.0, (25.0, 75.0))
st.write("Rango de valores: ", rango)

# ejemplo 3
hora = st.slider("Hora de la reunión", 
                 value=(time(13,30), time(15,30)))
st.write("Tu reunión tendrá lugar en este intervalo: ",
         hora[0].strftime("%H:%M:%S"),   " - ", hora[1].strftime("%H:%M:%S"))