# -*- encoding: utf-8 -*-

'''
* @File    :   Exchange.py
* @Time    :   2021/02/09 23:51:00
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from enum import Enum

class Exchange(Enum):
    """ 交易所 """


    # 台灣
    TSE = "TSE" # Taiwan Stock Exchange 台灣證券交易所
    TFE = "TFE" # Taiwan Futures Exchange 台灣期貨交易所

    # 美國

    # 香港

    # 新加坡

    # 澳洲

    # 歐洲

    # 韓國

    # 日本
    