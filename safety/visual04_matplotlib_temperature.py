# # -*- coding: utf-8 -*-
# # @Time    : 2020/8/27 9:43
# # @Author  : 面包狗
# # @Email   : 3034221968Qqq.com
# # @File    : visual04_matplotlib_temperature.py
# # @Software: PyCharm
#
# from matplotlib import pyplot as plt
# plt.rcParams['font.sans-serif'] = [u'SimHei']
# plt.rcParams['axes.unicode_minus'] = False
#
#
# y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
# y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]
#
# x_3 = range(1,32)
# x_10 = range(51,82)
#
# # 设置图行大小
# plt.figure(figsize=(20,8),dpi=80)
#
# # 使用scatter方法绘制的散点图，和之前绘制折线土地唯一区别
# plt.scatter(x_3,y_3,label="三月份")
# plt.scatter(x_10,y_10,label="十月份")
#
# # 调整x轴的刻度
# _x = list(x_3)+list(x_10)
# _xtick_lables = ["三月{}日".format(i) for i in x_3]
# _xtick_lables += ["十月{}日".format(i-50) for i in x_10]
# plt.xticks(_x,_xtick_lables,rotation=90)
#
# # 添加图例
# plt.legend(loc="upper left")
#
# # 添加描述信息
# plt.xlabel("时间")
# plt.ylabel("温度")
# plt.title("标题")
#
# # 展示
# plt.show()


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import datetime  as dt
diyi = pd.read_excel('附件_一季度.xlsx')

ys = diyi[diyi['水表名']=='浴室']
ss = diyi[diyi['水表名']=='XXX第一学生宿舍']
st = diyi[diyi['水表名']=='XXX第一食堂']
ws = diyi[diyi['水表名']=='XXX污水处理']
jd = diyi[diyi['水表名']=='XXXK酒店']
x1 =ys['采集时间']
x2 =ss['采集时间']
x3 =st['采集时间']
x4 =ws['采集时间']
x5 =jd['采集时间']
y1= ys['当前读数']
y2=ss['当前读数']
y3=st['当前读数']
y4=ws['当前读数']
y5=jd['当前读数']
plt.figure(figsize=(20,8),dpi=80)
plt.plot(x2,y2,label='宿舍')
plt.plot(x1,y1,label='浴室')
plt.plot(x3,y3,label='食堂')
plt.plot(x4,y4,label='污水处理')
plt.plot(x5,y5,label='酒店')

plt.show()