# -*- encoding: utf-8 -*-

'''
* @File    :   CloseWindowButton.py
* @Time    :   2021/02/10 05:32:25
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from PyQt5.Qt import QPushButton

class CloseWindowButton(QPushButton):
    """ 關閉窗口按鈕 """

    def __init__(self, parent):
        super(CloseWindowButton, self).__init__()
        self.clicked.connect(self.onClicked)

    def onClicked(self):
        """ 被按下時調用 """
        self.parent().close()


