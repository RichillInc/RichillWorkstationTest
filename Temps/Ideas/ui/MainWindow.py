# -*- encoding: utf-8 -*-

'''
* @File    :   MainWindow.py
* @Time    :   2021/02/10 06:01:23
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from PyQt5.Qt import QWidget, QGridLayout

class MainWindow(QWidget):
    """ 主窗口 """


    def __init__(self):
        super(MainWindow, self).__init__()
        self.__menuBar = None
        self.__topBar = None
        self.__centralWidget = None
        self.__statusBar = None

        layout = QGridLayout(self)        


    def setMeunBar(self, menuBar):
        """ 設置選單列 
        Arguments:
            menuBar: MenuBar 選單列
        """

    def setTopBar(self, topBar):
        """ 設置頂端列 
        Arguments:
            topBar: TopBar 頂端列
        """

    def setCentralWidget(self, centralWidget):
        """ 中央組件
        Arguments:
            centralWidget: Widget 組件              
        """

    def setStatusBar(self, statusBar):
        """ 設置狀態列 
        Arguments:
            statusBar: StatusBar 狀態列
        """


        
            