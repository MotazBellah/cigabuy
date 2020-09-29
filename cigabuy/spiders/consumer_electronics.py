import scrapy


class ConsumerElectronicsSpider(scrapy.Spider):
    name = 'consumer_electronics'
    allowed_domains = ['www.cigabuy.com']
    start_urls = ['https://www.cigabuy.com/consumer-electronics-c-56_75-pg-1.html']

    def parse(self, response):
        # Get the div the contain all info about the product
        div_wrapper = response.xpath("//div[@class='p_box_wrapper']")
        for product in div_wrapper:
            name = product.xpath(".//a[@class='p_box_title']/text()").get()
            link = product.xpath(".//a[@class='p_box_title']/@href").get()
            price = product.xpath(".//div[@class='p_box_price']/span[1]/text()").get()
            original_price = product.xpath(".//div[@class='p_box_price']/span[2]/text()").get()

            yield {
                "title": name,
                'url': link,
                "dicsounted_price": price,
                "original_price": original_price,
            }
        # Get the nextPage link
        next_page = response.xpath("(//a[@class='nextPage'])[1]/@href").get()
        # If found, call parse function on the url
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
