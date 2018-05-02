# -*- coding: utf-8 -*-
from scrapy.spider import Spider
from scrapy.selector import Selector
from tutorial.items import DmozItem
import scrapy


# 抓取在cnblog中的文章
class CnblogSpider(Spider):
    # 抓取名称 执行命令的时候后面的名称   scrapy crawl cnblog 中的cnblog 就是在这里定义的
    name = 'cnblog'
    allow_domains = ["cnblogs.com"]

    # 定义抓取的网址
    start_urls = [
        'https://blog.csdn.net/liaoyuecai'
    ]

    # 执行函数
    def parse(self, response):
        title = response.xpath('.//h4/a')
        for t in title:
            print(t.xpath('.//text()').extract_first()[2].encode('utf-8'))
            next_page = t.xpath('.//@href').extract_first()
            # print(next_page)
            # 继续抓取内容页数据
            yield scrapy.Request(next_page, callback=self.parse_content)


    # 内容页抓取
    def parse_content(self, response):
        img = response.xpath(".//img[@class='avatar_pic']//@src").extract()
        item = DmozItem()
        item['image_urls'] = img
        print(img)
        print(response.xpath(".//h6[@class='title-article']//text()").extract_first())
        str = ''
        for s in response.xpath(".//div[@class='htmledit_views']//text()").extract():
            str += s
        print(str)
        yield item
