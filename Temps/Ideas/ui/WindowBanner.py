# -*- encoding: utf-8 -*-

'''
* @File    :   WindowBanner.py
* @Time    :   2021/02/10 05:36:30
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from PyQt5.Qt import *
from Temps.ui.CloseWindowButton import CloseWindowButton


class WindowBanner(QWidget):
    """ 窗口橫幅 """

    def __init__(self):
        super(WindowBanner, self).__init__()
        self.__windowTitleLabel = QLabel()
        self.__closeWindowButton = CloseWindowButton(self)
        
        layout = QGridLayout(self)
        layout.addWidget(self.__windowTitleLabel, 0, 0, 1, 9)
        layout.addWidget(self.__closeWindowButton, 0, 9, 1, 1)
        