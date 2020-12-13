

class Student:
    def __init__(self,sn,name,age,sex):
        self.name = name
        self.sn = sn
        self.age = age
        self.sex = sex

    def __str__(self):
        return "%s->%s" % (self.sn,self.name)

