# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
#
#
class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
    image_urls = scrapy.Field()  # 保存图片地址
    images = scrapy.Field()  # 保存图片的信息

class DouBanItem(scrapy.Item):
    title = scrapy.Field()
    grade = scrapy.Field()
    commentary = scrapy.Field()
    image_urls = scrapy.Field()  # 保存图片地址
    images = scrapy.Field()  # 保存图片的信息