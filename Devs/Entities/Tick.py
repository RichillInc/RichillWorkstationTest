# -*- encoding: utf-8 -*-

'''
* @File    :   Tick.py
* @Time    :   2021/02/13 07:45:57
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


class Tick(object):
    """ 逐筆成交 """

    def __init__(self,
        datetime,
        close,
        volume

    ):
        self.__datetime = datetime
        self.__close = close
        self.__volume = volume
    


    def getDatetime(self):
        """ 獲取時間日期 """
        return self.__datetime

    def getClose(self):
        """ 獲取收盤價 """
        return self.__close

    def getVolume(self):
        """ 獲取成交量 """
        return self.__volume        

    def __str__(self):
        return f"Tick [datetime={self.__datetime}, close={self.__close}, volume={self.__volume}]"


