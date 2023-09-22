FROM python:alpine3.18 as base
LABEL maintainer="vitorsnta90@gmail.com"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY . /app/
COPY scripts_entrypoints ./scripts

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
# python -m venv /venv &&\
#     source /venv/bin/activate &&\

RUN pip install --upgrade pip && \
    pip install -r /app/requirements.txt 

# TODO implements for sh
# ENV PATH="./scripts:$PATH"
# USER duser
# CMD ["docker-entrypoint.sh"]

EXPOSE 8000
