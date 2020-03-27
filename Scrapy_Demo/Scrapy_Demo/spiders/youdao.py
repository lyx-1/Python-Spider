# -*- coding: utf-8 -*-
import scrapy
import json
from Scrapy_Demo.items import YoudaoItem

class YoudaoSpider(scrapy.Spider):
    name = 'youdao'
    allowed_domains = ['youdao.com']
    # start_urls = ['http://youdao.com/']

    def start_requests(self):
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        data = {
            'i': '我',
            'doctype': 'json'
        }

        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse)

    def parse(self, response):
        # res = response.json()
        res = json.loads(response.body)
        item = YoudaoItem()
        item['result'] = res['translateResult'][0][0]['tgt']
        yield item
