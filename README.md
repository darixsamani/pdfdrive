# pdfdrive
I build this project to enhance my python skill after a long of time no coding


## what does it do

it's a web scraper that collects information on the pdfdrive.com site and then saves it in a file and in a mongodb database


## How to install

`1. Install virtual env
  ```
  pip3 install virtualenv
  ```
2. Create virtual env
```
virtualenv env
```
4. Active vituale enn
```
source enc/bin/activate
```
5. Install requirements
```
pip3 install -r requirements.txt
```
6. Laucch Spider
   Before modify  `.env` to your mondo de URI
```
cd pdfdrive && scrapy crwal pdfdrive
```
