# -*- encoding: utf-8 -*-

'''
* @File    :   BacktestMarketDataSimulator.py
* @Time    :   2021/02/09 22:21:16
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from Devscripts.KBarUpdatedEvent import KBarUpdatedEvent



class BacktestMarketDataSimulator():
    """ 回測行情模擬器 """


    def __init__(self):
        self.__historicalMarketData = {
        }

    def addKBars(self, symbol, kBars):
        """ 添加K棒 
        Arguments:
            symbol: str 商品代號
            kBars: KBar 歷史數據K棒
        """

        # 新增K棒
        if not self.__historicalMarketData.get(symbol, None):
            self.__historicalMarketData[symbol] = []
            self.__historicalMarketData[symbol].extend(kBars)
        else:
            self.__historicalMarketData[symbol].extend(kBars)

    def startSimulation(self, strategies):
        """ 開始模擬 """
        
        for symbol in self.__historicalMarketData.keys():
            for strategy in strategies:
                if self.isSubscribedByStrategy(symbol, strategy):
                    bars = self.__historicalMarketData[symbol]
                    for bar in bars:
                        barUpdatedEvent = KBarUpdatedEvent(bar)
                        strategy.onKBarUpdated(barUpdatedEvent)

    def getHistoricalMarketData(self, symbol):
        return self.__historicalMarketData[symbol]

    def isSubscribedByStrategy(self, symbol, strategy):
        """ """          
        if strategy.isSymbolSubscribed(symbol):
            return True
        else:
            return False      