# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from tutorial.items import DmozItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "https://blog.csdn.net/liaoyuecai"
    ]

    def parse(self, response):
        # for sel in response.css('.article-item-box.csdn-tracking-statistics'):
        title = response.xpath('.//h4/a')
        # print(len(title))
        # a= title[1]
        # print(title[1])

        for t in title:
            print(t.xpath('.//text()').extract_first()[2].encode('utf-8'))
            next_page = t.xpath('.//@href').extract_first()
            self.test(next_page)
            yield Request(next_page, callback=self.parse_url2)
        # item = DmozItem()
        # item['title'] = sel.xpath('a/text()').extract()

    #     item['link'] = sel.xpath('a/@href').extract()
    #     item['desc'] = sel.xpath('text()').extract()
    #     yield item
    # filename = "C:/Users/Administrator/Desktop/test.txt"
    # # fo = open(filename, 'w')
    # # fo.write(response.xpath('//title'))
    # yield Request(url, callback=self.parse)

    def test(self,next_page):
        yield  Request(next_page, callback=self.parse_url2)

    def parse_url2(self, response):
        item = DmozItem()  # 实例化一个item
        selector = Selector(response)  # 构造一个选择器
        title = selector.xpath("//div[@class='title']/h1/text()").extract()[0]  # 标题
        content = selector.xpath("//div[@id='content']//text()").extract()  # 内容
        # item['article_url'] = response.url
        # item['article_title'] = title
        # item['article_content'] = "".join(content)
        yield item

    def parse_item(self, response):
        print("start")
        print(response.xpath('.//h6/text()').extract())
