#!/usr/bin/python
#coding:utf-8
import scrapy
import re
from anjuke.items import AnjukeItem

class AnjukeSpider(scrapy.Spider):
    name = "anjuke"
 #   header = {
#'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
#}
    start_urls = ["https://shanghai.anjuke.com/tycoon/"]

    npages = 115
    
    for i in range(1, npages+1):
        start_urls.append("https://shanghai.anjuke.com/tycoon/p"+str(i)+"")

    def parse(self, response):
        for href in response.xpath('//div[@class="jjr-itemmod"]/@link'):
            url = href.extract()
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        item = AnjukeItem()

        str_nam = response.xpath('//div[@class="firstline clearfix"]//a/text()').extract_first().strip()
        str_nam = str(str_nam)
        str_nam = str_nam.split("的")[0]
        #str_nam = str_nam.replace('\\r','').replace('\\n','').replace('\\t','')
        #str_nam = str_nam.strip()
        item['name'] = str_nam
        str_phn = response.xpath('//title/text()').extract()
        str_phn = str(str_phn)
        item['phone'] = re.findall(r"1\d{10}", str_phn)
        yield item
