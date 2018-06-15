# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

'''
class MystockSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(self,s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self,response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self,response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self,response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        print('产生错误了吗。。发得分积分')
        print(spider.name)
        pass

    def process_start_requests(self,start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
'''        
        
        
import random  
import scrapy  
from scrapy import log 
from mystock.spiders.crawl_sici_ip import my_set 

class ProxyMiddleWare(object):         
    def process_request(self,request, spider):
        print('开始抓起了daffodil阿凡达发')
        print(spider.name)
        
        if spider.name == 'mystock':
            '''对request对象加上proxy'''  
            proxy = self.get_random_proxy()  
            print("this is request ip:%s"%proxy)  
            request.meta['proxy'] = proxy          
    def process_exception(self, request, exception, spider):
        print('捕获到异常了巴巴爸爸不不不不不')
        print(spider.name)
        return request
        
        
    def process_response(self, request, response, spider):
        print('抓取回应的阿达的法律')
        print(spider.name)
        print(response.status)
        
        
         # 如果返回的response状态不是200，重新生成当前request对象  
        if response.status != 200:  
            if spider.name == 'mystock':
                proxy = self.get_random_proxy()  
                print("this is response ip:%s"%proxy)  
                # 对当前reque加上代理  
                request.meta['proxy'] = proxy   
                return request         
        return response


    def get_random_proxy(self):  
        '''随机从文件中读取proxy''' 
        len= my_set.find().count()
        for ip_info in my_set.find().limit(1).skip(random.randint(0,len)):
            proxy = ip_info["proxy_type"]+'://'+ip_info['ip']+':'+ip_info['port']
            print('随机获取的ip为 {}'.format(ip_info))
#        proxy = random.choice(proxies).strip()  
        return proxy  


    
        
