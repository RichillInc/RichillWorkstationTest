# -*- encoding: utf-8 -*-

'''
* @File    :   ContractType.py
* @Time    :   2021/02/09 01:39:01
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from enum import Enum

class ContractType(Enum):
    """ 合約類型 """


    FUTURES = "期貨"
    OPTION = "選擇權"

