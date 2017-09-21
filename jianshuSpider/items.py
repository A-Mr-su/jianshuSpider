# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 文章内容
    article = scrapy.Field()
    # 文章链接
    link = scrapy.Field()
    # pass
