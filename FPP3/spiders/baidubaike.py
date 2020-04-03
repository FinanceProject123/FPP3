# -*- coding: utf-8 -*-
import scrapy
from FPP3.items import BaiduBaike
from scrapy import Request


class BaiDuItem(scrapy.Spider):
    name = 'baiduitem'
    # start_url = ''

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }

    def start_requests(self):
        url = 'https://baike.baidu.com/item/玉米/18401'
        yield Request(url, headers=self.header)

    def parse(self, response):
        infos = []
        items = []
        item = BaiduBaike()
        all_text = response.xpath(
            "//div[@class='main-content']/div[contains(@class, 'para-title') or contains(@class ,'para')]")
        print(all_text)
        i,flag = 0,False
        # 将数据按照标题存入item
        # while i<len(all_text):
        #     if flag:
        #         items.append(item)
        #         flag = False
        #     else:
        #         item = BaiduBaike()
        #         item['title_h1'] = all_text[i].xpath()
        # for para in paras:
        #     # print(type(para))
        #     # print(para)
        #     info = para.xpath('string(.)').extract()[0]
        #     infos.append(info)
        #     print('---------------------')
        #     print(info)
        #     print('------------------------')
        # print(infos)

        yield item

    def second_parse(self, response):
        pass
