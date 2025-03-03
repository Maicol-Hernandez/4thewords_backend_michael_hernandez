FROM python:3.9

WORKDIR /code

# Instalar dependencias del sistema (si necesitas compilar librerías)
RUN apt-get update && apt-get install -y --no-install-recommends \
    default-libmysqlclient-dev \
    gcc \
    python3-dev \
    pkg-config \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /code/app

CMD ["fastapi", "dev", "app/main.py", "--port", "80"]