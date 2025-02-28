# Usamos una imagen oficial de Python
FROM python:3.13.1

# Definir el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Configurar variable de entorno para Django
ENV DJANGO_CSRF_TRUSTED_ORIGINS="https://gc-django-app-340020449796.*"

# Exponer el puerto donde corre Django
EXPOSE 8000

# Comando para correr la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
