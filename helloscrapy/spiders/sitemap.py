# -*- coding: utf-8 -*-
from scrapy.spiders import SitemapSpider

class MySpider(SitemapSpider):
    name = 'sitemap'
    sitemap_urls = ['http://www.example.com/sitemap.xml']
    # sitemap_urls = ['http://www.example.com/robots.txt']
    sitemap_rules = [
        ('/product/', 'parse_product'),
        ('/category/', 'parse_category'),
        ('/shop/', 'parse_shop'),
    ]
    sitemap_follow = ['/sitemap_shops']
    other_urls = ['http://www.example.com/about']
    
    def start_requests(self):
        requests = list(super(MySpider, self).start_requests())
        requests += [scrapy.Request(x, self.parse_other) for x in self.other_urls]
        return requests

    def parse_product(self, response):
        pass # ... scrape product ...

    def parse_category(self, response):
        pass # ... scrape category ...

    def parse_shop(self, response):
        pass # ... scrape shop here ...