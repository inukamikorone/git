from urllib.request import urlopen, urlretrieve, Request
from urllib.parse import quote

import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def search_baidu(wd="千峰"):
    # 网络资源的接口（URL
    url = "https://www.baidu.com/s?wd=%s"
    headers = {"Cookie": "BIDUPSID=EAD99A83A5E3009E0DABD230A45CF45A; PSTM=1589893090; "
                  "BAIDUID=EAD99A83A5E3009EA763677FA68B00CE:FG=1; BD_UPN=12314753; "
                  "BDUSS=o4R3Jsb244Y1hQTFV-R0xKbGR0VHh4Rmt2WVVxV0FLRWxrTFQzNUtH"
                  "TExsaDlmSVFBQUFBJCQAAAAAAAAAAAEAAADbefXCvtW7qLf-"
                  "uaS3wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
                  "AAAAAAAAAAAAAAMsJ-F7LCfheSk; "
                  "BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS_BFESS=o4R3Jsb244Y1hQTFV-R0xKbGR"
                  "0VHh4Rmt2WVVxV0FLRWxrTFQzNUtHTExsaDlmSVFBQUFBJCQAAAAAAAAAAAEAAADbefXCvtW7qLf-"
                  "uaS3wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMsJ-"
                  "F7LCfheSk; COOKIE_SESSION=88601_8_9_5_3_11_0_0_9_5_3_1_0_0_10_0_1596537121_"
                  "1596358363_1596633628%7C9%2355_299_1596358349%7C9; H_PS_645EC=a9e653LsLxNyx1%2F"
                  "3F6kbstOv2YvyloB4i3037rao6fNGn79bfQ2Vg7fmaur3xf5u%2BkbI; BD_HOME=1; "
                  "H_PS_PSSID=32294_1447_31670_32328_31253_32349_32045_32398_32404_32429_32091",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}

    # 生成请求对象，封装请求的url和头header
    request = Request(url % quote(wd),headers=headers)
    response = urlopen(request)
    assert response.code == 200
    print("请求成功")

    # 读取响应的对象
    bytes_ = response.read()

    # 当对象进入上下文时，调用对象的
    # 当对象退出上下文时，调用对象的
    with open("%s.html" % wd, "wb") as file:
        file.write(bytes_)


def download_img(url):

    # 从url中获取文件名
    filename = url[url.rfind("/")+1:]

    urlretrieve(url, filename)


if __name__ == '__main__':
    # search_baidu()
    download_img("https://www.dy2018.com/d/file/html/gndy/jddyy/2020-08-06/debfff36236e32f5b33279323ff32f44.jpg")
