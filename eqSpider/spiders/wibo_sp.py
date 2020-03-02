# -*- coding: utf-8 -*-
import scrapy
import json
from urllib.parse import urlencode
#导入item包
from eqSpider.items import EqspiderItem
import re
import datetime
import time
class WiboSpSpider(scrapy.Spider):
    name = 'wibo_sp'
    allowed_domains = ['m.weibo.cn']
    params = {
		'containerid':'231522type=1&t=10&q=#地震快讯#',
		'isnewpage':1,
		'luicode':'10000011',
		'lfid':'231522type=1&q=#地震快讯#',
		'sudaref':'login.sina.com.cn',
		'display':0,
		'retcode':6102,
		'page_type':'searchall'
	}
    start_urls = ['https://m.weibo.cn/api/container/getIndex?'+ urlencode(params)]

    #爬取的方法
    def parse(self, response):
        item = EqspiderItem()
        rs =  json.loads(response.text)
        cards = rs.get('data').get('cards')
        for card in cards:
            mblog = card.get('mblog')            
            if mblog:               
                text = mblog.get('text')
                #print(text)
                pattern = re.compile(r'^.*?(中国地震台网正式测定).*(\d{1,2})月(\d{1,2})日(\d{1,2})时(\d{1,2})分在(.*)\S{2}纬(\d*\.\d{2})度，.*经(\d*\.\d{2})度.*发生(\d*\.\d{1}).*震源深度(\d*).*$')
                match = pattern.match(text)
                if match:
                    # 使用Match获得分组信息
                    # print('***************************************************')
                    # print(str(match.group(1)))
                    # print(str(datetime.datetime.now().year)+"-"
                    #     + str(match.group(2)) +"-"
                    #     + str(match.group(3)) +" "
                    #     + str(match.group(4)) +":"
                    #     + str(match.group(5)))
                    # print(str(match.group(6)))
                    # print(str(match.group(7)))
                    # print(str(match.group(8)))
                    # print(str(match.group(9)))
                    # print(str(match.group(10)))

                    dateTime_p = datetime.datetime.strptime(str(datetime.datetime.now().year)+"-"
                        + str(match.group(2)) +"-"
                        + str(match.group(3)) +" "
                        + str(match.group(4)) +":"
                        + str(match.group(5)),'%Y-%m-%d %H:%M')
              
                    tt = int(time.time())

                    item['O_time'] = dateTime_p
                    dateText = datetime.datetime.strftime(dateTime_p, '%Y%m%d%H%M')
                    item['Cata_id'] = 'CE'+ dateText
                    item['Eq_type'] =0
                    item['Location_cname'] =match.group(6)
                    item['Lat'] = match.group(7)
                    item['Lon'] = match.group(8)
                    item['M'] = match.group(9)                   
                    item['Depth'] = match.group(10)
                    item['is_create_pic'] = 0
                    item['geom'] ='POINT('+match.group(8)+' '+match.group(7)+')'
                    yield item