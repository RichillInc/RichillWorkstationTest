# -*- encoding: utf-8 -*-

'''
* @File    :   MarketPosition.py
* @Time    :   2021/02/09 02:04:54
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


class MarketPosition(object):
    """ 市場部位 """

    def __init__(self, tradeDirection, symbol, exchange, quantity, averagePrice):
        self.__tradeDirection = tradeDirection # 交易方向
        self.__symbol = symbol # 合約代號
        self.__exchange = exchange # 交易所
        self.__quantity = 0.0 # 數量
        self.__averagePrice = 0.0  # 均價
        self.__marketValue = 0.0 # 市場價值
        

