# -*- coding:utf-8 -*-
# @Time : 2020/8/20 9:34
# @Author : 面包狗
# @File : spider03_urllib_parse.py
# @Software: PyCharm

"""
复杂的get请求，多页面请求下载
"""
import time
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


url = "https://www.baidu.com/s?"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Cookie": "BIDUPSID=157D6ED675F6169AA3E4962D17275DB1; PSTM=1597562301; BAIDUID=157D6ED675F6169AF4E550778438CCF0:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; DOUBLE_LANG_SWITCH=0; JAPAN_PINYIN_SWITCH=1; BDUSS=NIMzYxVkQ4aUwxWnpjRW5BOWkzR25vYUtGODRna2Z-djZVVnEtam5ENUdRbVJmSVFBQUFBJCQAAAAAAAAAAAEAAADbefXCvtW7qLf-uaS3wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEa1PF9GtTxfan; BDUSS_BFESS=NIMzYxVkQ4aUwxWnpjRW5BOWkzR25vYUtGODRna2Z-djZVVnEtam5ENUdRbVJmSVFBQUFBJCQAAAAAAAAAAAEAAADbefXCvtW7qLf-uaS3wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEa1PF9GtTxfan; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=7; H_PS_PSSID=1456_32573_32530_32327_31660_32352_32045_32117_26350_32504_32482; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1597674870,1597882691; __yjsv5_shitong=1.0_7_700b49dd26ddad4deb4ff4494ba99240e976_300_1597882736289_221.13.63.194_ad4102ec; yjs_js_security_passport=20105e1962265c921f49df88c96a32d8a6e602bd_1597882763_js; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1597884023",
    "x-requested-with": "XMLHttpRequest",
}
params = {
    "wd": "",
    "pn": 0  # 0 10 20 30 40....     =(n-1)*10
}


def pages_get(wd):
    params["wd"] = wd
    for page in range(1,101):
        params["pn"] = (page - 1) * 10

        page_url = url + urlencode(params)
        resp = urlopen(Request(page_url, headers=headers))

        assert resp.code == 200
        file_name = "baidu_pages/%s-%s.html" % (wd, page)
        with open(file_name, "wb") as f:
            bytes_ = resp.read()
            f.write(bytes_)
            print(f"{file_name} 写入成功!")
            time.sleep(0.5)
    print("下载%s100页成功" % wd)

if __name__ == '__main__':
    pages_get("Python3.6")