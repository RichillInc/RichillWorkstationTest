# -*- encoding: utf-8 -*-

'''
* @File    :   Contract.py
* @Time    :   2021/02/09 01:37:00
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


class Contract(object):
    """ 商品合約 """

    def __init__(self, symbol, name, exchange, contractType):
        self.__symbol = symbol
        self.__name = name
        self.__exchange = exchange
        self.__contractType = contractType


    def getSymbol(self):
        """ 獲取合約代號 """    
        return self.__symbol


    def getName(self):
        """ 獲取合約名稱 """
        return self.__name

    def getExchange(self):
        """ 獲取交易所 """
        return self.__exchange

    def getContractType(self):
        """ 獲取合約類型 """
        return self.__contractType                          