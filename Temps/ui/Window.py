# -*- encoding: utf-8 -*-

'''
* @File    :   Window.py
* @Time    :   2021/02/10 05:34:12
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())

from PyQt5.Qt import *
from Temps.ui.WindowBanner import WindowBanner
class Window(QWidget):


    def __init__(self):
        super(Window, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.__windowBanner = WindowBanner()
        

        layout = QGridLayout(self)
        layout.addWidget(self.__windowBanner, 0, 0, 1, 10)


    def setWindowTitle(self, title):
        self.__windowBanner.setTitle(title)
        