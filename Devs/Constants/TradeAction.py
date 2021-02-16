# -*- encoding: utf-8 -*-

'''
* @File    :   TradeAction.py
* @Time    :   2021/02/16 05:23:15
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


from enum import Enum

class TradeAction(Enum):
    """ 交易動作 """

    BUY = "Buy"
    SELL = "Sell"



