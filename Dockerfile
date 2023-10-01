FROM python:alpine3.18 as base
LABEL maintainer="vitorsnta90@gmail.com"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY . /app/
COPY ./docker/scripts_entrypoints /scripts

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && \
    pip install -r /app/requirements.txt
# ENV PATH="/app/scripts/docker/scripts_entrypoints:$PATH"
# ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 8000
