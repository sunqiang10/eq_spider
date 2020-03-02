# -*- coding: utf-8 -*-
import scrapy
import time
#导入item包
from eqSpider.items import EqspiderItem
# from scrapy.linkextractors import LinkExtractor
import datetime

class JobPositionSpider(scrapy.Spider):
    name = 'job_position'
    allowed_domains = ['news.ceic.ac.cn']
    tt = int(time.time())
    start_urls = ['http://news.ceic.ac.cn/index.html?time=' + str(tt)]
    #爬取的方法
    def parse(self, response):
        item = EqspiderItem()
        # link = LinkExtractor(restrict_css='table.news-table > td')
        # links = link.extract_links(response)
        # print(type(links))      
        for trText in response.xpath('//table[@ class="news-table"]/tr'): 
            text = trText.xpath('./td/text()').extract() 
            if(len(text)>0):
                dateTime_p=datetime.datetime.strptime(text[1],'%Y-%m-%d %H:%M:%S')
                item['Cata_id'] ='CE'+ text[1][0:16].replace("-", " ").replace(":", " ").replace(" ", "")
                item['Eq_type'] =0
                item['M'] = text[0]
                item['O_time'] = dateTime_p
                item['Lat'] = text[2]
                item['Lon'] = text[3]
                item['Depth'] = text[4]
                item['is_create_pic'] = 0
                item['Location_cname'] =trText.xpath('./td/a/text()').get()
                item['geom'] ='POINT('+text[3]+' '+text[2]+')'
                yield item