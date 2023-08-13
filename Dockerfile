FROM python:3.8

MAINTAINER Darix SAMANI
COPY . /app

WORKDIR /app

RUN pip install virtualenv 
RUN virtualenv env
RUN . env/bin/activate

RUN pip install --upgrade pip
RUN pip install -r requirements.txt



WORKDIR /app/pdfdrive

ENTRYPOINT ["scrapy", "crawl",   "pdfdrive" ]

