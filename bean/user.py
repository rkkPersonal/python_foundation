#  -*-coding:utf8 -*-

from bean.time import time

'''
类的专有方法：
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__truediv__: 除运算
__mod__: 求余运算
__pow__: 乘方
'''


class user(time):
    __id: str
    __name: str

    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def print_to_string(self):
        print('id:' + self.__id + ',name:' + self.__name)


if __name__ == '__main__':
    user = user('1', 'Steven')
    user.print_to_string()
