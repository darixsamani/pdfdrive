FROM python:3.8

MAINTAINER Darix SAMANI
COPY . /app

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install poetry
RUN poetry install



WORKDIR /app/pdfdrive

ENTRYPOINT ["poetry", "run", "scrapy", "crawl", "pdfdrive" ]
