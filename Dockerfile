# Imagen base: Python 3.11 (ligera y actual)
FROM python:3.11-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar primero el archivo de dependencias
COPY requirements.txt .

# Instalar dependencias sin usar caché para reducir tamaño
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Exponer el puerto 1003 (el que usa Flask en tu app)
EXPOSE 1003

# Comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]