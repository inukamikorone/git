# -*-coding:utf-8-*-
# @Time:2020/8/2313:44
# @Author:面包狗
# @Email:3034221968@qq.com
# @File:stu_db.py
# @Software:PyCharm

from DAO.base import BaseDao
from entity import Student


class StuDao(BaseDao):
    def query(self,where=None,args=None):
        item =  super(StuDao,self.query("student","sn","name","age","sex",where=where,whereargs=args))
        return [
            Student(item["sn"],item["name"],item["sex"],item["age"])
        ]

if __name__ == '__main__':
    dao = StuDao()
    print(dao.query())