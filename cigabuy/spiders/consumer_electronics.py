import scrapy


class ConsumerElectronicsSpider(scrapy.Spider):
    name = 'consumer_electronics'
    allowed_domains = ['www.cigabuy.com/consumer-electronics-c-56_75-pg-1.html']
    start_urls = ['http://www.cigabuy.com/consumer-electronics-c-56_75-pg-1.html/']

    def parse(self, response):
        pass
