# -*- coding:utf-8 -*-
# @Time : 2020/8/18 21:25
# @Author : 面包狗
# @File : MusicDownloads.py
# @Software: PyCharm

from tkinter import *
import requests
import jsonpath
import os
from urllib.request import urlretrieve


# 歌曲保存
def song_load(song_url, song_title):
    # 创建文件夹保存
    os.makedirs("music", exist_ok=True)
    path = "..\music\{}.mp3".format(song_title)
    text.insert(END,"歌曲：{}，正在下载。。。。".format(song_title))
    # 文本框滚动
    text.see(END)
    # 更新
    text.update()
    # 下载
    urlretrieve(song_url,path)
    text.insert(END,"下载完毕：{}，情试听".format(song_title))
    text.see(END)
    text.update()


# 搜索歌曲名
def get_music_name():
    name = entry.get()
    headers = {
        "X-Requested-With": "XMLHttpRequest",  # 判断你的请求是异步的还是同步
    }
    params = {
        "input": name,
        "filter": "name",
        "type": "qq",
        "page": 1,
    }
    url = "http://www.youtap.xin/"
    resp = requests.post(url, data=params, headers=headers)
    # print(resp.content.decode("utf-8"))
    data = resp.json()
    title = jsonpath.jsonpath(data, "$..title")[0]
    author = jsonpath.jsonpath(data, "$..author")[0]
    url = jsonpath.jsonpath(data, "$..url")[0]
    song_load(url,title)


# 创建一个画布
root = Tk()
# 取标题
root.title("全网音乐下载器")
# 设置窗口大小
root.geometry("710x560+400+200")
# 标签组件
label = Label(root, text="请输入需要下载的歌曲名:", font=("华文行楷", 20))
# 定位
label.grid()
# 输入框创建
entry = Entry(root, font=("隶书", 20))
entry.grid(row=0, column=1)
# 列表框
text = Listbox(root, font=("隶书", 20), width=50, heigh=16)
text.grid(row=1,columnspan=2)
# 下载按钮
botton1 = Button(root,text="开始下载",font=("隶书", 15),command=get_music_name)
botton1.grid(row=2,column=0,sticky=W)
# 退出按钮
botton2 = Button(root,text="退出",font=("隶书", 15))
botton2.grid(row=2,column=1,sticky=E)

# 显示界面
root.mainloop()

