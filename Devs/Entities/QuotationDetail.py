# -*- encoding: utf-8 -*-

'''
* @File    :   QuotationDetail.py
* @Time    :   2021/02/22 08:29:14
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


class QuotationDetail(object):
    """ 報價單明細 """

    def __init__(self,
        quotationId,
        itemName, 
        quantity,
        unit,
        unitPrice,
        amount,
        remark
    ):
        """
        Arguments:
            quotationId (str): 報價單號
            itemName (str): 品項名稱
            quantity (float): 數量
            unit (str): 單位
            unitPrice (float): 單價
            amount (float): 金額
            remark (str): 備註
        """
        self.__quotationId = quotationId 
        self.__itemName = itemName
        self.__quantity = quantity
        self.__unit = unit
        self.__unitPrice = unitPrice
        self.__amount = amount
        self.__remark = remark

    def getQuotationId(self):
        """ 獲取報價單號 """
        return self.__quotationId

    def getItemName(self):
        """ 獲取品項名稱 """
        return self.__itemName

    def getQuantity(self):
        """ 獲取數量 """
        return self.__quantity

    def getUnit(self):
        """ 獲取計量單位 """
        return self.__unit

    def getUnitPrice(self):
        """ 獲取單價 """
        return self.__unitPrice

    def getAmount(self):
        """ 獲取金額 """
        return self.__amount

    def getRemark(self):
        """ 獲取備註 """
        return self.__remark                        

    def __str__(self):
        return f"QuotationDetail [quotationId={self.__quotationId}]"        
    



