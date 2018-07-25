import scrapy

class QfSpider(scrapy.Spider):
    name = "qfang"
    #for other cities, simply change the url below
    allowed_domains = ['shanghai.qfang.com']
    
    #for other cities, simply change the start link below
    start_urls = ["https://shanghai.qfang.com/tycoon"]
    
    #for other cities, make sure to change the total page number
    npages = 50
    #This mimic getting the pages using the next button.
    for i in range(2, npages+1):
        start_urls.append("https://shanghai.qfang.com/tycoon/n"+str(i)+"")

    def parse(self, response):
        for broker in response.xpath('//li[@class="brokers-list-item clearfix"]'):
            yield {
                'name': broker.xpath('.//p[@class="name fl"]//text()').extract_first(),
                'phone': broker.xpath('.//div[@class="broker-tel fr"]/p/text()').extract_first().strip(),
            }
        
