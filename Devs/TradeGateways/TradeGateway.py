# -*- encoding: utf-8 -*-

'''
* @File    :   TradeGateway.py
* @Time    :   2021/02/12 01:55:30
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


class TradeGateway(object):
    """ 交易網關 
    
    """

    def __init__(self, tradeGatewayName):
        """
        Arguments:
            tradeGatewayName (str): 交易網關名稱
        """
        super(TradeGateway, self).__init__()
        self.__tradeGatewayName = tradeGatewayName


    def getTradeGatewayName(self):
        """ 獲取交易網關名稱 """
        return self.__tradeGatewayName



