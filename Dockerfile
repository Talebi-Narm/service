FROM python:3.11.1-slim-buster

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    POETRY_VERSION=1.3.2

RUN pip install --upgrade pip
RUN apt-get update
RUN apt-get -y install libpq-dev gcc
RUN pip install poetry && pip install gunicorn[gthread]

WORKDIR /usr/src/app

COPY poetry.lock pyproject.toml ./
RUN poetry install --no-interaction --no-ansi -vvv

COPY ./ ./

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind=0.0.0.0:8000", "--worker-tmp-dir=/dev/shm", "--chdir=/usr/src/app", "--log-level='info'", "--log-file=-", "--workers=2", "--threads=4", "--worker-class=gthread", "chain_restaurants.wsgi:application"]
