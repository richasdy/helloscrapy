# -*- coding: utf-8 -*-
import scrapy


class ScrapySpider(scrapy.Spider):
    name = 'scrapy'
    allowed_domains = ['scrapy.com']
    start_urls = ['http://scrapy.com/']

    def parse(self, response):
        pass
