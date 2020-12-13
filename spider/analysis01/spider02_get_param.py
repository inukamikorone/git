# -*- coding: utf-8 -*-
# @Time    : 2020/8/28 14:16
# @Author  : 面包狗
# @Email   : 3034221968Qqq.com
# @File    : spider02_get_param.py
# @Software: PyCharm

from  urllib import request,parse
import string


def get_method_params():
    url = "http://www.baidu.com/s?wd="
    # 拼接字符串(汉字)
    # python可以接收的数据
    #  https://www.baidu.com/s?wd=%E7%BE%8E%E5%A5%B3
    name = "美女"
    final_url = url + name
    # 代码发送了请求
    # 网址里面包含了汉字，ASCII没有汉字，url转译

    # 将包含汉字的网址进行转译
    encode_new = parse.quote(final_url,safe=string.printable)

    response = request.urlopen(encode_new)
    # 读取内容
    data = response.read().decode()

    # 保存到本地
    with open("02-encode.html","w",encoding="utf-8") as f:
        f.write(data)
    # UnicodeEncodeError: 'ascii' codec can't encode characters in position 10-11: ordinal not in range(128)
    # python是解释型语言，解析器只支持:ascii 0 - 127
    # 不支持中文

get_method_params()