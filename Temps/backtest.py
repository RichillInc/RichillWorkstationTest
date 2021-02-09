# -*- encoding: utf-8 -*-

'''
* @File    :   backtest.py
* @Time    :   2021/02/09 22:58:17
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())

from Devscripts.historicalTest import getHistoricalKBarData
from Devscripts.BacktestMarketDataSimulator import BacktestMarketDataSimulator

class MyStrategy:

    def __init__(self):
        self.__subscribedSymbols = ["2330.TW", "3008.TW"]

    def onKBarUpdated(self, barEvent):
        """"""
        print(f"策略:{self.__class__.__name__}, 接收到K棒{barEvent.getKBar().getSymbol()}, 成交價: {barEvent.getKBar().getClose()}")





    def getSubscribedContractSymbols(self):
        return self.__subscribedSymbols

    def isSymbolSubscribed(self, symbol):
        return symbol in self.__subscribedSymbols


class MyStrategy2:
    def __init__(self):
        self.__subscribedSymbols = ["2303.TW", "3037.TW", "2330.TW"]

    def onKBarUpdated(self, barEvent):
        """"""
        print(f"策略:{self.__class__.__name__}, 接收到K棒{barEvent.getKBar().getSymbol()}, 成交價: {barEvent.getKBar().getClose()}")


    def getSubscribedContractSymbols(self):
        return self.__subscribedSymbols

    def isSymbolSubscribed(self, symbol):
        return symbol in self.__subscribedSymbols        


simulator = BacktestMarketDataSimulator()
strategies = [MyStrategy(), MyStrategy2()]
symbols = []
for s in strategies:
    ss = s.getSubscribedContractSymbols()
    symbols.extend(ss)

for symbol in symbols:
    kbars = getHistoricalKBarData(symbol)
    simulator.addKBars(symbol, kbars)

simulator.startSimulation(strategies)

