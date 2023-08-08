from pathlib import Path
import scrapy
from scrapy.shell import Shell
from bs4 import BeautifulSoup
import requests
import lxml
from pdfdrive.items import PdfdriveItem

class PdfdriveSpider(scrapy.Spider,):
    name = "pdfdrive"


    def start_requests(self):
        
        for url in [f"http://www.pdfdrive.com/category/{i}" for i in range(0,115)]:

            yield scrapy.Request(url=url, callback=self.parse)

        
    def parse(self, response):
        for book in response.css("div.row"):
            print(f"TYPE : {type(book.css('a::attr(href)').get())}")
            url_book = book.css('a::attr(href)').get()
            url_book = "http://www.pdfdrive.com" + url_book

            print(f"URL BOOK : {url_book}")

            same_book = BeautifulSoup(requests.get(url=url_book).text, "lxml")
            # s = same_book.find_all('div', {'class': 'ebook-tags'})[0].find_all("a")
            # SM = [ tag.get_text() for tag in same_book.find_all('div', {'class': 'ebook-tags'})[0].find_all("a")]
            # print(f"HTML LEN {len(s)}{url_book} RESPONSE {SM} {same_book.find_all('div', {'class': 'ebook-tags'})}")

            yield PdfdriveItem(
                url_book = "http://www.pdfdrive.com" + book.css('a::attr(href)').get(),
                size_book = book.css("span.fi-size::text").get(),
                year =  int(book.css('span.fi-year::text').get()),
                number_pages = book.css('span.fi-pagecount::text').get(),
                title = book.css('h2::text').get(),
                url_image = book.css("img.img-zoom::attr(src)").get(),
                langage_book = same_book.find_all("span",{"class":"info-green"})[-1].get_text(),
                tags = [tag.get_text() for tag in same_book.find_all('div', {'class': 'ebook-tags'})[0].find_all('a')]
            )
            # {
            #     "url_book": "http://www.pdfdrive.com" + book.css('a::attr(href)').get(),
            #     "size_book" : book.css("span.fi-size::text").get(),
            #     "year" : book.css('span.fi-year::text').get(),
            #     "number pages": book.css('span.fi-pagecount::text').get(),
            #     "title": book.css('h2::text').get(),
            #     "url_image": book.css("img.img-zoom::attr(src)").get(),
            #     "langage_book" : same_book.find_all("span",{"class":"info-green"})[-1].get_text(),
            #     "tags": [tag.get_text() for tag in same_book.find_all('div', {'class': 'ebook-tags'})[0].find_all('a')]
            # }
        
        print("URL {response.url}")
        next_page = response.css("a.next::attr(href)").get()
        print(f"NEXT Page : {next_page}")
        if next_page is not None:
            next_page = response.urljoin(next_page)
            print(f"Next Page : {response.urljoin(next_page)}")
            yield scrapy.Request(next_page, callback=self.parse)
    

    def myparse(self, response):
        print(f"url de base dans my parser : {self.base_url}" )
        self.same_book = response
    

    # def parsemy(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = f"quotes-{page}.html"
    #     Path(filename).write_bytes(response.body)
    #     self.log(f"Saved file {filename}")
