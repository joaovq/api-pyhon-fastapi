FROM python:alpine3.18 as base
LABEL maintainer="vitorsnta90@gmail.com"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY ../ /code/
WORKDIR /code/
EXPOSE 8000
ENTRYPOINT [ "docker-entrypoint.sh" ] 