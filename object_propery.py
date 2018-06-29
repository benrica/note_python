#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    作者:     Damon 
    日期:     2018/6/28 
    版本:     1.0
    文件:     object_propery.py 
    功能: 
        
"""


class Bird(object):
    feather = True


class Chicken(Bird):
    fly = False

    def __init__(self, age):
        self.age = age


chick = Chicken(2)
print("类及属性展示...")
print("Bird:", Bird.__dict__)
print("Chicken:", Chicken.__dict__)
print("chick:", chick.__dict__)

print("------------------------")
chick.__dict__['age'] = 3
print(chick.__dict__['age'])

chick.age = 10
print(chick.age)


# 特性 @property

class Num(object):
    """
        类的特性
        定义3个函数，一个设置特性的值，一个获取特性的值，一个删除特性的值，然后将这3个函数作为参数传给类 property 做实例化
    """
    def __init__(self, value):
        self.value = value

    def getNeg(self):
        return -self.value

    def setNeg(self, value):
        self.value = -value

    def delNeg(self):
        print("value also deleted")
        del self.value

    neg = property(getNeg, setNeg, delNeg, "I'm negative")


print("\n类的特性展示")
print(Num.__doc__)
x = Num(1.1)
print(x.neg)
x.neg = -22
print(x.value)
print(Num.neg.__doc__)
del x.neg


# 访问即时生成的属性或是访问不存在的属性时可以用这个来实现
class bird(object):
    feather = True


class chicken(bird):
    """
        访问即时生成的属性或是访问不存在的属性时 __getattr__ 方法实现
    """
    fly = False

    def __init__(self, age):
        self.age = age

    def __getattr__(self, name):
        if name == 'adult':
            if self.age > 1.0:
                return True
            else:
                return False
        else:
            raise AttributeError(name)


print("访问即时生成属性展示")
summer = chicken(2)
print(summer.__doc__)
print(summer.adult)
summer.age = 0.5
print(summer.adult)

print(summer.male)

if __name__ == '__main__':
    pass
