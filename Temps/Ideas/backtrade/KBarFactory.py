# -*- encoding: utf-8 -*-

'''
* @File    :   KBarFactory.py
* @Time    :   2021/02/10 21:45:34
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())

from Temps.backtrade.KBar import KBar


class KBarFactory(object):
    """ K線工廠 """


    @staticmethod
    def createKBar(symbol, exchange, date, time, open, high, low, close, volume):
        """ 創建K線對象 """
        kBar = KBar(symbol, exchange, date, time, open, high, low, close, volume)
        return kBar
