import scrapy

import logging
from scrapy.utils.log import configure_logging

class AuthorSpider(scrapy.Spider):
    name = 'author'

    start_urls = ['http://quotes.toscrape.com/']

    custom_settings = {
        'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter',
        'DOWNLOAD_DELAY': 2,
        'ITEM_PIPELINES': {
            # 'helloscrapy.pipelines.pipelines': 300,
            # 'mybot.pipelines.validate.ValidateMyItem': 300,
            # 'mybot.pipelines.validate.StoreMyItem': 800,
        },
    }

    logging.basicConfig(
        filename='log.txt',
        # format='%(levelname)s: %(message)s',
        # level=logging.INFO
    )

    def parse(self, response):
        
        self.logger.debug('Parse function called on %s', response.url)
        self.logger.info('Parse function called on %s', response.url)
        self.logger.warning('Parse function called on %s', response.url)
        self.logger.error('Parse function called on %s', response.url)
        self.logger.critical('Parse function called on %s', response.url)

        author_page_links = response.css('.author + a')
        yield from response.follow_all(author_page_links, self.parse_author)

        pagination_links = response.css('li.next a')
        yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }