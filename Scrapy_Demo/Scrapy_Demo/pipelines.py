# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exceptions import DropItem

class ScrapyDemoPipeline(object):
    def process_item(self, item, spider):
        if item['price']:
            return item
        else:
            raise DropItem

class YoudaoPipeline(object):
    def process_item(self, item, spider):
        return item
        # print(item)

class CoursePipeline(object):
    file_path = ''

    def __init__(self, file):
        self.file_path = file

    @classmethod
    def from_crawler(cls, crawler):
        s = cls(crawler.settings.get("FILE_PATH"))
        return s

    def process_item(self, item, spider):
        item_str = json.dumps(dict(item), ensure_ascii=False)
        if self.file_path:
            with open(self.file_path, 'a', encoding='utf-8') as f:
                f.write(item_str + '\n')