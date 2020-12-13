# -*- coding: utf-8 -*-
# @Time    : 2020/8/30 19:06
# @Author  : 面包狗
# @Email   : 3034221968Qqq.com
# @File    : spider03_cookie.py
# @Software: PyCharm

import requests

# 请求数据urL
member_url = "https://www.yaozh.com/member/"

cookie = {"Cookie": "_ga=GA1.1.1998704260.1598681980; _gid=GA1.1.2110364107.1598681980; acw_tc=2f624a4d15987856657253485e657745141c5a14f2900650cbac4b45abaaab; PHPSESSID=830mse318l9bs7cemmu4fqqkm1; _gat=1; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1598785672; yaozh_logintime=1598785672; yaozh_user=974673%09sqdwsq; yaozh_userId=974673; yaozh_jobstatus=kptta67UcJieW6zKnFSe2JyXnoaabplrnJeHnKZxanJT1qeSoMZYoNdzbZtapdTJ2dTVhpyqn26fhtHCpquUrJrOnlNu1HCWlHNZkm1rm5u084B448edC98485Cfef533351F9095c8ak5aYlVmgqJ%2BYn4OnoKKdU5ysa2SUcIeVbnCZb2qYm5mTmJqRWaCy37868bcfbb3088fa7b74e070a245e3d2; db_w_auth=811950%09sqdwsq; UtzD_f52b_saltkey=MKAWjyVr; UtzD_f52b_lastvisit=1598782073; UtzD_f52b_lastact=1598785673%09uc.php%09; UtzD_f52b_auth=76f5i5YGb1aukHMBXSh1EakLn%2BHaFn1GFkZb%2BWLDUWojUS7p3uM9LPSL22qWdCncEoIfNnptnOjEJ45rNNaM3KAPXIg; yaozh_uidhas=1; yaozh_mylogin=1598785675; _ga=GA1.1.1998704260.1598681980; _gid=GA1.1.2110364107.1598681980; acw_tc=2f624a4d15987856657253485e657745141c5a14f2900650cbac4b45abaaab; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1598680961%2C1598681958%2C1598681980%2C1598785668",}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
}
cook_dict = {

}
response = requests.get(member_url,headers=headers,cookies=cook_dict)