FROM python:3.9

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    default-libmysqlclient-dev \
    gcc \
    python3-dev \
    pkg-config \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

RUN groupadd -g 1000 devgroup
RUN useradd -u 1000 -ms /bin/bash -g devgroup devuser

COPY --chown=devuser:devgroup . /app

RUN chown -R devuser:devgroup /app

USER devuser

CMD ["fastapi", "dev", "app/main.py", "--port", "80"]