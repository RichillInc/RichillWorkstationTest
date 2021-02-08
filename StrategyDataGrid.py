

# -*- encoding: utf-8 -*-

'''
* @File    :   StrategyDataGrid.py
* @Time    :   2021/02/09 04:19:02
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from PyQt5.Qt import *

class StrategyDataGrid(QTableWidget):


    columnNames = [
        "策略代號",
        "策略名稱",
        "狀態",
        "通知",
        "淨利",
        "累計報酬率(%)",        
        "本日損益",
        "本月損益",
        "策略啟動時間"
    ]

    def __init__(self):
        super(StrategyDataGrid, self).__init__()
        self.resize(3000, 1500)
        self.setColumnCount(len(self.columnNames))
        self.setHorizontalHeaderLabels(self.columnNames)
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.setSelectionBehavior(QTableWidget.SelectRows)
        self.verticalHeader().setVisible(False)



if __name__ == '__main__':
    
    
    app = QApplication(sys.argv)
    widget = StrategyDataGrid()
    widget.show()
    app.exec_()        