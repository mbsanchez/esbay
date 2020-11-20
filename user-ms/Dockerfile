FROM python:3.7-alpine

COPY ./app/requirements.txt /app/requirements.txt

WORKDIR /app

RUN apk add --no-cache --update \
    build-base \
    bash \
    curl \
    gcc \
    libc-dev \
    mariadb-dev \
    musl-dev \
    linux-headers \
  && pip install --upgrade pip \
  && pip install -r requirements.txt

  ENV FLASK_RUN_HOST=0.0.0.0
  ENV FLASK_ENV=development
  EXPOSE 5000

  COPY ./app /app

  CMD ["python", "app.py"]