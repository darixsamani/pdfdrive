# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from itemadapter import ItemAdapter
import pymongo
from scrapy.utils.project import get_project_settings
from pdfdrive.items import PdfdriveItem
import json

settings = get_project_settings()

class PdfdrivePipeline:


    def __init__(self) -> None:
        conn = pymongo.MongoClient(
            settings.get('MONGO_HOST'),
            settings.get('MONGO_PORT')
        )
        db = conn[settings.get('MONGO_DB_NAME')]
        self.collection = db[settings['MONGO_COLLECTION_NAME']]


    def process_item(self, item, spider):

        if isinstance(item, [PdfdriveItem]):

            self.collection.insert_one(PdfdriveItem.toDict())
        return item



class JsonWriterPipeline:
    def open_spider(self, spider):
        self.file = open("items.jsonl", "w")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):

        if isinstance(item, PdfdriveItem):
            line = json.dumps(item.toDict()) + "\n"
        self.file.write(line)
        return item