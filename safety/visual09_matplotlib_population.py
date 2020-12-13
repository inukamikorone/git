# -*- coding: utf-8 -*-
# @Time    : 2020/8/27 15:26
# @Author  : 面包狗
# @Email   : 3034221968Qqq.com
# @File    : visual09_matplotlib_population.py
# @Software: PyCharm
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False

interval = [0,5,10,15,20,25,30,35,40,45,60,90]
width = [5,5,5,5,5,5,5,5,5,15,30,60]
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]


# 设置图形大小
plt.figure(figsize=(20,8),dpi=80)

plt.barh(interval,quantity,width)

# _x = [i -0.5 for i in range(12)]
# _xtick_labels = interval
# plt.xticks(_x,_xtick_labels)
plt.show()