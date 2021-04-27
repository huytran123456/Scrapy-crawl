# -*- coding: UTF-8 -*-

from scrapy import Spider
from scrapy.selector import Selector
from crawler.items import CrawlerItem
import json
from scrapy.http import Request
import scrapy
class CrawlerSpider(Spider):
    name = "test"
    # List your urls to crawl here!!!
    base_Url = "https://vneconomy.vn"
    start_urls = [
        "https://vneconomy.vn/ong-vu-tien-loc-lan-song-fdi-the-he-moi-khong-chay-theo-so-luong-quy-mo-646514.htm",

    ]
    allowed_domains = ["vneconomy.vn"]
    def parse(self, response):
        # yield {"title":response.css('div.detail__author::text')[0].get()}
        for t in response.css('header.detail__header'):
            # self.content(t)
            yield {"URL": response.request.url,
                   "Title": t.css('h1.detail__title::text').get(),
                   "Author": t.xpath('//div[@class="detail__author"]/strong/text()').get(),
                   "Date": t.css('div.detail__meta::text').get()}
        for href in response.xpath('//article[@class="story story--featured"]/figure[@class="story__thumb"]/a/@href').extract():
            #print(self.base_Url+href)
            yield scrapy.Request(self.base_Url+href,callback=self.content)
            # yield {
            #     "URL": self.base_Url + href
            # }
           # print(title.css('::text').get())
        # item['Author'] = Selector(response).xpath(
        #     'span[@class="ReferenceSourceTG"]/text()').extract_first()

        # yield item
    def content(self, response):
        for t in response.css('header.detail__header'):
            # self.content(t)
            yield {"URL": response.request.url,
                   "Title": t.css('h1.detail__title::text').get(),
                   "Author": t.xpath('//div[@class="detail__author"]/strong/text()').get(),
                   "Date": t.css('div.detail__meta::text').get()}
