# -*- coding: utf-8 -*-
import scrapy
from scrapytutorial.items import ScrapyTutorialItem
import csv

class AmazonSpider(scrapy.Spider):
    name = "amazon"
    allowed_domains = ["www.amazon.in"]
    # start_urls = ["http://www.amazon.in/Smartphones-Basic-Mobiles-Accessories/s?ie=UTF8&page=1&rh=n%3A1389432031"]

    def start_requests(self):
        for i in xrange(2, 69):
            yield self.make_requests_from_url("http://www.amazon.in/Smartphones-Basic-Mobiles-Accessories/s?ie=UTF8&page=%d" % (i) +"&rh=n%3A1389432031")
            # def start_requests(self):
    #     for i in xrange(1,69):
    #         yield self.make_requests_from_url("http://www.amazon.in/Smartphones-Basic-Mobiles-Accessories/s?ie=UTF8&page=%d&rh=n:1389432031" % i)

    def parse(self, response):
        for item in response.css('#s-results-list-atf > li.s-result-item'):
            product = ScrapyTutorialItem()
            product['pid'] = item.css('::attr(data-asin)').extract()
            product['name'] = item.xpath('.//h2/text()').extract()
            product['link'] = item.xpath('.//span[contains(@class,"s-price")]/../@href').extract()
            #price = item.css('div > div:nth-child(3) > div:nth-child(1) > a > span.a-color-price::text').extract()
            product['price'] = item.xpath('.//span[contains(@class,"s-price")]/text()').extract()

            




            yield product



