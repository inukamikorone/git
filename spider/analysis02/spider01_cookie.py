# -*- coding: utf-8 -*-
# @Time    : 2020/8/29 14:01
# @Author  : 面包狗
# @Email   : 3034221968Qqq.com
# @File    : spider01_cookie.py
# @Software: PyCharm

"""
    直接获取个人中心的页面

    1，代码登录 登录成功 cookie有效
    2，自动带着cookie去请求个人中心
"""

from urllib import request

url = "https://www.yaozh.com/member/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
    "Cookie": "acw_tc=707c9fc515986807931704332e3668026b7b47034c957fa516d87493285656; PHPSESSID=f1qmgv7eirtegi61u3e6qq6np5; _ga=GA1.2.1932410471.1598680796; _gid=GA1.2.1422759773.1598680796; yaozh_logintime=1598681044; yaozh_user=974673%09sqdwsq; yaozh_userId=974673; yaozh_jobstatus=kptta67UcJieW6zKnFSe2JyXnoaabplrnJeHnKZxanJT1qeSoMZYoNdzbZtapdTJ2dTVhpyqn26fhtHCpquUrJrOnlNu1HCWlHNZkm1rm5u28CCb1E849dF369059a8aA793F5Ea444akpSYlVmgqJ%2BYn4OnoKKdU5ysa2SUcIeVbnCZbmqUlZaXnZaVWaCy34501badfd32364552f73937cf6225cd; _gat=1; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1598681048; yaozh_uidhas=1; yaozh_mylogin=1598681050; acw_tc=707c9fc515986807931704332e3668026b7b47034c957fa516d87493285656; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1598680797%2C1598680961",
}

request.Request(url,headers=headers)
response = request.urlopen(url)

data = response.read()

with open("01cookie.html","wb") as f:
    f.write(data)