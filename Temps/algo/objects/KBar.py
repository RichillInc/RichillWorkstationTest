# -*- encoding: utf-8 -*-

'''
* @File    :   KBar.py
* @Time    :   2021/02/09 21:00:21
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


class KBar(object):
    """ K棒 
    儲存每根K棒的基礎數據, ex. 時間, 開, 高, 低, 收, 量
    """

    def __init__(self,
        symbol,        
        open,
        high,
        low,
        close,
        volume
    ):
        """
        Arguments:
            symbol: str 合約代號

            open: float K棒的開盤價
            high: float K棒的最高價
            low: float K棒的最低價
            close: float K棒的收盤價
            volume: float K棒的成交量

        """        
        self.__symbol = symbol

        self.__open = open
        self.__high = high
        self.__low = low
        self.__close = close
        self.__volume = volume

    def getSymbol(self):
        """ 獲取合約代號 """
        return self.__symbol

    def getName(self):
        """ 獲取合約名稱 """
        return self.__name        

    def getOpen(self):
        """ 獲取開盤價 """
        return self.__open

    def getHigh(self):
        """ 獲取最高價 """
        return self.__high

    def getLow(self):
        """ 獲取最低價 """
        return self.__low

    def getClose(self):
        """ 獲取收盤價 """
        return self.__close

    def getVolume(self):
        """ 獲取成交量 """
        return self.__volume          