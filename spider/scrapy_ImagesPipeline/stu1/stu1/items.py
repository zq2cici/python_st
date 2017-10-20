# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Stu1Item(scrapy.Item):
# 	define the fields for your item here like:
#   item is dictionary-like: {'image_urls': ,'images': ,'image_paths': }
   image_urls = scrapy.Field()
   images = scrapy.Field()
   image_paths = scrapy.Field()
   
