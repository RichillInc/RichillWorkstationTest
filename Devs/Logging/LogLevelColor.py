# -*- encoding: utf-8 -*-

'''
* @File    :   LogLevelColor.py
* @Time    :   2021/02/17 21:31:36
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from enum import Enum


class LogLevelColor(Enum):
    """ 日誌等級顏色 """

    DEBUG = 0x0007 
    INFO = 0x02 
    WARNING = 0x06
    ERROR = 0x04 
    CRITICAL = 0x05

