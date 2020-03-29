# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
# from myproject.items import TestItem

class XmlfeedSpider(XMLFeedSpider):
    name = 'xmlfeed'

    # allowed_domains = ['xamlfeed.com']
    # start_urls = ['http://xamlfeed.com/feed.xml']
    # iterator = 'iternodes' # you can change this; see the docs
    # itertag = 'item' # change it accordingly

    # def parse_node(self, response, selector):
    #     item = {}
    #     #item['url'] = selector.select('url').get()
    #     #item['name'] = selector.select('name').get()
    #     #item['description'] = selector.select('description').get()
    #     return item

    # name = 'example.com'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com/feed.xml']
    iterator = 'iternodes'  # This is actually unnecessary, since it's the default value
    itertag = 'item'

    def parse_node(self, response, node):
        self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.getall()))

        # item = TestItem()
        item['id'] = node.xpath('@id').get()
        item['name'] = node.xpath('name').get()
        item['description'] = node.xpath('description').get()
        return item
