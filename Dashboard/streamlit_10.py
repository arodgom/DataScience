import streamlit as st
import yfinance as yf

# titulo
st.title("Gráfica con streamlit para finanzas")

# selección de empresa
empresas = ("GOOGL", "AAPL", "TSLA", "NFLX")
option = st.selectbox("Selecciona una de estas empresas: ",
                      empresas)
st.write("Has elegido: ", option)

# 1 año a 5, de 1 en 1 para este ejemplo:
anho = st.slider("Número de años que quieres plotear: ",
                 1, 5, 1)
st.write("Has elegido: ", anho)

anho_final = 2015 + anho
st.write("año final: ", anho, " años")

# obtención de datos vía quandl
data = yf.download(option, "2015-1-1", f"{anho_final}-12-31")
#head
st.write("vamos a imprimir los 5 primeros valores del dataset")
st.write(data.head())

# tambien como dataframe
st.dataframe(data.head())

#tail
st.write("vamos a imprimir los 5 últimos valores del dataset")
st.write(data.tail())

# elegimos la cotización de cierre
st.write("vamos a seleccionar solo la columna close")
data = data[["Close"]]
st.dataframe(data)

st.write("Vamos a plotear el gráfico seleccionado")
st.write("Gráfico seleccionado: ", option)
st.write("Año inicial: 2015, año final: ", anho_final)
st.line_chart(data)
