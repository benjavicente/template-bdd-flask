FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y install --no-install-recommends postgresql-common
RUN yes | /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends postgresql-client-16

RUN pip3 --disable-pip-version-check --no-cache-dir install Flask psycopg[binary]
