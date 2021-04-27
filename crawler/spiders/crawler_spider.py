# -*- coding: UTF-8 -*-

from scrapy import Spider
from scrapy.selector import Selector
from crawler.items import CrawlerItem
import json


class CrawlerSpider(Spider):
    name = "test"
    # List your urls to crawl here!!!
    start_urls = [
        "https://vneconomy.vn/ong-vu-tien-loc-lan-song-fdi-the-he-moi-khong-chay-theo-so-luong-quy-mo-646514.htm",
        "https://vneconomy.vn/nguy-co-bi-kiem-soat-dinh-gia-cua-ant-group-co-the-chi-dang-29-ty-usd-thay-vi-320-ty-646521.htm",
        "https://vneconomy.vn/giai-ma-nguon-con-cat-lo-chung-cu-cao-cap-ha-noi-ca-ty-dong-moi-can-646061.htm"
    ]

    def parse(self, response):
        # yield {"title":response.css('div.detail__author::text')[0].get()}
        for t in response.css('header.detail__header'):
            yield {"URL": response.request.url,
                   "Title": t.css('h1.detail__title::text').get(),
                   "Author": t.xpath('//div[@class="detail__author"]/strong/text()').get(),
                   "Date": t.css('div.detail__meta::text').get()}
          # print(title.css('::text').get())
        # item['Author'] = Selector(response).xpath(
        #     'span[@class="ReferenceSourceTG"]/text()').extract_first()

        # yield item
