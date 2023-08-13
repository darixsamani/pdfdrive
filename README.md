# pdfdrive
I build this project to enhance my python skill after a long of time no coding


## what does it do

it's a web scraper that collects information on the pdfdrive.com site and then saves it in a file and in a mongodb database


## How to install

`1. Install virtual env
  ```
  pip3 install virtualenv
  ```
2. Create  a virtual environment
```
virtualenv env
```
4. activate a virtual environment
```
source enc/bin/activate
```
5. Install requirements
```
pip3 install -r requirements.txt
```
6. Laucch Spider
  Before changing `.env` to your URI mondo
```
cd pdfdrive && scrapy crwal pdfdrive
```


## Run with docker

```
docker pull darixsamani/pdfdrive
docker run -it -e MONGO_URI=mongodb://localhost:27017 -e MONGO_DATABASE=pdfdrive darixsamani/pdfdrive
```
