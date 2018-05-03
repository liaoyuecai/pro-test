# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import DmozItem
import urllib2


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.org"]
    start_urls = [
        "https://movie.douban.com/top250"
    ]

    number = 0

    def parse(self, response):
        infos = response.xpath(".//div[@class='item']")

        # imgs = response.xpath(".//img//@src").extract()
        # for i in imgs:
        #     binary_data = urllib2.urlopen(i).read()
        #     temp_file = open('C:/Users/Administrator/Desktop/test/ccc.jpg', 'wb')
        #     temp_file.write(binary_data)
        #     temp_file.close()

        # file = open('C:/Users/Administrator/Desktop/douban_test.txt', 'a')
        folder = 'C:/Users/Administrator/Desktop/test/'
        file = open('C:/Users/Administrator/Desktop/douban_test.txt', 'a+')
        title = ''
        for info in infos:
            # item = DmozItem()
            title = info.xpath(".//span[@class='title']//text()").extract()[0].encode('utf-8')
            # item['image_urls'] = info.xpath(".//div[@class='pic']//a//img//@src").extract()
            # yield item
            img_url = info.xpath(".//div[@class='pic']//a//img//@src").extract_first().encode('utf-8')
            binary_data = urllib2.urlopen(img_url).read()
            save_url = folder + title + r'.'+img_url.split('.')[-1]
            temp_file = open(save_url.decode('utf-8'), 'wb')
            temp_file.write(binary_data)
            temp_file.close()
            file.write(title)
            file.write('\n')
            file.write('评分:')
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
