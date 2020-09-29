import scrapy


class ConsumerElectronicsSpider(scrapy.Spider):
    name = 'consumer_electronics'
    allowed_domains = ['www.cigabuy.com']
    start_urls = ['https://www.cigabuy.com/consumer-electronics-c-56_75-pg-1.html']

    def parse(self, response):
        div_wrapper = response.xpath("//div[@class='p_box_wrapper']")
        for i in div_wrapper:
            name = i.xpath(".//a[@class='p_box_title']/text()").get()
            link = i.xpath(".//a[@class='p_box_title']/@href").get()
            price = i.xpath(".//div[@class='p_box_price']/span[1]/text()").get()
            original_price = i.xpath(".//div[@class='p_box_price']/span[2]/text()").get()

            yield {
                "title": name,
                'url': link,
                "dicsounted_price": price,
                "original_price": original_price,
            }
