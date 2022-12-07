ARG PYTHON_VERSION=3.9-slim-buster

# define an alias for the specfic python version used in this file.
FROM python:${PYTHON_VERSION} as python

ENV POETRY_VERSION=1.2.0

ARG BUILD_ENVIRONMENT=dev
ARG APP_HOME=/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

RUN addgroup --system django \
    && adduser --system --ingroup django django

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
RUN pip install --no-cache-dir poetry==${POETRY_VERSION}

COPY poetry.lock pyproject.toml ${APP_HOME}/

# Project initialization:
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY --chown=django:django ./compose/dev/django/entrypoint /entrypoint
RUN chmod +x /entrypoint


COPY --chown=django:django ./compose/dev/django/start /start
RUN chmod +x /start


COPY --chown=django:django ./compose/dev/django/celery/worker/start /start-celeryworker
RUN chmod +x /start-celeryworker


COPY --chown=django:django ./compose/dev/django/celery/beat/start /start-celerybeat
RUN chmod +x /start-celerybeat


COPY ./compose/dev/django/celery/flower/start /start-flower
RUN chmod +x /start-flower
COPY --chown=django:django . ${APP_HOME}

# make django owner of the WORKDIR directory as well.
RUN chown django:django ${APP_HOME}

USER django

ENTRYPOINT ["/entrypoint"]
