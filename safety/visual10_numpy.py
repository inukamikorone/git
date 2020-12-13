# -*- coding: utf-8 -*-
# @Time    : 2020/8/27 15:50
# @Author  : 面包狗
# @Email   : 3034221968Qqq.com
# @File    : visual10_numpy.py
# @Software: PyCharm
from matplotlib import pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False
t1 = np.array([1,2,3])
print(t1)
print(type(t1))

t2 = np.array(range(10))
print(t2)
print(type(t2))

t3 = np.arange(4,10,2)
print(t3)
print(type(t3))

print(t3.dtype)