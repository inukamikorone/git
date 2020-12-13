# -*- coding: utf-8 -*-
# @Time    : 2020/8/28 15:10
# @Author  : 面包狗
# @Email   : 3034221968Qqq.com
# @File    : spider03_get_param.py
# @Software: PyCharm

from  urllib import request,parse
import string

def get_params():
    url = "http://www.baidu.com/s?wd="
    params = {
        "wd":"中文",
        "key":'zhang',
        "value":"san",
    }
    str_params = parse.urlencode(params)
    final_url = url + str_params

    # 将带有中文的url,转译成计算机可以识别的url
    end_url = parse.quote(final_url,safe=string.printable)
    response = request.urlopen(end_url)
    data = response.read().decode("utf-8")
    print(data)

get_params()