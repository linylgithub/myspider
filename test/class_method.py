#!/usr/bin/env python
#-*-coding: utf-8 -*-
"""
@version: 0.1
@author:linyl
@file: class_method.py
@time: 2018/10/6 16:36
"""

import math

class Circle(object):
    """一个圆"""

    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi*self.radius**2

    @property
    def perimeter(self):
        return 2*math.pi*self.radius

class Foo(object):
    def __init__(self, val):
        self.__NAME = val #将所有的数据属性都隐藏起来

    @property
    def name(self):
        return self.__NAME #obj.name访问的是self.__NAME(这也是真实值的存放位置)

    @name.setter
    def name(self, value):
        if not isinstance(value, str): #类型检查
            raise TypeError('%s must be str'%value)

    @name.deleter
    def name(self):
        raise TypeError('Can not delete')

if __name__ == '__main__':
    f =Foo('hello')
    print(f.name)
    f.name = '123'
    f.name = 123
    # def f.name

    c = Circle(5)
    print('radius:%0.2f'%float(c.radius))
    print('area:%0.2f'%c.area)
    print('perimeter:%0.2f'%c.perimeter)
    c.perimeter = 100