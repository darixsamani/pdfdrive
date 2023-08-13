FROM python:3.8

MAINTAINER Darix SAMANI
COPY . /app

WORKDIR /app

RUN ls -al
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /app/pdfdrive

RUN ls -al
ENTRYPOINT ["scrapy", "crawl",   "pdfdrive" ]

