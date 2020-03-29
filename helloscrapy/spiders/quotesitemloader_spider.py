import scrapy
from scrapy.loader import ItemLoader
from helloscrapy.items import Quote

class QuoteItemLoaderSpider(scrapy.Spider):
    name = "quotesitemloader"

    start_urls = [
        'http://quotes.toscrape.com',
    ]

    custom_settings = {
        'DOWNLOAD_DELAY': 2,
    }

    def parse(self, response):
        
        self.logger.info('A response from %s just arrived!', response.url)

        # l = ItemLoader(item=Quote(), response=response)
        # l = ItemLoader(item=Quote, response=response)

        for quote in response.css('div.quote'):

            self.logger.info('in quote loop')

            l = ItemLoader(item=Quote(), response=quote)

            self.logger.info('after quote loop')

            l.add_css('text','span.text::text')
            l.add_css('author','small.author::text')
            l.add_css('tags','div.tags a.tag::text')
            l.add_value('last_updated','today')
            yield l.load_item()

            # yield {
            #     'text': quote.css('span.text::text').get(),
            #     'author': quote.css('small.author::text').get(),
            #     'tags': quote.css('div.tags a.tag::text').getall(),
            # }
        
        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:

        #     yield response.follow(next_page, callback=self.parse)

