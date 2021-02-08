# -*- encoding: utf-8 -*-

'''
* @File    :   TradeAccountStatus.py
* @Time    :   2021/02/09 04:47:54
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())

from enum import Enum

class TradeAccountStatus(Enum):

    """ 交易帳戶狀態 """
    CONNECTING = 0 # 連接中
    CONNECTED = 1 # 已連接
    SIGNED = 2 # 已登入
    DISCONNECTING = 3 # 斷開中
    DISCONNECTED = 4 # 已斷開
    