# -*- encoding: utf-8 -*-

'''
* @File    :   TradeOrderPriceType.py
* @Time    :   2021/02/13 07:47:32
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from enum import Enum

class TradeOrderPriceType(Enum):
    """ 委託單價格類型 """
    # Limit
    # Market
