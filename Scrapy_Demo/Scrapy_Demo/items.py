# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class YoudaoItem(scrapy.Item):
    result = scrapy.Field()

class CourseItem(scrapy.Item):
    title = scrapy.Field()
    time = scrapy.Field()
    price = scrapy.Field()
