import scrapy


class ConsumerElectronicsSpider(scrapy.Spider):
    name = 'consumer_electronics'
    allowed_domains = ['www.cigabuy.com']
    # No need to start_urls, since we call start request function, to override the request header
    # start_urls = ['https://www.cigabuy.com/consumer-electronics-c-56_75-pg-1.html']
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',}

    def start_requests(self):
        yield scrapy.Request(url='https://www.cigabuy.com/consumer-electronics-c-56_75-pg-1.html', callback=self.parse, headers=self.header)

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
            yield scrapy.Request(url=next_page, callback=self.parse, headers=self.header)
