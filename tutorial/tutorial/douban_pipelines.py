# -*- coding: utf-8 -*-

import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from tutorial.items import DouBanItem


class DouBanPipeline(ImagesPipeline):
    # def process_item(self, item, spider):
    #     return item

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            print(image_url)
            yield scrapy.Request('https://avatar.csdn.net/A/5/7/3_u012150179.jpg', meta={'item': item, 'index': item['image_urls'].index(image_url)})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]  # ok判断是否下载成功
        if not image_paths:
            raise DouBanItem("Item contains no images")
        # item['image_paths'] = image_paths
        return item

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        image_guid = request.url.split('/')[-1]
        suffix = image_guid.split('.')[1]
        title = item['title']
        return image_guid
