import scrapy

class WiwjSpider(scrapy.Spider):
    name = "wiwj"
    # for other cities, simply change the url below
    allowed_domains = ['sh.5i5j.com']
    
    # for other cities, simply change the start link below
    start_urls = ["https://sh.5i5j.com/jingjiren/"]
    
    # for other cities, make sure to change the total page number
    npages = 200
    # This mimic getting the pages using the next button.
    for i in range(2, npages+1):
        # for other cities, need to change the url below accordingly
        start_urls.append("https://sh.5i5j.com/jingjiren/n"+str(i)+"")

    def parse(self, response):
        for agent in response.xpath('//div[@class="agent-con lf"]'):
            yield {
                'name': agent.xpath('.//div[@class="agent-tit"]/a/span/h3/text()').extract_first(),
                'phone': agent.xpath('.//div[@class="contacty"]/span/text()').extract_first(),
                'company': agent.xpath('.//p[@class="iconsleft"]/text()').extract_first()
            }
        
