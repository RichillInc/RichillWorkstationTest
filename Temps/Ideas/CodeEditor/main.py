# -*- encoding: utf-8 -*-

'''
* @File    :   main.py
* @Time    :   2021/02/19 01:42:24
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from PyQt5.Qt import QWidget, QGridLayout, QMenuBar, QPlainTextEdit, QTableWidget, QTreeWidget, QTextEdit

class TradeStrategyCodeEditor(QWidget):

    def __init__(self):
        super(TradeStrategyCodeEditor, self).__init__()

        self.menuBar = QMenuBar()
        self.fileBrowser = QWidget()
        self.codeEditor = QPlainTextEdit()
        self.logWindow = QTextEdit()
        self.statusBar = QWidget()

        layout = QGridLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        





if __name__ == '__main__':
    
    from PyQt5.Qt import QApplication

    app = QApplication(sys.argv)

    widget = TradeStrategyCodeEditor()
    widget.show()
    app.exec_()