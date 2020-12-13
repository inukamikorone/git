import sqlite3
import xlwt
from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import csv

def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1，获取网页
    datalist = getData(baseurl)
    savepath = "./豆瓣电影top250.xls"
    dbpath = "movie.db"
    saveData(datalist,savepath) # 保存成为excel数据
    # saveDataDB(datalist, dbpath)  # 保存成为sqlite


findLink = re.compile(r'<a href="(.*?)">')  # 创建正则表达式对象，表示规则（字符串模式）
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(10):  # 调用获取网页信息的函数10次
        url = baseurl + str(i)
        html = askURl(url)  # 保存获取到的网页源码

        # 2，解析一个网页
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_="item"):  # 查找符合要求的字符串，形成列表
            # print(item)
            data = []  # 保存一部电影的所有信息
            item = str(item)

            link = re.findall(findLink, item)[0]
            data.append(link)
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)
            title = re.findall(findTitle, item)
            if (len(title)) == 2:
                ctitle = title[0]
                data.append(ctitle)
                otitle = title[1].replace("/", "")
                data.append(otitle)
            else:
                data.append(title[0])
                data.append(" ")

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)

            inq = re.findall(findInq, item)[0]
            data.append(inq)

            bd = re.findall(findBd, item)[0]
            bd = re.sub("<br(\s+)?/>(\s+)?", " ", bd)
            bd = re.sub("/", " ", bd)
            data.append(bd.strip())

            datalist.append(data)
    return datalist

def saveData(datalist, savepath):
    # 3,保存数据
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet("豆瓣电影top250", cell_overwrite_ok=True)
    col = ("电影详情连接", "图片连接", "影片中文名", "影片外文名", "平分", "评价数", "概况", "相关信息")
    for i in range(0, 8):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        print("第%d条" % i)
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])

    book.save("豆瓣电影.xls")

def saveDataDB(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cru = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"' + data[index] + '"'
        sql = '''
            insert into movie250(
            info_link,pic_link,cname,ename,score,rated,instroduction,info)
            values (%s);''' % ",".join(data)
        cru.execute(sql)
        conn.commit()
    cru.close()
    conn.close()


def init_db(dbpath):
    sql = """
        create table movie250(
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar ,
        score numeric ,
        rated numeric ,
        instroduction text,
        info text
        );
    """
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


# 得到指定一个url的网页内容
def askURl(url):
    head = {  # 模拟浏览器头部信息，向豆瓣发送信息
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36",
    }  # 用户代理表示告诉豆瓣我们是什么类型的机器

    request = urllib.request.Request(url, headers=head)
    html = " "
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:

        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html


if __name__ == '__main__':
    main()
