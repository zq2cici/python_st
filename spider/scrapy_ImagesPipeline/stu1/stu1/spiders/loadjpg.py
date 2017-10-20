import scrapy
import stu1.items
from stu1.items import Stu1Item
class LoadjpgSpider(scrapy.Spider):
    name = 'loadjpg'
#    start_urls = ['http://jandan.net/pic/page-{}'.format(i) for i in range(1,5)]
    start_urls = ['http://www.58pic.com/tupian/JPGtupian-0-0-1.html']

    def parse(self, response):
        item=Stu1Item()
        image_urls=response.css('.thumb-box > img::attr(src)').extract()
        item['image_urls']=[(i)for i in image_urls]
        yield item  #爬回的图片url传递给图片管道
   
        