#  -*-coding:utf8 -*-

"""

https://www.runoob.com/python3/python3-data-type.html

Python3 中有六个标准的数据类型：

Number（数字）
String（字符串）

List（列表）
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
元组中的元素类型也可以不相同：
Tuple（元组）

Set（集合）
Dictionary（字典）
Python3 的六个标准数据类型中：

不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。



isinstance 和 type 的区别在于：

type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
"""
import json


def judgement_data_type():
    a, b, c = 1, 0.3, 'hello'
    print(type(a))
    print(type(b))
    print(type(c))


def string_operation():
    str = 'Runoob'

    print(str)  # 输出字符串
    print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
    print(str[0])  # 输出字符串第一个字符
    print(str[2:5])  # 输出从第三个开始到第五个的字符
    print(str[2:])  # 输出从第三个开始的后的所有字符
    print(str * 2)  # 输出字符串两次，也可以写成 print (2 * str)
    print(str + "TEST")  # 连接字符串


def list_operation():
    list = ['abcd', 786, 2.23, 'runoob', 70.2]
    tinylist = [123, 'runoob']

    print(list)  # 输出完整列表
    print(list[0])  # 输出列表第一个元素
    print(list[1:3])  # 从第二个开始输出到第三个元素
    print(list[2:])  # 输出从第三个元素开始的所有元素
    print(tinylist * 2)  # 输出两次列表
    print(list + tinylist)  # 连接列表


def tuple_operation():
    tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
    tinytuple = (123, 'runoob')

    print(tuple)  # 输出完整元组
    print(tuple[0])  # 输出元组的第一个元素
    print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
    print(tuple[2:])  # 输出从第三个元素开始的所有元素
    print(tinytuple * 2)  # 输出两次元组
    print(tuple + tinytuple)  # 连接元组


def set_operation():
    sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

    print(sites)  # 输出集合，重复的元素被自动去掉

    # 成员测试
    if 'Runoob' in sites:
        print('Runoob 在集合中')
    else:
        print('Runoob 不在集合中')

    # set可以进行集合运算
    a = set('abracadabra')
    b = set('alacazam')

    print(a)

    print(a - b)  # a 和 b 的差集

    print(a | b)  # a 和 b 的并集

    print(a & b)  # a 和 b 的交集

    print(a ^ b)  # a 和 b 中不同时存在的元素


''' 类似于java的HashMap'''


def dictionary_opeartion():
    dict = {}
    dict['one'] = "1 - 菜鸟教程"
    dict[2] = "2 - 菜鸟工具"

    tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

    print(dict['one'])  # 输出键为 'one' 的值
    print(dict[2])  # 输出键为 2 的值
    print(tinydict)  # 输出完整的字典
    print(tinydict.keys())  # 输出所有键
    print(tinydict.values())  # 输出所有值


def dic_operation():
    tinydict = {'Name': 'Runoob', 'Age': 7, 'NicName': '小菜鸟'}

    print("tinydict['Name']: ", tinydict['Name'])
    print(len(tinydict))
    del tinydict['Age']

    print(tinydict)
    print(len(tinydict))

    print(json.dumps(tinydict))


if __name__ == "__main__":
    dic_operation()
