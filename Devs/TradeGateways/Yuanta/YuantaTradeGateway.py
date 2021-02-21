# -*- encoding: utf-8 -*-

'''
* @File    :   YuantaTradeGateway.py
* @Time    :   2021/02/20 05:46:05
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())

from Devs.TradeGateways.TradeGateway import TradeGateway

class YuantaTradeGateway(TradeGateway):
    """ 元大交易網關 """

    def __init__(self):
        super(YuantaTradeGateway, self).__init__("Yuanta")

    


