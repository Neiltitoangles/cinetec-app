FROM python:3.11-slim

# Evita que python genere archivos basura
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del proyecto
COPY . .

# Expone el puerto 8000
EXPOSE 8000

# Ejecuta el migrate y luego inicia el servidor
CMD sh -c "python manage.py migrate --noinput && gunicorn --bind 0.0.0.0:8000 cine_project.wsgi:application"