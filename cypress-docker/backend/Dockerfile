
FROM python:3.8-slim

ENV DJANGO_DATABASE_NAME=website-db
ENV DJANGO_DATABASE_USER=admin-user
ENV DJANGO_DATABASE_PASSWORD=admin-password
ENV DJANGO_DEBUG=1
ENV DJANGO_DATABASE_HOST database
ENV DJANGO_DATABASE_ENGINE=django.db.backends.postgresql
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV APP_ROOT=/app/workspace
ENV USERNAME=python

WORKDIR ${APP_ROOT}

RUN groupadd -g 1000 ${USERNAME} && useradd -G ${USERNAME} -ms /bin/bash -g 1000 ${USERNAME}

RUN pip install poetry && chown ${USERNAME}:${USERNAME} -R ${APP_ROOT}

USER ${USERNAME}

COPY --chown=${USERNAME} pyproject.toml poetry.lock ./

COPY --chown=${USERNAME} . ${APP_ROOT}

RUN poetry config virtualenvs.in-project "false" && poetry install

CMD [ "poetry", "run", "python3", "manage.py", "runserver", "0.0.0.0:8000" ]
