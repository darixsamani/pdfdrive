FROM python:3.8
COPY . /pdfdrive
WORKDIR /pdfdrive
RUN pip install -r ../requirements.txt
EXPOSE 8000
ENTRYPOINT ["scrapy", "quotes", "-o","quotes.jsonl"] 
