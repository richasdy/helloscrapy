import scrapy

class SettingSpider(scrapy.Spider):
    name = 'setting'
    start_urls = ['http://example.com']

    def parse(self, response):
        print("Existing settings: %s" % self.settings.attributes.keys())