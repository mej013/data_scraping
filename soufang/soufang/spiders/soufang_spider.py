import scrapy

class SfSpider(scrapy.Spider):
    name = "soufang"
    #for other cities, simply change the url below
    allowed_domains = ['http://sh.sofang.com']
    
    #for other cities, simply change the start link below
    start_urls = ["http://sh.sofang.com/brokerlist"]
    
    #for other cities, make sure to change the total page number
    npages = 5
    #This mimic getting the pages using the next button.
    for i in range(2, npages):
        start_urls.append("http://sh.sofang.com/brokerlist?page="+str(i)+"&")

    def parse(self, response):
        for broker in response.xpath('//li/dl'):
            yield {
                'name': broker.xpath('.//a[@class="broker_name"]/text()').extract_first(),
                'phone': broker.xpath('.//dd[@class="dd"]/span/text()').extract_first(),
                'company': broker.xpath('.//dd/p/text()').extract_first()
            }
        
