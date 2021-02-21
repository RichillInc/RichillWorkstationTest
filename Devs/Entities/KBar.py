# -*- encoding: utf-8 -*-

'''
* @File    :   KBar.py
* @Time    :   2021/02/13 07:46:28
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


class KBar(object):
    """ K線 """


    def __init__(self,
        datetime,
        open,
        high,
        low,
        close,
    ):
        
        """
        Arguments:
            datetime (datetime): 日期時間
            open (float): 開盤價
            high (float): 最高價
            low (float): 最低價
            close (float): 收盤價
            
        """
        self.__datetime = datetime
        self.__open = open
        self.__high = high 
        self.__low = low 
        self.__close = close 

    def getDatetime(self):
        """ 獲取時間日期 """
        return self.__datetime

    def setDatetime(self, datetime):
        """ 設置時間日期 
        Arguments: 
            datetime (datetime): 日期時間
        """
        self.__datetime = datetime    

    def getOpen(self):
        """ 獲取開盤價 """
        return self.__open    

    def getHigh(self):
        """ 獲取最高價 """
        return self.__high

    def setHigh(self, high):
        """
        Arguments:
            high (float): 最高價
        """
        self.__high = high

    def getLow(self):
        """ 獲取最低價 """
        return self.__low

    def setLow(self, low):
        """
        Arguments:
            low (float): 最低價
        """
        self.__low = low

    def getClose(self):
        """ 獲取收盤價 """
        return self.__close

    def setClose(self, close):
        """
        Arguments:
            close (float): 收盤價 
        """
        self.__close = close        
                            
    def __str__(self):
        return f"KBar [datetime={self.__datetime}, open={self.__open}, high={self.__high}, low={self.__low}, close={self.__close}]"
        
        



