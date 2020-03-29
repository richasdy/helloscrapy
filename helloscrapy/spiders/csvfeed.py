# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider
# from myproject.items import TestItem


class CsvfeedSpider(CSVFeedSpider):
    
    name = 'csvfeed'

    # allowed_domains = ['csvfeed.com']
    # start_urls = ['http://csvfeed.com/feed.csv']
    # # headers = ['id', 'name', 'description', 'image_link']
    # # delimiter = '\t'

    # # Do any adaptations you need here
    # #def adapt_response(self, response):
    # #    return response

    # def parse_row(self, response, row):
    #     i = {}
    #     #i['url'] = row['url']
    #     #i['name'] = row['name']
    #     #i['description'] = row['description']
    #     return i

    # name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com/feed.csv']
    delimiter = ';'
    quotechar = "'"
    headers = ['id', 'name', 'description']

    def parse_row(self, response, row):
        self.logger.info('Hi, this is a row!: %r', row)

        item = TestItem()
        item['id'] = row['id']
        item['name'] = row['name']
        item['description'] = row['description']
        return item
