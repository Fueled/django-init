ARG PYTHON_VERSION=3.9-slim-buster

# define an alias for the specfic python version used in this file.
FROM python:${PYTHON_VERSION} as python

ARG BUILD_ENVIRONMENT=local
ARG APP_HOME=/app

ENV POETRY_VERSION=1.2.0
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

# Cache our requirements and only reinstall them when pyproject.toml or poetry.lock files change
# COPY poetry.lock pyproject.toml ${APP_HOME}

# Install required system dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    # dependencies for building Python packages
    build-essential \
    # psycopg2 dependencies
    libpq-dev \
    # Translations dependencies
    gettext \
    # Versatile image field & pillow \
    libmagic1 \
    libmagic-dev \
    # cleaning up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry==${POETRY_VERSION}

# Requirements are installed here to ensure they will be cached.
COPY poetry.lock pyproject.toml ${APP_HOME}/

# Project initialization:
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY ./compose/local/entrypoint /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/start /start
RUN chmod +x /start

COPY ./compose/dev/django/celery/worker/start /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./compose/dev/django/celery/beat/start /start-celerybeat
RUN chmod +x /start-celerybeat

COPY ./compose/dev/django/celery/flower/start /start-flower
RUN chmod +x /start-flower

# copy application code to WORKDIR
COPY . ${APP_HOME}

ENTRYPOINT ["/entrypoint"]
