# -*- encoding: utf-8 -*-

'''
* @File    :   OperationResultType.py
* @Time    :   2021/02/22 04:55:55
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from enum import Enum

class OperationResultType(Enum):
    """ 操作結果類型 """

    SUCCESS = "操作成功"
    FAILED = "操作失敗"
    




