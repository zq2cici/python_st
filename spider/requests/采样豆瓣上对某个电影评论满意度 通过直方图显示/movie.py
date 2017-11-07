#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import os
from bs4 import BeautifulSoup

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

url='https://movie.douban.com/subject/22266012/comments'
#url='https://movie.douban.com/subject/22266012/comments?start=20&limit=20&sort=new_score&status=P&percent_type='

class spider(object):
    """docstring for spider"""
    comments={'力荐':0,'推荐':0,'还行':0,'较差':0,'很差':0}

    page =0

    def __init__(self, arg):
        super(spider, self).__init__()
        self.arg = arg

    def get_data(self,movie_url):
        try:
            r =requests.get(url= movie_url,headers={'user-agent': 'Mozilla/5.0'})
            self.data_prase(r)
        except ConnectionError:
            exit_after_echo("Network connection failed")

    def data_prase(self,respon):
        #使用beautifulsoup解析字符串
        soup = BeautifulSoup(respon.content,'html.parser')
        for key in self.comments:
            html = soup.find_all('span',title=key)
            self.comments[key] += len(html)
        self.get_next_page(soup)

    def get_next_page(self,soup):
        html = soup.find_all(class_='next')
#        print(html)
#        print('\n')
        if ('href' in html[0].attrs ) == True:
            next_page_url = url+html[0]['href']
#            print(next_page_url)
            self.page +=1
            if self.page <8:
                self.get_data(next_page_url)

    def save_data(self,datas):

        filename = 'film_comments'
        filename ='%s.txt'%filename

        with open("jpg/"+filename, 'wb') as fd:
            fd.write(str(datas).encode())

    def millions(x, pos):
        'The two args are the value and tick position'
        return '%1.1f人' % (x)
    formatter = FuncFormatter(millions)

    def draw_pic(self,data):
        x_label=[]
        y=[]
        for i in data:
            x_label.append(i)
            y.append(data[i])
        x = np.arange(len(y))

        ax =plt.subplot()
        plt.bar(x, y, color = 'g')

        plt.xlabel('满意度')
        plt.ylabel('人数')

        ax.yaxis.set_major_formatter(self.formatter)
        plt.xticks(x,x_label,size='small',rotation='30')

        sum=0
        percent =[]
        for num in y:
            sum +=num
        for per in y:
            percent.append(per*100/sum)

        for a,b,c in zip(x, y, percent):
            plt.text(a, b+0.05, '{}人 {:.1f}%'.format(b,c))
        plt.show()


if __name__ == '__main__':
    sp = spider(1)
    sp.get_data(url)
    sp.save_data(sp.comments)
    sp.draw_pic(sp.comments)


