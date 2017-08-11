# -*- coding: utf-8 -*-
import scrapy
from scrapytutorial.items import ScrapyTutorialItem
import csv


class FlipkartSpider(scrapy.Spider):
    name = "flipkart"
    allowed_domains = ["www.flipkart.com"]

    def start_requests(self):
        for i in xrange(1, 3394):
            #yield self.make_requests_from_url("https://www.flipkart.com/search?q=apple&otracker=start&as-show=on&as=off")
            yield self.make_requests_from_url("https://www.flipkart.com/search?q=samsung&otracker=start&as-show=on&as=off")
    def parse(self, response):
        for item in response.css('div._3liAhj'):
            product = ScrapyTutorialItem()
            product['pid'] = item.css('::attr(data-iid)').extract()
            name = item.css('div.pu-title > a::text').extract()
            #product['name'] = item.xpath('.//a[contains(@class,"_2cLu-l")]/../@href').extract()
            product['name'] = item.xpath('.//a[@class="_2cLu-l"]/text()').extract()

            
            #product['link'] = item.css('div.pu-title > a::attr(href)').extract()
            product['price'] = item.xpath('.//div[contains(@class,"_1vC4OE")]/text()').extract()
            product['Mprice'] = item.xpath('.//div[@class="_3auQ3N"]/text()').extract()
            product['Rating'] = item.xpath('.//div[contains(@class,"hGSR34 _2beYZw")]/text()').extract()
            product['Reviews'] = item.xpath('.//span[contains(@class,"_38sUEc")]/text()').extract()
            product['Features'] = item.xpath('.//div[contains(@class,"_2-riNZ")]/ul/li').extract()


            yield product