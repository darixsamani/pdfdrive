FROM python:3.8

MAINTAINER Darix SAMANI
COPY . /app
WORKDIR /app


RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

RUN pip install virtualenv 
RUN virtualenv env
 
SHELL ["env/bin/activate"]

RUN cd /pdfdrive

ENTRYPOINT ["scrapy", "crawl", "pdfdrive"] 

