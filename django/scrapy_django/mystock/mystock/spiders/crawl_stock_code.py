import scrapy
import os
import re
import time
import random


from pymongo import MongoClient


conn = MongoClient('127.0.0.1', 27017)
db = conn.mydb_stock  #连接mydb数据库，没有则自动创建
my_set=db.code_set


class Crawl_stock_code(scrapy.Spider):
    name = "crawl_stock_code"


    def start_requests(self):
        my_set.remove({})
        urls = [
            'http://quote.eastmoney.com/stocklist.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.crawl_stock_prase)


    def crawl_stock_prase(self,response):
        urls=response.xpath('//div[@class="quotebody"]//a[@target="_blank"]//@href').extract()
        num=0
        for url in urls:
            stock_code =re.findall(r"[s][hz]\d{6}", url)[0]
            if (re.match( r'sh60', stock_code, re.M|re.I) or re.match( r'sz00', stock_code, re.M|re.I)):
                my_set.insert({"num":num,"stock_code":stock_code})
                num =num+1
        print('完成第一 条爬虫了哦哦哦哦哦哦哦哦哦哦哦哦')        
            
                
           






