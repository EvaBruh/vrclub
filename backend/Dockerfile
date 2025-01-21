FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /backend

COPY pyproject.toml poetry.lock /backend/

RUN pip install poetry && poetry install

COPY . /backend

EXPOSE 8000
