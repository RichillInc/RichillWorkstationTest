# -*- encoding: utf-8 -*-

'''
* @File    :   TradeAccount.py
* @Time    :   2021/02/13 07:52:37
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


class TradeAccount(object):
    """ 交易帳戶 """


    def __init__(self, tradeAccountId, tradeAccountName):
        """
        Arguments:
            tradeAccountId (str): 交易帳戶代號
            tradeAccountName (str): 交易帳戶名稱
        """
        self.__tradeAccountId = tradeAccountId
        self.__tradeAccountName = tradeAccountName

    def __str__(self):
        return f"TradeAccount [tradeAccountId={tradeAccountId}, tradeAccountName={self.__tradeAccountName}]"

    
    
