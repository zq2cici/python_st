#coding=utf-8


import scrapy
import os
import re
import time
import random
import requests

from scrapy.selector import Selector

from pymongo import MongoClient





conn = MongoClient('127.0.0.1', 27017)
db = conn.mydb_stock  #连接mydb数据库，没有则自动创建
my_set=db.ip_set#使用test_set集合，没有则自动创建


#my_set.remove({})

class Crawl_ip(scrapy.Spider):
    name = "crawl_ip"
    
    
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"}

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
        my_set.remove({})
        urls = [
            "http://www.xicidaili.com/nn/{}".format(i)for i in range(1,3)
#            "http://www.xicidaili.com/nn/1",
        ]
        headers={
            'User-Agent':random.choice(self.user_agent_list),
        }  
        for url in urls:
            print(url)
            print('你大爷达到 大大法法')
            yield scrapy.Request(url=url, headers =headers,callback=self.crawl_ips_prase)
            
    def judge_ip(self, ip, port,poxy_type):
        #判断ip是否可用
        http_url = "http://www.baidu.com"
#        proxy_url = "http://{0}:{1}".format(ip, port)
        proxy_url = "{2}://{0}:{1}".format(ip, port,poxy_type)
        try:
            proxy_dict = {
                "http":proxy_url,
                
            }
            time.sleep(0.1)
            response = requests.get(http_url, proxies=proxy_dict,timeout=0.05)
        except Exception as e:
            print ("invalid ip and port")
            return False
        else:
            code = response.status_code
            if code >= 200 and code < 300:
                print ("effective ip")
                return True
            else:
                print  ("invalid ip and port")
                return False            
    def crawl_ips_prase(self,response):
        #爬取西刺的免费ip代理
        
#        for i in range(1568):
#            re = requests.get("http://www.xicidaili.com/nn/{0}".format(i), headers=headers)
        print('aadhffhakhafhadjfhafhsajfhasjfhsajdfhsj')
        selector = Selector(text=response.text)
        all_trs = selector.css("#ip_list tr")

        ip_list = []
        for tr in all_trs[1:]:
            speed_str = tr.css(".bar::attr(title)").extract()[0]
            if speed_str:
                speed = float(speed_str.split("秒")[0])
            all_texts = tr.css("td::text").extract()

            ip = all_texts[0]
            port = all_texts[1]
            proxy_type = all_texts[5]

            ip_list.append((ip, port, proxy_type, speed))

        for ip_info in ip_list:
#            if self.judge_ip(ip_info[0],ip_info[1],ip_info[2]):
#                my_set.insert({"ip":ip_info[0],"port":ip_info[1],"proxy_type":ip_info[2].lower(),"speed":ip_info[3]})
            my_set.insert({"ip":ip_info[0],"port":ip_info[1],"proxy_type":ip_info[2].lower(),"speed":ip_info[3]})    
                
        print('完成第二条虫了哦哦哦哦')  

        
            



                
'''                
class GetIP(object):
    def delete_ip(self, ip):
        #从数据库中删除无效的ip
        my_set.remove({'ip':ip})
        return True

    def judge_ip(self, ip, port):
        #判断ip是否可用
        http_url = "http://www.baidu.com"
        proxy_url = "http://{0}:{1}".format(ip, port)
        try:
            proxy_dict = {
                "http":proxy_url,
            }
            response = requests.get(http_url, proxies=proxy_dict)
        except Exception as e:
            print ("invalid ip and port")
            self.delete_ip(ip)
            return False
        else:
            code = response.status_code
            if code >= 200 and code < 300:
                print ("effective ip")
                return True
            else:
                print  ("invalid ip and port")
                self.delete_ip(ip)
                return False


    def get_random_ip(self):
        #从数据库中随机获取一个可用的ip
#        aa=my_set.find().limit(1).skip(random.randint(0,22))
        len= my_set.find().count()
        print('记录长度为  %d'%len)
        for ip_info in my_set.find().limit(1).skip(random.randint(0,len)):
            print('年地方大家发就发')
            print(ip_info)
        
        
        
        for ip_info in my_set.find():
            ip = ip_info['ip']
            port = ip_info['port']

            judge_re = self.judge_ip(ip, port)
            if judge_re:
                return "http://{0}:{1}".format(ip, port)
            else:
                return self.get_random_ip()



if __name__ == "__main__":
    get_ip = GetIP()
    get_ip.get_random_ip()
    
'''   
    
    
    
    