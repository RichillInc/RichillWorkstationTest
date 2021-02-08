# -*- encoding: utf-8 -*-

'''
* @File    :   TradeOrderStatus.py
* @Time    :   2021/02/09 03:50:41
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


class TradeOrderStatus(object):
    """ 委託單狀態 """
    REJECTED = 0 # 拒絕委託 可能原因: 數量不是整數(貨幣類除外), 保證金不足, 委託價格超過漲跌停價格, 該標的當天無法交易(包含未上市/下市/停牌/未開盤/停止申購等)
    PARTIAL_FILLED = 1 # 部分成交
    FILLED = 2 # 完全成交
    OPEN = 3 # 未成交
    


