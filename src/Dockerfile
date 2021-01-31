# start from base
FROM ubuntu:18.04

LABEL maintainer="Abhilash"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt

COPY . /app

RUN export FLASK_APP=Python.py

# We copy just the requirements.txt first to leverage Docker cache
WORKDIR /app


EXPOSE 5000

RUN flask run
