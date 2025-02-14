# Usa una imagen base oficial de Python
FROM python:3.13.1-slim

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requerimientos e instálalos
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del proyecto al contenedor
COPY . /app/

# Comando para iniciar la aplicación
CMD ["python",  "manage.py", "runserver", "0.0.0.0:8000"]

# Expone el puerto del contenedor (8000 para Django por defecto)
EXPOSE 8000