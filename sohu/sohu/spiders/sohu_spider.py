#!/usr/bin/python
#coding:utf-8
import scrapy
import re
from sohu.items import SohuItem
class SohuSpider(scrapy.Spider):
    #phn = 0
    name = "sohu"
    
    start_urls = ["http://esf.focus.cn/sh/realtors/?page=-"]

    npages = 4140
    
    for i in range(1, npages):
        start_urls.append("http://esf.focus.cn/sh/realtors/?page="+str(i)+"")
    
    
    
    def parse(self, response):
        for agent in response.xpath('//div[@class="realtor-info"]'):
            item = SohuItem()
            item['name'] = agent.xpath('.//a[@class="realtor-info-name"]/text()').extract_first()
            item['company'] = agent.xpath('.//div[@class="rcompany"]//span/text()').extract()[1] 
            listR = agent.xpath('.//div[@class="rparks"]//text()').extract()
            predict = str(listR[0]) + str(listR[1]) + str(listR[2])
            listR = predict + "/".join([str(listR[i]) for i in range(3, len(listR)-1)])
            listR = listR.replace('\n',"").replace(" ","").replace("//","/")
            item['region'] = listR
            reId = agent.xpath('.//a[@class="realtor-info-name"]/@href').extract_first().strip()
            reId = str(reId)
            reId = re.findall('[1-9]\d*', reId)[0]
            href ="http://esf.focus.cn/api/getVirtualPhone?realtorId="+reId+"&ecoCityId=73&call_url=.html"
            yield scrapy.Request(href, meta={'item':item}, callback=self.parse_phone)
            
            #yield item

    def parse_phone(self, response):
        #item = SohuItem()
        #global phn
        item = response.meta['item']
        phn = response.body
        phn = str(phn)
        phn = re.findall(r"1\d{10}",phn)
        item['phone'] = phn
        return item
