# -*- coding: utf-8 -*-
import scrapy
from FPP.items import FppItem
from scrapy import Request



class BaiDuItem(scrapy.Spider):
    name = 'baiduitem'
    #start_url = ''

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }

    def start_requests(self):
        url = 'https://baike.baidu.com/item/%E7%8E%89%E7%B1%B3/18401'
        yield Request(url, headers=self.header)

    def parse(self, response):
        infos = []
        items = FppItem()
        paras = response.xpath('//div[@class="main-content"]/div[@class="para"]')
        #print(type(paras))
        #print(paras)
        for para in paras:
            #print(type(para))
            #print(para)
            info = para.xpath('string(.)').extract()[0]
            infos.append(info)
            print('---------------------')
            print(info)
            print('------------------------')
        print(infos)
        items['para'] = infos
        yield items









