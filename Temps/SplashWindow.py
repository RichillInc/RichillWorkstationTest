# -*- encoding: utf-8 -*-

'''
* @File    :   SplashWindow.py
* @Time    :   2021/02/09 17:18:36
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from PyQt5.Qt import QSplashScreen

class SplashWindow(QSplashScreen):
    """ 啟動視窗 """

    def __init__(self):
        super(SplashWindow, self).__init__()



