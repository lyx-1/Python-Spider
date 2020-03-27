# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class ScrapyDemoPipeline(object):
    def process_item(self, item, spider):
        if item['title']:
            return item
        else:
            raise DropItem('免费')


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
        # item_str = json.dumps(dict(item), ensure_ascii=False)
        # print(item)
        if self.file_path:
            with open(self.file_path, 'a', encoding='utf-8') as f:
                f.write(item['title'] + ' ' + item['price'] + ' ' + item['time'] + '\n')
        return item


class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        url = item['pic']
        yield scrapy.Request(url=url)

    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-1]
        return file_name

    def item_completed(self, results, item, info):
        # int(results)
        for ok, x in results:
            if ok:
                # print("c")
                # print(item)
                return item
            else:
                raise DropItem()

