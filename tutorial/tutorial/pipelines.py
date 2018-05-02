# -*- coding: utf-8 -*-

import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from tutorial.items import DmozItem


class TutorialPipeline(ImagesPipeline):
    # def process_item(self, item, spider):
    #     return item
    number = 0

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url, meta={'item': item, 'index': item['image_urls'].index(image_url)})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]  # ok判断是否下载成功
        if not image_paths:
            raise DmozItem("Item contains no images")
        # item['image_paths'] = image_paths
        return item

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        url = request.url
        image_guid = request.url.split('/')[-1]
        prefix = image_guid.split('.')[0]
        suffix = image_guid.split('.')[1]
        prefix = bytes(self.number) + "/" + prefix
        self.number += 1
        # filename = u'full/{0[mote_id]}/{1}'.format(item, image_guid)
        return prefix + '.' + suffix
