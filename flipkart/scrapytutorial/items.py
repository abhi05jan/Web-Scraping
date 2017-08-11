# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
#from scrapy_tutorial.items import ScrapyTutorialItem

class ScrapyTutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # new code below:
    pid = scrapy.Field()
    name = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    Mprice = scrapy.Field()
    Rating = scrapy.Field()
    Reviews = scrapy.Field()
    Features = scrapy.Field()

