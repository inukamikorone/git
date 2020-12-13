"""
应用，百度翻译
 - urllib.request.Request()
 - urllib.request.urlopen()
 - urllib.request.urlencode()
 - 发起post请求
"""
import json
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://fanyi.baidu.com/v2transapi?from=zh&to=en"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Cookie": "BIDUPSID=157D6ED675F6169AA3E4962D17275DB1; PSTM=1597562301; BAIDUID=157D6ED675F6169AF4E550778438CCF0:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; DOUBLE_LANG_SWITCH=0; JAPAN_PINYIN_SWITCH=1; BDUSS=NIMzYxVkQ4aUwxWnpjRW5BOWkzR25vYUtGODRna2Z-djZVVnEtam5ENUdRbVJmSVFBQUFBJCQAAAAAAAAAAAEAAADbefXCvtW7qLf-uaS3wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEa1PF9GtTxfan; BDUSS_BFESS=NIMzYxVkQ4aUwxWnpjRW5BOWkzR25vYUtGODRna2Z-djZVVnEtam5ENUdRbVJmSVFBQUFBJCQAAAAAAAAAAAEAAADbefXCvtW7qLf-uaS3wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEa1PF9GtTxfan; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=7; H_PS_PSSID=1456_32573_32530_32327_31660_32352_32045_32117_26350_32504_32482; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1597674870,1597882691; __yjsv5_shitong=1.0_7_700b49dd26ddad4deb4ff4494ba99240e976_300_1597882736289_221.13.63.194_ad4102ec; yjs_js_security_passport=20105e1962265c921f49df88c96a32d8a6e602bd_1597882763_js; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1597884023",
    "x-requested-with": "XMLHttpRequest",
}


def fanyi(kw):
    data = {
        "kw": kw
    }
    # 下面data 的参数是byte类型
    req = Request(url,
                  data=urlencode(data).encode("utf-8"))

    resp = urlopen(req)
    assert resp.code == 200

    json_data = resp.read() # byte
    content_encode = resp('Content-Type')
    content_encode = "utf-8" if content_encode is None else content_encode.split("=")[-1]

    return json.loads(json_data.decode(content_encode))


if __name__ == '__main__':
    print(fanyi("orange"))
