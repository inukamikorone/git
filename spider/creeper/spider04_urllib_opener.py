# -*- coding:utf-8 -*-
# @Time : 2020/8/20 10:26
# @Author : 面包狗
# @File : spider04_urllib_opener.py
# @Software: PyCharm

from collections import namedtuple
from urllib.request import HTTPHandler,build_opener

# 声明类  namedtuple 有命名的元组类
Response = namedtuple("Response",field_names=["headers","code","text","body","encoding"])

def get(url):
    opener = build_opener(HTTPHandler())
    resp = opener.open(url)
    # 要求返回某一类的对象，应该包含：headers->dict, code->int  text 文本  body 字节码


    headers = dict(resp.getheaders())
    try:
        encoding = headers["Content-Type"].split("=")[-1]
    except:
       encoding = "utf-8"
    code = resp.code
    body = resp.read()
    text = body.decode(encoding)


    return Response(headers=headers,
                    encoding=encoding,
                    code=code,
                    body=body,
                    text=text)

if __name__ == '__main__':
    resp:Response = get("http://jd.com")
    print(resp.code)
    print(resp.text)

    resp.code = 300     # 禁止修改namedtuple类的属性，(元组是不可变类型)
    print("ok")