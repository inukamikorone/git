# -*- coding: utf-8 -*-
# @Time    : 2020/8/26 16:01
# @Author  : 面包狗
# @Email   : 3034221968Qqq.com
# @File    : visual01_matplotlib.py
# @Software: PyCharm

import numpy as np
from matplotlib import pyplot as plt
import random
import matplotlib

# 设置字体
# font = {    'family' : 'monospace',
#             'weight' : 'bold',
#             'size'   : 'larger'}
#
# matplotlib.rc("font",**font)


plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

plt.figure(figsize=(20, 8), dpi=80)

plt.plot(x, y)

_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i-60) for i in range(60)]
plt.xticks(list(x)[::3], _xtick_labels[::3],rotation=90)

# 添加描述信息
plt.xlabel("时间")
plt.ylabel("温度 单位(℃)")
plt.title("10点到12点每分钟气温变化情况")

plt.show()
