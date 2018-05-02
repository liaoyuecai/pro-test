# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import DouBanItem


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.org"]
    start_urls = [
        "https://movie.douban.com/top250"
    ]

    number = 0;

    def parse(self, response):
        infos = response.xpath(".//div[@class='item']")
        # file = open('C:/Users/Administrator/Desktop/douban_test.txt', 'a')
        file = open('C:/Users/Administrator/Desktop/douban_test.txt', 'a+')
        title = ''
        for info in infos:
            # print(info.xpath(".//div[@class='pic']//a//img//@src").extract())
            # item = DouBanItem()
            title = info.xpath(".//span[@class='title']//text()").extract()[0].encode('utf-8')
            # item['title'] = title
            # item['image_urls'] = info.xpath(".//div[@class='pic']//a//img//@src").extract()
            # yield item
            file.write(title)
            file.write('\n')
            file.write('评分')
            file.write(info.xpath(".//div[@class='star']//text()").extract()[2].encode('utf-8'))
            file.write('\n')
            file.write(info.xpath(".//div[@class='star']//text()").extract()[5].encode('utf-8'))
            file.write('\n')
            quote = info.xpath(".//p[@class='quote']//text()").extract()
            if (len(quote) > 0):
                file.write(quote[1].encode('utf-8'))
            file.write('\n')
            file.write('\n')
        file.close()
        if (self.number < 225):
            self.number += 25
            next_url = 'https://movie.douban.com/top250?start=' + bytes(self.number) + '&amp;filter='
            yield scrapy.Request(next_url, callback=self.parse, dont_filter=True)
