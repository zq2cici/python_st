# coding:utf-8
'''
from scrapy import cmdline
print("执行第一条虫了啊啊啊啊啊啊啊啊啊啊啊啊啊")
cmdline.execute("scrapy crawl crawl_stock_code".split())
print("执行第二条虫了啊啊啊啊啊啊啊啊啊啊啊啊啊")
cmdline.execute("scrapy crawl crawl_ip".split())
print("执行第三条虫了啊啊啊啊啊啊啊啊啊啊啊啊啊")
cmdline.execute("scrapy crawl mystock".split())
'''
import sys  
import os  
import time  

try:
    print("执行第一条虫了啊啊啊啊啊啊啊啊啊啊啊啊啊")
    os.system("scrapy crawl crawl_stock_code")  
    time.sleep(5)  
    print("执行第2条虫了啊啊啊啊啊啊啊啊啊啊啊啊啊")
    os.system("scrapy crawl crawl_ip")  
    time.sleep(5)  
    print("执行第3条虫了啊啊啊啊啊啊啊啊啊啊啊啊啊")
    os.system("scrapy crawl mystock")
except SyntaxError:
    print('产生错误，退出系统')





