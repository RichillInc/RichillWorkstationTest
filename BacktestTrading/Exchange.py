# -*- encoding: utf-8 -*-

'''
* @File    :   Exchange.py
* @Time    :   2021/02/09 01:39:57
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from enum import Enum

class Exchange(object):
    """ 交易所 """


    TSE = "TSE" # Taiwan Stock Exchange
    TFE = "TFE" # Taiwan Futures Exchange

