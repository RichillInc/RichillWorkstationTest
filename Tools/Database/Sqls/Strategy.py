# -*- encoding: utf-8 -*-

'''
* @File    :   Strategy.py
* @Time    :   2021/02/01 22:10:02
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


class Strategy(object):
    """ 策略 """

    CREATE = """
    Create Table If Not Exists Strategy (
        StrategyId Varchar(255),
        StrategyName Varchar(255),
        StrategyFileName Varchar(255)
    )
    """

