FROM python:3.9

WORKDIR /code

# Instalar dependencias del sistema (si necesitas alguna, ej: para PostgreSQL)
# RUN apt-get update && apt-get install -y --no-install-recommends gcc python3-dev

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["fastapi", "run", "app/main.py", "--port", "80"]