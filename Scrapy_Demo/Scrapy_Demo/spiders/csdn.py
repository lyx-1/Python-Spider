# -*- coding: utf-8 -*-
import scrapy
from Scrapy_Demo.items import CourseItem

class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    allowed_domains = ['edu.csdn.net']
    start_urls = ['https://edu.csdn.net/courses/p1']
    p = 1
    # def start_requests(self):

    def parse(self, response):
        course_list = response.selector.xpath('//div[@class="course_item"]')
        item = CourseItem()
        # print(course_list)

        for course in course_list:
            # print(course)
            # print(course.xpath('.//span[@class="course_lessons"]/text()'))
            item['title'] = course.xpath('.//span[@class="title ellipsis-2"]/text()').extract_first().strip()
            item['time'] = course.xpath('.//span[@class="course_lessons"]/text()').extract_first()
            item['price'] = course.xpath('.//span[@class="num"]/em/text()').extract_first()
            item['pic'] = course.xpath('.//img/@src').extract_first()
            yield item

        url = response.url
        self.p += 1
        url_list = url.split('/')
        url_list[-1] = 'p' + str(self.p)
        next_url = '/'
        next_url = next_url.join(url_list)
        if self.p < 4:
            yield scrapy.Request(next_url)
