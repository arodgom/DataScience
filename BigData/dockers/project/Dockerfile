#Instalación de Python
FROM python:3.8

# Instalación de las librerías
RUN pip install fastapi uvicorn[standard]

# Puerto de acceso: 80
EXPOSE 80

# Carpeta se copie en la imagen de docker en app
COPY ./app /app

# Comando de ejecución
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"] 