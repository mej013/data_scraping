import scrapy

class TianxiaSpider(scrapy.Spider):
    name = "tianxia"
    # for other cities, simply change the url below
    allowed_domains = ['esf.sh.fang.com']
    
    # for other cities, simply change the start link below
    start_urls = ["http://esf.sh.fang.com/agenthome/"]
    
    # for other cities, make sure to change the total page number
    npages = 100
    # This mimic getting the pages using the next button.
    for i in range(2, npages+1):
        # To change the location, please edit the url below accordingly
        start_urls.append("http://esf.sh.fang.com/agenthome/-i3"+str(i)+"-j310/"+"")

    def parse(self, response):
        for agent in response.xpath('//div[@class="agent_ren fl"]'):
            yield {
                'name': agent.xpath('.//div[@class="ttop"]//b/text()').extract_first(),
                'phone': agent.xpath('.//p[@class="gray3 f14 liaxni"]/text()').extract_first(),
                'company': agent.xpath('.//span[@class="gray3 fl"]/text()').extract_first().strip()
            }

