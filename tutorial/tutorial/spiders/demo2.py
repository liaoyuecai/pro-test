# -*- coding: utf-8 -*-
from scrapy.spider import Spider
from scrapy.selector import Selector
# from tutorial.items import DmozItem
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
        # sel = Selector(response)
        # self.log("begins  % s" % response.url)
        # article_list = sel.css('div.postTitle').xpath('a')
        #
        # # 抓取列表里面的内容也地址后循环抓取列表的内容页面数据
        # for article in article_list:
        #     url = article.xpath('@href').extract()[0]
        #     self.log("list article url: % s" % url)
        title = response.xpath('.//h4/a')
        for t in title:
            print(t.xpath('.//text()').extract_first()[2].encode('utf-8'))
            next_page = t.xpath('.//@href').extract_first()
            # print(next_page)
            # 继续抓取内容页数据
            yield scrapy.Request(next_page, callback=self.parse_content)

        # # 如果有下一页继续抓取数据
        # next_pages = sel.xpath('//*[@id="nav_next_page"]/a/@href')
        # title = response.xpath('.//h4/a')

        # for t in title:
        #     print(t.xpath('.//text()').extract_first()[2].encode('utf-8'))
        #     next_page = t.xpath('.//@href').extract()[0]
        # if next_pages:
        #     next_page = next_pages.extract()[0]
        #     # print next_page
        #     self.log("next_page: % s" % next_page)
        #     # 自己调用自己  类似php 函数的当中的递归
        #     yield scrapy.Request('https://blog.csdn.net/liaoyuecai', callback=self.parse)

    # 内容页抓取
    def parse_content(self, response):
        print(response.xpath(".//h6[@class='title-article']//text()").extract_first())
        str = ''
        for s in response.xpath(".//div[@class='htmledit_views']//text()").extract():
            str += s
        print(str)
        # self.log("detail views: % s" % response.url)

        # 定义好的item  只需要在items 文件中定义抓取过来的数据对应的字段
        # item = DmozItem()

        # xpath 寻找需要在页面中抓取的数据
        # item['link'] = response.url

        # # 正则匹配出文章在cnblog中的id
        # m = re.search(r"([0-9])+", item['link'])
        # if m:
        #     item['aid'] = m.group(0)
        # else:
        #     item['aid'] = 0;
        # item['title'] = response.xpath('//*[@id="cb_post_title_url"]/text()').extract()[0]
        # item['content'] = response.xpath('//*[@id="cnblogs_post_body"]').extract()[0]
        # item['date'] = response.xpath('//*[@id="post-date"]').extract()
        # print item['content']
        # yield item
