# -*- encoding: utf-8 -*-

'''
* @File    :   Trade.py
* @Time    :   2021/02/09 02:00:19
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


class Trade(object):
    """ 交易 """

    def __init__(self, tradeId):
        self.__tradeId = tradeId # 交易序號
        
        
        self.__profitAndLoss = 0 # 交易損益
        self.__commission = 0 # 手續費 
        self.__netProfit = 0 # 淨損益

    