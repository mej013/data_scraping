import scrapy

class SinaSpider(scrapy.Spider):
    name = "sina"
    #for other cities, simply change the url below
    allowed_domains = ['sh.esf.leju.com']
    
    #for other cities, simply change the start link below
    start_urls = ["https://sh.esf.leju.com/agent/"]
    
    #for other cities, make sure to change the total page number
    npages = 53
    #This mimic getting the pages using the next button.
    for i in range(2, npages+1):
        #for other cities, need to change the url below accordingly
        start_urls.append("https://sh.esf.leju.com/agent/n"+str(i)+"")

    def parse(self, response):
        headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        
        for broker in response.xpath('//dd[@class="fl"]'):
            yield {
                'name': broker.xpath('.//div[@class="tit clearfix"]//a[@target="_blank"]/text()').extract_first().strip(),
                'phone': broker.xpath('.//div[@class="tit clearfix"]//a[@target="_blank"]/span/text()').extract_first(),
                'company': broker.xpath('//div[@class="info"]//span/em[@class="txt-cut"]/text()').extract_first()
            }
        
