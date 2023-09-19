# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from scrapy.utils.project import get_project_settings
from pdfdrive.items import PdfdriveItem
import json
from scrapy.settings import Settings
import logging

settings = get_project_settings()

class MongoDbPipeline:


    collection_name = 'pdfdrive'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        ## pull in information from settings.py
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        ## initializing spider
        ## opening db connection
        print(f"MONGO DB URI : {self.mongo_uri}")
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]


    def process_item(self, item, spider):
        item = dict(ItemAdapter(item))
        res = self.db[self.collection_name].insert_one(item)
        logging.debug(f"Properties added to MongoDB {res.inserted_id}")
        return item





class JsonWriterPipeline:

    def open_spider(self, spider):
        self.file = open("items.jsonl", "w")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        item = dict(ItemAdapter(item))
        line = json.dumps(item) + "\n"
        self.file.write(line)
        return item