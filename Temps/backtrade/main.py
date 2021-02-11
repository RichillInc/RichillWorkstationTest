
# -*- encoding: utf-8 -*-

'''
* @File    :   main.py
* @Time    :   2021/02/11 22:36:51
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())

from Temps.backtrade.SinopacTradeGateway import SinopacTradeGateway




ga = SinopacTradeGateway()
ga.connect()