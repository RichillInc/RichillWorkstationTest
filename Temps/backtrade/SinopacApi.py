# -*- encoding: utf-8 -*-

'''
* @File    :   SinopacApi.py
* @Time    :   2021/02/11 22:18:23
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())

from shioaji import Shioaji
from shioaji.constant import QuoteType as SinopacQuoteType

from Devs.Entities.Contract import Contract
from Devs.Entities.OptionContract import OptionContract

class SinopacApi(Shioaji):
    """ 永豐金Api """

    def __init__(self):
        super(SinopacApi, self).__init__()

        self.__sinopacContracts = {}
        self.__subscribedSymbols = set()

    def login(self, personId, password, hashed=0, contractsTimeout=5000, contractsCallback=None):
        """ 登入SinopacApi
        Arguments:
            personId: str 身分證字號
            password: str 登入密碼
            hashed: int 
            contractsTimeout: int 下載合約等待時間 0~10000毫秒
            contractsCallback: Callable 合約回調函數
        """
        try:
            super().login(personId, password, False, contractsTimeout, contractsCallback)        
            print(f"SinopacApi 登入成功. [{personId}]")   
        except Exception as exception:
            print(f"SinopacApi 登入失敗. [{exception}]")
            return        

    def logout(self):
        """ 登出SinopacApi """
        response = super().logout()
        if response: 
            print(f"SinpacApi 已登出")

    def downloadAllContracts(self):
        """ 下載所有合約 """
        # allContracts.extend(self.__downloadIndexContracts())
        # allContracts.extend(self.__downloadFuturesContract())
        # allContracts.extend(self.__downloadOptionContracts())
        # allContracts.extend(self.__downloadSecurityContracts())
        # print(f"合約下載完成. {len(allContracts)}")

        self.__downloadFuturesContract()
        self.__downloadOptionContracts()
        self.__downloadSecurityContracts()
        self.__downloadIndexContracts()
        print(f"合約下載完成. {len(self.__sinopacContracts.items())}")                    


    def __downloadFuturesContract(self):
        """ 下載期貨合約 """
        for instrument in self.Contracts.Futures:
            for futureContract in instrument:
                symbol = futureContract.code
                name = f"{futureContract.name}{futureContract.delivery_month}"
                exchange = "TFE"
                instrumentType = "期貨"
                contractSize = 200
                priceTick = futureContract.unit 

                contract = Contract(
                    symbol,
                    name,
                    exchange,
                    instrumentType,
                    contractSize,
                    priceTick
                )
                # publishContractEvent
                self.__sinopacContracts[symbol] = futureContract     
        
    def __downloadOptionContracts(self):
        """ 下載選擇權合約 """
        for instrument in self.Contracts.Options:
            for optionContract in instrument:
                symbol = optionContract.code
                name = f"{optionContract.name}{optionContract.delivery_month}"
                exchange = "TFE"
                contractSize = 50
                priceTick = optionContract.unit    
                if optionContract.option_right == "C":
                    optionType = "Call"
                else:
                    optionType = "Put"    
                strikePrice = optionContract.strike_price

                contract = OptionContract(
                    symbol,
                    name,
                    exchange, 
                    contractSize, 
                    priceTick,
                    optionType,
                    strikePrice
                )            
                # publishContractEvent
                self.__sinopacContracts[symbol] = optionContract


    def __downloadSecurityContracts(self):
        """ 下載證券合約 """
        for instrument in self.Contracts.Stocks:
            for securityContract in instrument:
                symbol = securityContract.code
                name = securityContract.name
                exchange = "TSE"
                instrumentType = "權益證券"
                contractSize = 1
                priceTick = securityContract.unit
                
                contract = Contract(
                    symbol,
                    name,
                    exchange,
                    instrumentType,
                    contractSize,
                    priceTick
                )
                # publishContractEvent
                self.__sinopacContracts[symbol] = securityContract              

    def __downloadIndexContracts(self):
        """ 下載指數合約 """
        for instrument in self.Contracts.Indexs:
            for indexContract in instrument:
                symbol = indexContract.code 
                name = indexContract.name 
                exchange = "TSE"
                contract = Contract(
                    symbol,
                    name,
                    exchange,
                    "指數",
                    0,
                    0
                )
                self.__sinopacContracts[symbol] = indexContract

    def subscribe(self, contract):
        """ 訂閱報價 
        Arguments:
            contract: Contract 合約
        """
        # TODO: 判斷是否支援交易所
        if self.isContractSubscribed(contract): # 判斷是否重複訂閱
            return        
                    
        sinopacContract = self.getSinopacContractBySymbol(contract.getSymbol()) # 獲取永豐金合約對象
        if sinopacContract:        
            self.quote.subscribe(sinopacContract, SinopacQuoteType.Tick) 
            self.quote.subscribe(sinopacContract, SinopacQuoteType.BidAsk)
            self.__subscribedSymbols.add(sinopacContract.code)
            print(f"訂閱合約: {contract.getExchange()} - {contract.getSymbol()} {contract.getName()}")
            return True

    def isContractSubscribed(self, contract):
        """ 判斷合約是否已訂閱 
        Arguments:
            contract: Contract 合約對象
        """
        if contract.getSymbol() in self.__subscribedSymbols:
            print(f"訂閱失敗, 重複訂閱{contract.getSymbol()}")
            return True
        return False    
        
    def getSinopacContractBySymbol(self, symbol):
        """ 獲取永豐金合約根據合約代號 
        Arguments:
            symbol: str 合約代號
        """                
        sinopacContract = self.__sinopacContracts.get(symbol, None)
        if not sinopacContract:
            print("獲取合約失敗, 查無此合約. [{symbol}]")
        return sinopacContract        


    def setQuoteCallback(self, quoteCallback):
        """ 設置報價回調函數 
        Arguments:
            quoteCallback: Callable 報價回調函數
        """
        self.quote.set_quote_callback(quoteCallback)





