FROM python:3.10-slim

RUN pip install poetry

WORKDIR /app

COPY . .

EXPOSE 8000

RUN poetry install


CMD poetry run python manage.py runserver 0.0.0.0:8000
