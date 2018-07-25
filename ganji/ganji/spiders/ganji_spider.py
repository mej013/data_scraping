#!/usr/bin/python
#coding:utf-8
import scrapy 
import re
from ganji.items import GanjiItem

class GanjiSpider(scrapy.Spider):
    name = "ganji"

    start_urls = ["http://sh.ganji.com/fang/agent/o0/"]

    npages = 59

    for i in range(1, npages+1):
        start_urls.append("http://sh.ganji.com/fang/agent/o"+str(i)+"")

    def parse(self, response):
        for href in response.xpath('//a[@class="f-list-item"]/@href').extract():
            url = "http://sh.ganji.com" + href
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        item = GanjiItem()

        item['name'] = response.xpath('//div[@class="f-crumbs"]//span/text()').extract()
        a = response.xpath('//title/text()')
        a = str(a)
        item['phone'] = re.findall(r"1\d{10}",a) 
        yield item
