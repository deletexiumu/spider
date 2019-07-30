# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CookiespiderItem(scrapy.Item):
    pass


class PostItem(scrapy.Item):
    """
    帖子信息定义
    """
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    body_size = scrapy.Field()
    price = scrapy.Field()
    server = scrapy.Field()
    detail_url = scrapy.Field()
    photo = scrapy.Field()

