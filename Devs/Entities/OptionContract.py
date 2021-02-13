# -*- encoding: utf-8 -*-

'''
* @File    :   OptionContract.py
* @Time    :   2021/02/11 21:50:28
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


from Devs.Entities.Contract import Contract

class OptionContract(Contract):
    """ 選擇權合約 """

    def __init__(self,
        symbol,
        name,
        exchange,
        contractSize,
        priceTick,
        
        optionType,
        strikePrice,

    ):
        """
        Arguments:
            symbol: str 合約代號
            name: str 合約名稱
            exchange: Exchange 交易所
            contractSize: float 合約大小
            priceTick: float 最小跳動點      
            optionType: OptionType 選擇權類型
            strikePrice: float 履約價       
        """
        super(OptionContract, self).__init__(symbol, name, exchange, "選擇權", contractSize, priceTick)
        self.__optionType = optionType
        self.__strikePrice = strikePrice
        


    def getOptionType(self):
        """ 獲取選擇權類型 """
        return self.__optionType

    def getStrikePrice(self):
        """ 獲取履約價 """
        return self.__strikePrice        

    def __str__(self):
        return (f"OptionContract [symbol={self.__symbol}, name={self.__name}, exchange={self.__exchange}, instrumentType={self.__instrumentType}, " 
        + f"contractSize={self.__contractSize}, priceTick={self.__priceTick}, optionType={self.__optionType}, strikePrice={self.__strikePrice}]")
        


