#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    作者:     Damon 
    日期:     2018/6/28 
    版本:     1.0
    文件:     decorator.py 
    功能: 
        
"""


# 计算平方和
def square_sum(a, b):
    print("square_sum input:", a, b)
    return a ** 2 + b ** 2


# 计算平方差
def square_sub(a, b):
    print("square_sub input:", a, b)
    return a ** 2 - b ** 2


print(square_sum(3, 2))
print(square_sub(3, 2))


def decorator(f):
    def deco_f(a, b):
        print("input:", a, b)
        return f(a, b)

    return deco_f


# 计算平方和
@decorator
def square_sum(a, b):
    return a ** 2 + b ** 2


# 计算平方差
@decorator
def square_sub(a, b):
    return a ** 2 - b ** 2


print(square_sum(3, 2))
print(square_sub(3, 2))


# 再加一个包装层

def deco(pre=""):
    def deco1(f):
        def deco2(a, b):
            print(pre + " input:", a, b)
            return f(a, b)

        return deco2

    return deco1


# 计算平方和
@deco("square_sum")
def square_sum(a, b):
    return a ** 2 + b ** 2


# 计算平方差
@deco("square_sub")
def square_sub(a, b):
    return a ** 2 - b ** 2


print(square_sum(5, 2))
print(square_sub(5, 2))


def decorator(aClass):
    class newClass:
        def __init__(self, age):
            self.total_display = 0
            self.wrapped = aClass(age)

        def display(self):
            self.total_display += 1
            print("total display", self.total_display)
            self.wrapped.display()

    return newClass


@decorator
class Bird:
    def __init__(self, age):
        self.age = age

    def display(self):
        print("my age is", self.age)


eagleLord = Bird(5)

for i in range(5):
    eagleLord.display()

if __name__ == '__main__':
    pass
