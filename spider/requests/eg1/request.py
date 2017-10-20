import requests
import os
from bs4 import BeautifulSoup
#import re


url='http://www.58pic.com/tupian/JPGtupian-0-0-1.html'
r =requests.get(url=url)


#使用beautifulsoup解析字符串
soup = BeautifulSoup(r.content,'html.parser')
image_urls = soup.find_all('a','thumb-box')


#使用正则表达式查找字符串
#image_urls = re.findall(r'src="(\S+)"', re.findall(r'class="thumb-box"(.*)', r.text)[0])
#print(image_urls)

try:
    for x in image_urls:
        image_url= x.img['src']

        image = requests.get(image_url,stream=True)
        if image.status_code ==200:
            filename = image_url.split('/')[-1]
            filename ='%s.jpg'%filename

            with open("jpg/"+filename, 'wb') as fd:
                for data in image:
                    fd.write(data)
except ConnectionError:
    exit_after_echo("Network connection failed")

