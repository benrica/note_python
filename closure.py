#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    作者:     Damon 
    日期:     2018/6/28 
    版本:     1.0
    文件:     closure.py 
    功能: 
        
"""


def line_conf():
    def line(x):
        return 2 * x

    return line


line = line_conf()
print(line(5))


def line_conf():
    b = 10

    def line(x):
        return 2 * x + b

    return line


line = line_conf()
print(line(5))


def line_conf(a, b):
    def line(x):
        return a * x + b

    return line


print("定义：一个包含有环境变量取值的函数对象。是一种组织代码的结构，提供了代码的可重复使用性")
line = line_conf(2, 3)
print(line(5))
print(line.__closure__)
print(line.__closure__[0].cell_contents)
print(line.__closure__[1].cell_contents)

if __name__ == '__main__':
    pass
