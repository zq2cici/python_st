'''
如何添加数据标签
使用zip()函数返回数据标签的位置
使用text() 添加文本标签

'''

from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np


x = np.arange(4)
y1 = [1, 2, 5, 3]
y2 = [4, 5, 4, 2]

x_label =['第一滴血', '第二滴血', '第三滴血', '第四滴血']

def millions(x, pos):
    'The two args are the value and tick position'
    return '$%1.1f人' % (x * 100)
formatter = FuncFormatter(millions)


#fig, ax = plt.subplots(figsize =(6,6))
fig, ax = plt.subplots()
#设置Y轴刻度格式显示‘人’
ax.yaxis.set_major_formatter(formatter)

#画柱状图
b1=plt.bar(x, y1,width=0.35,color = 'g')
b2=plt.bar(x, y2,width=0.35,color = 'b',bottom=y1)

#添加标题
plt.title('电影评价')
#设置x轴刻度
plt.xticks(x, x_label,size='small',rotation=30)
#设置x，y轴标签
plt.ylabel('观看人数')
plt.xlabel(u'影片')

#添加数据标签
for a,b in zip(x,y1 ):
    plt.text(a+0.25, b+0.05, b*100,ha='center',va='bottom',color='g',fontsize=7)

for a,b,c in zip(x,y1,y2 ):
    plt.text(a+0.25, b+c+0.05, c*100,ha='center',va='bottom',color='b',fontsize=7)


#添加图例
plt.legend([b1,b2],['值得看','不值得看'],loc='upper right',fontsize=10)
#添加网格线
plt.grid()
plt.show()