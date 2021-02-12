
# -*- encoding: utf-8 -*-

'''
* @File    :   SinopacTradeGateway.py
* @Time    :   2021/02/11 21:34:12
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from copy import copy
from threading import Thread
from datetime import datetime
from time import sleep


from shioaji.order import Status as SinopacOrderStatus # 永豐金委託單狀態
from shioaji import constant as SinopacConstant # 永豐金常數
from shioaji.account import StockAccount, FutureAccount # 永豐金股票&期貨帳戶  

from Devs.Apis.SinopacApi import SinopacApi
from Devs.TradeGateways.TradeGateway import TradeGateway

"""
Required classes:
    
Enum Classes:    
    Direction,
    Exchange,
    InstrumentTyp,
    OptionType,
    Status,
    TradeOrderType,
    TradeOrderOffset 

Data Classes:
    Tick,
    TradeOrder,
    Trade,
    TradeAccount,
    Contract,
    Position

Todos:
    - MarketData
        - HistoricalMarketData
        - Snapshot
        - ShortStockSource
        - CreditEnquires

    - TradeOrder
        - Stock
        - Futures and Option    
        - IntradayOdd
        - UpdateStatus
    - Account
        

"""

class SinopacTradeGateway(TradeGateway):
    """ 永豐金交易網關 """


    def __init__(self):
        super(SinopacTradeGateway, self).__init__("Sinopac")
        self.__api = SinopacApi() # 永豐金API

    def connect(self):
        """ 連接永豐金API """
        self.__api.login(personId, password)
        # TODO: activateCA(caPtah)
        # TODO: [optional] seelct default account
        self.__api.downloadAllContracts()                   
        self.__api.setQuoteCallback(self.publishQuote)
        # TODO: start thread
        
    def disconnect(self):
        """ 中斷永豐金API連線 """
        self.__api.logout()

    def subscribe(self, contract):
        """ 訂閱合約報價 
        Arguments:
            contract (Contract): 合約對象
        """
        self.__api.subscribe(contract)

    def publishQuote(self, topic, quoteData):
        """
        發布報價
        Arguments:
            topic (str): 標題
            quoeData (dict): 報價資料 
        """
        try:
            # 判斷報價類型
            quoteType = topic.split("/")[0] 
            

        except Exception as exception:
            exceptionType, traceback = sys.exc_info()
            filename = os.path.split(traceback.tb_frame.f_code.co_filename)[1]
            print(f"[{exceptionType}][{filename}][{traceback.tb_lineno}][{exception}]")
            print(quoteData)            

    def sendTradeOrder(self, contract, tradeOrder):
        """ TODO: 送出委託單 
        Arguments:
            contract (Contract): 合約
            tradeOrder (TradeOrder): 委託單
        """
        self.__api.sendTradeOrder(contract, tradeOrder)



if __name__ == '__main__':
    
    # Code for testing
    from Devs.Entities.Contract import Contract    

    gateway = SinopacTradeGateway() # create gateway
    gateway.connect() # connect gateway    

    # Create test contracts
    contract1 = Contract("2330", "台積電", "TSE", "證券", 1, 0.5)
    contract3 = Contract("2303", "聯電", "TSE", "證券", 1, 0.5)
    # Test for subscirbe contracts
    gateway.subscribe(contract1)
    gateway.subscribe(contract3)
    




