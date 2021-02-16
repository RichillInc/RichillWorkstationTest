# -*- encoding: utf-8 -*-

'''
* @File    :   Contract.py
* @Time    :   2021/02/11 21:28:11
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

    def __init__(self,
        symbol,
        name,
        exchange,
        instrumentType,
        contractSize,
        priceTick
    ):
        """
        Arguments:
            symbol: str 合約代號
            name: str 合約名稱
            exchange: Exchange 交易所
            instrumentType: InstrumentType 商品類型
            contractSize: float 合約大小
            priceTick: float 最小跳動點

        TODO arguments: 
            minimumTradingQuantity: float 最小下單量
            isSupportsStopOrder: bool 是否支持停損單
            

        """

        self.__symbol = symbol
        self.__name = name
        self.__exchange = exchange
        self.__instrumentType = instrumentType
        self.__contractSize = contractSize
        self.__priceTick = priceTick

    def getSymbol(self):
        """ 獲取合約代號 """
        return self.__symbol

    def getName(self):
        """ 獲取合約名稱 """
        return self.__name

    def getExchange(self):
        """ 獲取交易所 """
        return self.__exchange

    def getInstrumentType(self):
        """ 獲取商品類型 """
        return self.__instrumentType

    def getContractSize(self):
        """ 獲取合約大小 """
        return self.__contractSize

    def getPriceTick(self):
        """ 獲取最小跳動點 """
        return self.__priceTick                                        

    def __str__(self):
        return (f"Contract [symbol={self.__symbol}, name={self.__name}, exchange={self.__exchange}, instrumentType={self.__instrumentType}, " 
        + f"contractSize={self.__contractSize}, priceTick={self.__priceTick}]")
