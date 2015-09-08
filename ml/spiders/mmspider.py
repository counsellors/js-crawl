# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import logging

from ml.items import MlItem


class MmspiderSpider(CrawlSpider):
    name = 'mmspider'
    allowed_domains = ['baidu.com']
    start_urls = ['http://xiangce.baidu.com/picture/album/list/3474ef1140d96ffc38d86938912516c6d12fca36']

    rules = (
        Rule(LinkExtractor(allow=r'xiangce\.baidu\.com/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = MlItem()
        picSigns = response.selector.re("picSign:\s+'([0-9a-z]+)',")
        for x in picSigns:
            logging.warning(x)

        #logging.warning("This is a warning %s"%response.body)
        # '//*[@id="tile3effd4e929ab6700491a0314952456f26a14f627"]/div/a[1]'
        #item['image_urls'] = ''+response.xpath('//a[@class="img-container"]/@href').extract()

            #item['url'] = ''+response.xpath('//a[@class="img-container"]/@href').extract()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        yield item
