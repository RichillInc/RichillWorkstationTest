# -*- encoding: utf-8 -*-

'''
* @File    :   LogLevel.py
* @Time    :   2021/02/17 20:32:13
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from enum import Enum

class LogLevel(Enum):
    """ 日誌等級 """

    DEBUG = "Debug"
    INFO = "Info"
    WARNING = "Warning"
    ERROR = "Error"
    CRITICAL = "Critical"
    


