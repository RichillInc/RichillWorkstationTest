# -*- encoding: utf-8 -*-

'''
* @File    :   StrategyTemplate.py
* @Time    :   2021/02/09 23:43:02
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


class StrategyTemplate(object):
    """ 策略模板 
    回測策略的基礎類不可直接使用


    """

    def __init__(self):
        self.__subscribedContracts = {} # 已訂閱合約 key => symbol, value=> Contract
        self.__strategyParameters = {} # 策略參數 key=> symbol, value=> StrategyParamter
       
            

    def getSubscribedContracts(self):
        """ 獲取此策略訂閱的合約列表 
        """
        return [contract for contract in self.__subscribedContracts.values()]

    def getSubscribedContractSymbols(self):
        """ 獲取此合約訂閱的合約的合約代號列表 
        """
        return [symbol for symbol in self.__subscribedContracts.items()]

    def getSubscribedContractBySymbol(self, symbol):
        """ 獲取訂閱的合約 
        """
        return self.__subscribedContracts.get(symbol, None)

    def subscribeContract(self, contract):
        """ 訂閱合約
        """
        self.__subscribedContracts[contract.getSymbol()] = contract

    def sendTradeOrder(self):
        """ TODO: 送出委託單 
        Arguments: 
            symbol: str 合約代號
            tradeSide: TradeSide 交易方向 TradeSide.LONG or TradeSide.SHORT
            quantity: float 委託數量
            price: float 委託價格
            tradeOrderType: TradeOrderType 委託單類型 TradeOrderType.ROD or TradeOrderType.FOK or TradeOrderType.IOC
            tradeOrderOffset: TradeOrderOffset 開倉或平倉 TradeOrderOffset.OPEN or TradeOrderOffset.CLOSE (只適用於期貨/選擇權)
            tradeOrderPriceType: TradeOrderPriceType 價格類型 TradeOrderPriceType.LIMIT or TradeOrderPriceType.MARKET
        """
        



        
