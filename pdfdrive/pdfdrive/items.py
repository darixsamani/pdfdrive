# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from typing import List

class PdfdriveItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url_book: str = scrapy.Field()
    size_book :str = scrapy.Field()
    year: int = scrapy.Field()
    number_pages: str = scrapy.Field()
    title :str = scrapy.Field()
    url_image:str= scrapy.Field()
    langage_book: str = scrapy.Field()
    tags: List[str]= scrapy.Field()


    def __dict__(self):

        data = dict({"url_book":self.url_book, "size_book": self.size_book,
                      "year": self.year, "number_pages": self.number_pages,
                    "title": self.title, "url_image": self.url_image,
                     "languag_book": self.langage_book, "tags": self.tags }) 
        return data
