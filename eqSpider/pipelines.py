# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import copy
from eqSpider.model import MysqlOpt
class EqspiderPipeline(object):
    def process_item(self, item, spider):    	
    	self.resultList.append(copy.deepcopy(item))
    	return item
    def open_spider(self, spider):
    	self.resultList = []    	
    def close_spider(self, spider):
    	self.myConn = MysqlOpt.MysqlOpt()
    	self.resultList.reverse()
    	for item in self.resultList:
    		print("Location_cname:",item['Location_cname'])
    		self.myConn.insert(item,'cata7days')
    	self.myConn.close_session()