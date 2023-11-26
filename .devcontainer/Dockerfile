FROM python:3.11.6


RUN mkdir -p /usr/src

WORKDIR /usr/src

COPY requirements.txt requirements_dev.txt ./

RUN pip install -r requirements.txt