# -*- coding:utf-8 -*-
# @Time : 2020/8/20 20:51
# @Author : 面包狗
# @File : NetworkSafety01.py
# @Software: PyCharm

import _thread
import time
from subprocess import Popen,PIPE

def ping_check():
    chrck = Popen(["C:/",'-c','ping -c 2'+'127.0.0.1'],stdin=PIPE,stdout=PIPE)
    data = chrck.stdout.read()
    print(data)

ping_check()