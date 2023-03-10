FROM python:3.11-slim

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

WORKDIR /usr/src/app

RUN apt-get update --fix-missing
RUN pip install --upgrade pip
RUN pip install poetry gunicorn[gthread]

COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root --no-interaction --no-ansi

COPY ./ ./

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind=0.0.0.0:8000", "--worker-tmp-dir=/dev/shm", "--chdir=/usr/src/app", "--log-level='info'", "--log-file=-", "--workers=2", "--threads=4", "--worker-class=gthread", "Kadoo.wsgi:application"]
