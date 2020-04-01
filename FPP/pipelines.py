# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from FPP.items import FppItem
import pymysql



class FppPipeline(object):


    def __init__(self):
        self.connect = pymysql.connect(
            host = 'localhost',
            port =    ,
            user =   ,
            passwd =    ,
            db = 'baiduItem' ,
            charset =  'utf8'
        )

        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        insert_sql = "INSERT INTO job(para) VALUES('%s')" % (item['para'])
        self.cursor.execute(insert_sql)
        self.connect.commit()

    def clsoe_spider(self):
        self.cursor.close()
        self.connect.close()
