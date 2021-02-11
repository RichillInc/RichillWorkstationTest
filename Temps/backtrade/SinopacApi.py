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

from Devs.Entities.Contract import Contract
from Devs.Entities.OptionContract import OptionContract

class SinopacApi(Shioaji):
    """ 永豐金Api """

    def __init__(self):
        super(SinopacApi, self).__init__()



    def login(self, personId, password):
        """ 登入SinopacApi
        Arguments:
            personId: str 身分證字號
            password: str 登入密碼
        """
        try:
            super().login(personId, password)        
            print(f"SinopacApi 登入成功. [{personId}]")   
        except Exception as exception:
            print(f"SinopacApi 登入失敗. [{exception}]")
            return        


    def downloadAllContracts(self):
        """ 下載所有合約 """
        allContracts = []
        allContracts.extend(self.__downloadFuturesContract())
        allContracts.extend(self.__downloadOptionContracts())
        allContracts.extend(self.__downloadSecurityContracts())
        print(f"合約下載完成. {len(allContracts)}")
                
        return allContracts

    def __downloadFuturesContract(self):
        """ 下載期貨合約 """
        futuresContracts = []
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
                futuresContracts.append(contract)       
        return futuresContracts
        
    def __downloadOptionContracts(self):
        """ 下載選擇權合約 """
        optionContracts = []
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
                optionContracts.append(contract)
        return optionContracts

    def __downloadSecurityContracts(self):
        """ 下載證券合約 """
        securityContracts = []
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
                securityContracts.append(contract)          
        return securityContracts                
