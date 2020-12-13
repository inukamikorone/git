# -*- coding: utf-8 -*-
# @Time    : 2020/8/26 20:49
# @Author  : 面包狗
# @Email   : 3034221968Qqq.com
# @File    : visual02_matplotlib_age_trends.py
# @Software: PyCharm

from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False

y = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
x = range(11,31)

# 设置图形大小
plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y)

# 设置刻度
_xtick_lable = ["{}岁".format(i) for i in x]
plt.xticks(x,_xtick_lable)
plt.ylabel(range(0,9))

# 绘制网格
plt.grid(alpha=0.4)

# 显示
plt.show()