#  -*-coding:utf8 -*-
import sys


def for_demo():
    list_operator = [1, 2, 3, 4, 5, 6]
    for s in list_operator:
        print(s)


def for_range():
    for i in range(10):
        print(i)


def iterator():
    list_iterator = [1, 2, 3, 4]
    it = iter(list_iterator)  # 创建迭代器对象

    while True:
        try:
            print(next(it))
        except StopIteration:
            sys.exit()


if __name__ == '__main__':
    iterator()