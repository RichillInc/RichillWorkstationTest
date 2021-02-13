# -*- encoding: utf-8 -*-

'''
* @File    :   TradeOrder.py
* @Time    :   2021/02/13 07:34:04
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


class TradeOrder(object):
    """ 委託單 """


    def __init__(self, 
        tradeOrderId, 
        tradeOrderOffset, 
        tradeAction, 
        quantity, 
        price,
        tradeOrderPriceType,
        tradeOrderType,
        tradeOrderStatus

    ):
        """
        Arguments:
            tradeOrderId (str): 委託單代號
            tradeOrderOffset (TradeOrderOffset): 開平倉
            tradeAction (TradeAction): 交易動作
            quantity (float): 數量
            price (float): 價格
            tradeOrderPriceType (TradeOrderPriceType): 委託價格類型 LIMIT / MARKET
            tradeOrderType (TradeOrderType): 委託類型 ROD / FOK / IOC
            tradeOrderStatus (TradeOrderStatus): 委託狀態 SUMMITING, REJECTED, FILLED, PARTAIL_FILLED 
        """
        self.__tradeOrderId = tradeOrderId
        self.__tradeOrderOffset = tradeOrderOffset
        self.__tradeAction = tradeAction
        self.__quantity = quantity
        self.__price = price
        self.__tradeOrderPriceType = tradeOrderPriceType
        self.__tradeOrderType = tradeOrderType
        self.__tradeOrderStatus = tradeOrderStatus

    def getTradeOrderId(self):
        """ 獲取委託單代號 """
        return self.__tradeOrderId

    def getTradeOrderOffset(self):
        """ 獲取開平倉類型 """
        return self.__tradeOrderOffset

    def getTradeAction(self):
        """ 獲取交易動作 """
        return self.__tradeAction

    def getQuantity(self):
        """ 獲取委託數量 """
        return self.__quantity

    def getPrice(self):
        """ 獲取委託價格 """                                          
        return self.__price

    def getTradeOrderPriceType(self):
        """ 獲取委託價格類型 """
        return self.__tradeOrderPriceType

    def getTradeOrderType(self):
        """ 獲取委託類型 """
        return self.__tradeOrderType

    def getTradeOrderStatus(self):
        """ 獲取委託單狀態 """
        return self.__tradeOrderStatus

    def __str__(self):
        return f"TradeOrder []"
        

