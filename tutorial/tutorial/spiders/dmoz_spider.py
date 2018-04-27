# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import DmozItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "https://blog.csdn.net/liaoyuecai"
    ]

    def parse(self, response):
        # for sel in response.css('.article-item-box.csdn-tracking-statistics'):
        title = response.xpath('//h4/a/text()').extract()
        for t in title:
            print(t.encode('utf-8'))
        # item = DmozItem()
        # item['title'] = sel.xpath('a/text()').extract()
    #     item['link'] = sel.xpath('a/@href').extract()
    #     item['desc'] = sel.xpath('text()').extract()
    #     yield item
    # filename = "C:/Users/Administrator/Desktop/test.txt"
    # # fo = open(filename, 'w')
    # # fo.write(response.xpath('//title'))
