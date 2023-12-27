# FROM python:3-alpine3.15
# WORKDIR /app
# COPY . /app
# RUN pip install flask
# RUN pip install flask_restful
# EXPOSE 3000
# CMD python ./app.py

FROM ubuntu:latest

RUN apt update
RUN apt install python3-pip -y
RUN pip3 install Flask flask_restful
RUN pip3 install pytest

WORKDIR /app

COPY . /app



