#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    作者:     Damon 
    日期:     2018/6/28 
    版本:     1.0
    文件:     contextor.py 
    功能: 
        
"""

import os

# without context manager
cur_dir = os.path.join(os.getcwd(), "data")
file = os.path.join(cur_dir, "contextor.txt")
f = open(file, 'w')
print(f.closed)  # whether the file is open
f.write("hello,world!")
f.close()
print(f.closed)

with open(file, 'a') as f:
    print(f.closed)
    f.write("hello,world!")
print(f.closed)


class VOW(object):
    """
        任何定义了 __enter__() 和 __exit__()方法的对象都可以用于上下文管理器
    """

    def __init__(self, text):
        self.text = text

    def __enter__(self):
        self.text = "enter: " + self.text  # 添加前缀
        return self  # 注意,这里返回对象

    def __exit__(self, exc_type, exc_value, traceback):
        self.text = self.text + "now __exit__ !"  # 添加后缀


with VOW("你好") as myvow:
    print(myvow.text)
print(myvow.text)

if __name__ == '__main__':
    pass
