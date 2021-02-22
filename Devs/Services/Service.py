# -*- encoding: utf-8 -*-

'''
* @File    :   Service.py
* @Time    :   2021/02/22 01:12:27
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from Devs.Logging.LoggerFactory import LoggerFactory

class Service(object):
    """ 服務基類, 所有服務類別必須繼承此類別 """

    def __init__(self):
        self.__logger = LoggerFactory.createLogger(self.__class__.__name__)

    def _getLogger(self):
        """ 獲取日誌器 """
        return self.__logger