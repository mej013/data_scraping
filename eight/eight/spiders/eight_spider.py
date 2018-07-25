import scrapy
from eight.items import EightItem

class EightSpider(scrapy.Spider):
    name = "eight"

    # For other cities, paste the specific url below
    start_urls = ["https://broker.58.com/sh/list/pn1"]
    # remember to change the page no accordingly
    npages = 140

    # This mimics getting the pages using the next button. 
    for i in range(2, npages + 1):
        # need to change the link below accordingly  
        start_urls.append("https://broker.58.com/sh/list/pn"+str(i)+"")

    def parse(self, response):
        for href in response.xpath('//div[@class="content-side-left"]//li/a[@class="link"]/@href'):
            url = href.extract() 
            yield scrapy.Request(url, callback=self.parse_dir_contents)	
            

    def parse_dir_contents(self, response):
        item = EightItem()

        # Getting Agent's Name
        item['name'] = response.xpath('//div[@class="info-name"]/text()').extract_first().strip()

        # Getting Agent's Phone#
        item['phoneNo'] = response.xpath('//span[@class="info-contact-telephone"]/text()').extract_first().strip()

        # Getting Agent's Company
        item['company'] = response.xpath('//td[@class="info-basic-content info-content"]/text()').extract_first().strip()

        yield item
