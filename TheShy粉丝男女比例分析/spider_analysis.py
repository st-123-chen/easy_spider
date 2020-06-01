import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import pandas as pd




import csv
filename = 'E:\爬虫项目\weibospider\spider.CSV'

m = 0
n = 0
s = 0
xiaoliang ={}
with open('E:\爬虫项目\TheShy粉丝男女比例分析\spider.CSV',encoding='utf-8') as f:    #文件的绝对路径
    reader = csv.reader(f)
    # print(reader)
    # header = next(reader)   #使读取CSV文件中不包含表头
    # print(header)
    for i in reader:
        # xiaoliang[int(i[0])] = int(i[1])
        for j in i:
            if j == "f":
                m+=1
            if j == "m":
                n+=1
            else:
                s+=1
            # xiaoliang[int(i[0])] = int(i[1])
#
# print(m,n,s)

        # labels = ['MALE', 'FEMALE', 'OTHERS']
labels = ['FEMALE','MALE' ]
# 绘图显示的标签
values = [m,n]
colors = ['y', 'm']
explode = [0, 0.1]
# 旋转角度
plt.title("TheShy", fontsize=25) # 标题
plt.pie(values, labels=labels, explode=explode, colors=colors,
        startangle=180,
        shadow=True, autopct='%1.1f%%')
plt.axis('equal')
plt.show()
