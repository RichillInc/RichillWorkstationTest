# -*- encoding: utf-8 -*-

'''
* @File    :   TradeOrderStatus.py
* @Time    :   2021/02/13 07:48:53
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from enum import Enum

class TradeOrderStatus(Enum):
    """ 委託單狀態 """
    
    # Submitting
    # Rejected
    # Filled
    # PartialFilled
    

