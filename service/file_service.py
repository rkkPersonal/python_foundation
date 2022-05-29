#  -*-coding:utf8 -*-
import sys

import xlrd
import logging.config
import yaml

with open('../config.yaml', 'r', encoding='gbk') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger("main")


def read_file():
    try:
        print(sys.getdefaultencoding())
        file = open(file='../debug.log', mode='r', encoding='gbk')
        logger.info(file.read())
        '''
        data = file.read(32)
        while data:
            print(data, end='')
            data = file.read(32)
        '''
    finally:
        if file is None:
            file.close()
        pass

    return file


def write_file():
    try:
        file = open('../write_test.txt', mode='w', encoding='utf-8')

        file.write('我只想做燕子\n')
        file.write('只需简单思想\n')
        file.write('只求风中流浪\n')
        file.write('我想作树\n')
        file.write('不想长五脏六腑\n')
        file.write('不会肝肠寸断\n')

    finally:
        if file is None:
            file.close()
        pass
