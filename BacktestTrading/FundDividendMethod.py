# -*- encoding: utf-8 -*-

'''
* @File    :   FundDividendMethod.py
* @Time    :   2021/02/09 03:59:30
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


class FundDividendMethod(object):
    """ 基金分紅方式 """
    NO_DIVIDEND = 0 # 不分配 
    CASH_DIVIDEND = 1 # 配息
    REINVESTMENT = 2 # 再投資