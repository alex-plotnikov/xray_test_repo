FROM artifactory.aip.ooo/global-docker-dev-virtual/python:3.7-alpine

WORKDIR /build

COPY requirements.txt .

RUN pip install -U pip \
    && pip install -r requirements.txt