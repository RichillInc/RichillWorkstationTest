
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

from Devs.Entities.Contract import Contract
from Devs.Entities.OptionContract import OptionContract
from Temps.backtrade.SinopacApi import SinopacApi


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
"""

class SinopacTradeGateway():
    """ 永豐金交易網關 """


    def __init__(self):
        self.__subscribedContracts = set() # 已訂閱的合約
        self.__downloadedContracts = {} # 下載的合約
        self.__api = SinopacApi() # 永豐金API

    def connect(self):
        """ 連接永豐金API """
        personId = "P123622990"
        password = "among7201"
        self.__api.login(personId, password)
             
        # TODO: activateCA
        # TODO: [optional] seelct default account
        # downloadAllContracts
        allContracts = self.__api.downloadAllContracts()
        for contract in allContracts:
            self.__downloadedContracts[contract.getSymbol()] = contract                         
        
        self.__api.quote.set_callback(self.publishQuote)
        # start thread
        



    def publishQuote(self, topic, quoteData):
        """
        發布報價
        Arguments:
            topic: str 標題
            quoeData: dict 報價資料 
        """
        try:
            # 判斷報價類型
            quoteType = topic.split("/")[0] 

        except Exception as exception:
            exceptionType, traceback = sys.exc_info()
            filename = os.path.split(traceback.tb_frame.f_code.co_filename)[1]
            print(f"[{exceptionType}][{filename}][{traceback.tb_lineno}][{exception}]")
            print(quoteData)            




