# -*- encoding: utf-8 -*-

'''
* @File    :   BacktestTrader.py
* @Time    :   2021/02/09 01:30:09
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from Backtest.Portfolio import Portfolio


class BacktestTrader(object):
    """ 回測交易員 """

    def __init__(self):
        self.__watchedContracts = {} # 關注的合約
        self.__portfolio = Portfolio() # 此交易員的投資組合
        self.__trades = [] # 交易列表
    

    def setWatchedContracts(self, contracts):
        """ 設置關注的合約 
        Arguments:
            contracts: list[Contract] 關注的合約列表
        """
        for contract in contracts:
            self.addWatchedContract(contract)

    def addWatchedContract(self, contract):
        """ 新增關注的合約 
        Arguments:
            contract: Contract 關注的合約
        """
        symbol = contract.getSymbol()
        self.__watchedContracts[symbol] = contract

    def getWatchedContracts(self):
        """ 獲取關注的合約列表 """
        return list(self.__watchedContracts.values()) 

    def getWatchedContractBySymbol(self, symbol):
        """ 根據合約代號獲取關注的合約 """
        return self.__watchedContracts.get(symbol, None)

    def getWatchedContractSymbols(self):
        """ 獲取關注的合約代號列表 """
        watchedContractSymbols = list(contract.getSymbol() for contract in self.getWatchedContracts())
        return watchedContractSymbols

    # ================ 事件處理 ===============

    def onKBarUpdated(self, kBarUpdatedEvent):
        """ 處理K棒更新事件 """
        raise NotImplementedError("Should implement onKBarUpdated()")

    def onMarketOpened(self, marketOpenedEvent):
        """ 處理市場開盤事件 """

    def onMarketClosed(self, marketClosedEvent):
        """ 處理市場收盤事件 """
    
            
        
    # =============== 事件處理結束 ============
    
    # =============== 交易指令 ================            
    def closeAllPositions(self):
        """ 全部平倉 """

    def closeAllPositionBySymbol(self, symbol):
        """ 根據合約代號平倉所有部位 """

    def cancelTradeOrder(self, tradeOrderId):
        """ 取消委託單 """

    def purchase(self, symbol, amount):
        """ 申購基金 """                    

    def redeem(self, symbol, amount):
        """ 贖回基金 """

    def getPositionBySymbol(self, symbol):
        """ 根據合約代號查詢持倉狀況 """

    def getPositions(self):
        """ 獲取持倉狀況 """

            






if __name__ == '__main__':
    from Backtest.Contract import Contract
    from Backtest.Exchange import Exchange
    from Backtest.ContractType import ContractType
    txf = Contract("TXF202102", "台指期貨202102", Exchange.TFE, ContractType.FUTURES)
    txf2 = Contract("TXF202103", "台指期貨202103", Exchange.TFE, ContractType.FUTURES)
    backtrader = BacktestTrader()
    backtrader.setWatchedContracts([txf, txf2])


    
               