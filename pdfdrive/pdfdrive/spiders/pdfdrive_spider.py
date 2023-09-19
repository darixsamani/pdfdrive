from pathlib import Path
import scrapy
from scrapy.shell import Shell
from bs4 import BeautifulSoup
import requests
import lxml
from pdfdrive.items import PdfdriveItem
from scrapy.utils.project import get_project_settings

settings=get_project_settings()

import redis

r = redis.Redis(
  host=settings.REDIS_HOST,
  port=settings.REDIS_PORT,
  password=settings.REDIS_PASSWORD)

class PdfdriveSpider(scrapy.Spider,):
    name = "pdfdrive"

    custom_settings = {
    'LOG_FILE': 'pdfdrive/logs/pdfdrivespider.log',
    'LOG_LEVEL': 'DEBUG'
  }
    


    def start_requests(self):
        
        for url in [f"http://www.pdfdrive.com/category/{i}" for i in range(0,115)]:

            yield scrapy.Request(url=url, callback=self.parse)

        
    def parse(self, response):

        for book in response.css("div.row"):
            
            url_book = book.css('a::attr(href)').get()
            url_book = "http://www.pdfdrive.com" + url_book

            if not r.exists(url_book):
                # get more informatonn url
                same_book = BeautifulSoup(requests.get(url=url_book).text, "lxml")

                pdfdrive_item  = PdfdriveItem()

                pdfdrive_item["url_book"] = "http://www.pdfdrive.com" + book.css('a::attr(href)').get()
                pdfdrive_item["size_book"] = book.css("span.fi-size::text").get()
                pdfdrive_item["year"] = int(book.css('span.fi-year::text').get())
                pdfdrive_item["number_pages"] = book.css('span.fi-pagecount::text').get()
                pdfdrive_item["title"] = book.css('h2::text').get()
                pdfdrive_item["url_image"] = book.css("img.img-zoom::attr(src)").get()
                pdfdrive_item["langage_book"] = same_book.find_all("span",{"class":"info-green"})[-1].get_text()
                pdfdrive_item["tags"] = [tag.get_text() for tag in same_book.find_all('div', {'class': 'ebook-tags'})[0].find_all('a')]

                yield pdfdrive_item

                r.set(url_book, "True")

            
            # yield {
            #     "url_book": "http://www.pdfdrive.com" + book.css('a::attr(href)').get(),
            #     "size_book" : book.css("span.fi-size::text").get(),
            #     "year" : book.css('span.fi-year::text').get(),
            #     "number pages": book.css('span.fi-pagecount::text').get(),
            #     "title": book.css('h2::text').get(),
            #     "url_image": book.css("img.img-zoom::attr(src)").get(),
            #     "langage_book" : same_book.find_all("span",{"class":"info-green"})[-1].get_text(),
            #     "tags": [tag.get_text() for tag in same_book.find_all('div', {'class': 'ebook-tags'})[0].find_all('a')]
            # }
        
        
        next_page = response.css("a.next::attr(href)").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            # print(f"Next Page : {response.urljoin(next_page)}")
            yield scrapy.Request(next_page, callback=self.parse)
    