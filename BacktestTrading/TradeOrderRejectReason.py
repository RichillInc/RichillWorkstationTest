# -*- encoding: utf-8 -*-

'''
* @File    :   TradeOrderRejectReason.py
* @Time    :   2021/02/09 04:50:33
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from enum import Enum

class TradeOrderRejectReason(Enum):
    """ 委託單拒絕原因 """
    RISK_RULE_CHECK_FAILED = 1 # 不符合風控規則
    NO_ENOUGH_CASH = 2 # 資金不足
    NO_ENOUGH_POSITION 3 # 倉位不足
    NOT_IN_MARKET_SESSION = 4 # 非交易時段
    