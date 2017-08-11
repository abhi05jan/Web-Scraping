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