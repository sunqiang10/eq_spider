# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
class EqspiderItem(scrapy.Item):
    Cata_id = scrapy.Field()
    Eq_type = scrapy.Field()
    O_time = scrapy.Field()
    Lat = scrapy.Field()
    Lon = scrapy.Field()
    geom = scrapy.Field()#POINT(73.53 38.37)
    Depth = scrapy.Field()
    M = scrapy.Field()
    Location_cname = scrapy.Field()
    is_create_pic = scrapy.Field()