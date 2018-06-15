# -*- coding: utf-8 -*-
import scrapy
import os
import re
import time
import random


from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError


#from mystock.spiders.crawl_stock_code import my_set 

from pymongo import MongoClient


conn = MongoClient('127.0.0.1', 27017)
db = conn.mydb_stock  #连接mydb数据库，没有则自动创建
my_set=db.code_set
my_stockdata=db.stock_set


class Mystock(scrapy.Spider):
    name = "mystock"
    save_data ={}
    stock_code_list=[]
    stock_info_url = 'https://gupiao.baidu.com/stock/'

    user_agent_list = [\
        "Mozilla/5.0(Macintosh;IntelMacOSX10_7_0)AppleWebKit/535.11(KHTML,likeGecko)Chrome/17.0.963.56Safari/535.11",\
        "Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50",\
        "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Maxthon2.0)",\
        "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)",\
        "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;SE2.XMetaSr1.0;SE2.XMetaSr1.0;.NETCLR2.0.50727;SE2.XMetaSr1.0)",\
        "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)",\
        "Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1",\
        "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)"
        ]

    def start_requests(self):
        my_stockdata.remove({})
        cnt=0
        for cnt in range(0,3):        
            print('日日日日日日日日日日日')
            
                
            for stock_code in my_set.find({"num":cnt}):
                print(stock_code)
            
            
            time.sleep(2)
            url = self.stock_info_url + stock_code["stock_code"] + ".html"
            print(url)
            
            headers={
                'User-Agent':random.choice(self.user_agent_list),
            }
#                print(headers)
#                yield scrapy.Request(url=url, headers =headers,callback=self.stockDataParse,errback=self.errback_httpbin)
            yield scrapy.Request(url=url, headers =headers,meta={"download_timeout":10},callback=self.stockDataParse)

    def stockDataParse(self,response):

        time.sleep(2)
        print('mystock spider 反回了参数了发达东方大道')
        if response.status == 200 :
            data=response.xpath('//div[@class="stock-bets"]')
            stock_name = response.xpath('//a[@class="bets-name"]//text()')[0].extract().split()[0]
            stock_code =response.xpath('//a[@class="bets-name"]//text()')[1].extract()
            stock_price =response.xpath('//strong[@class="_close"]//text()').extract()
            keyList = response.xpath('//div[@class="bets-content"]//dt/text()').extract()
            valueList = response.xpath('//div[@class="bets-content"]//dd/text()').extract()
                


            if stock_price !=[]:
                stock_data ={}
                for i in range(len(keyList)):
                    stock_data[keyList[i]]=valueList[i]

                self.save_data={"股票名称":stock_name,"股票价格":stock_price[0],"市盈率":stock_data["市盈率"],"市净率":stock_data["市净率"],"每股收益":stock_data["每股收益"]}
                
                my_stockdata.insert(self.save_data)
            
            print(self.save_data)
        
        return
          
    def errback_httpbin(self, failure):
        # log all failures
        self.logger.error(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the failure's type:

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)

'''        
        for stock_code in my_set.find({}).sort({'num':1}):
        for stock_code in my_set.find({}):        
            print('日日日日日日日日日日日')
            
            cnt=cnt+1
            if cnt >5:
                break
                
                
            
            print(stock_code)
            time.sleep(2)
            url = self.stock_info_url + stock_code["stock_code"] + ".html"
            print(url)
            
            headers={
                'User-Agent':random.choice(self.user_agent_list),
            }
                print(headers)
                yield scrapy.Request(url=url, headers =headers,callback=self.stockDataParse,errback=self.errback_httpbin)
            yield scrapy.Request(url=url, headers =headers,meta={"download_timeout":10},callback=self.stockDataParse)
'''

        

        
  
         