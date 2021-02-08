# -*- encoding: utf-8 -*-

'''
* @File    :   OptimizationResult.py
* @Time    :   2021/02/06 22:10:44
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from PyQt5.Qt import *

class OptimizationResult(QWidget):
    """ 最佳化結果 """

    def __init__(self, resultValues, targetDisplay):
        """
        @param resultValues: list 結果數值
        @param targetDisplay: str 
        """
        super(OptimizationResult, self).__init__()


        self.setWindowTitle("策略最佳化結果") # 設置窗口標題
        self.setFixedSize(1100, 500) # 設置固定窗口大小

        # 創建結果表
        table = QTableWidget() 
        table.setColumnCount(2) # 設置欄數
        table.setRowCount(len(resultValues)) # 設置列數
        table.setHorizontalHeaderLabels(["參數", targetDisplay]) # 設置欄標題
        table.setEditTriggers(QTableWidget.NoEditTriggers) # 設置不可編輯
        table.verticalHeader().setVisible(False) # 隱藏列

        # table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        # table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)


        exportToCsvButton = QPushButton("輸出為CSV")
        exportToCsvButton.clicked.connect(self.onExportToCsvButtonClicked)

  
  

        layout = QGridLayout(self)
        layout.addWidget(table, 0, 0, 9, 10)
        layout.addWidget(exportToCsvButton, 9, 9, 1, 1)

    def onExportToCsvButtonClicked(self):
        """ 當按下儲存為CSV按鈕 """
        print("TODO: 輸出為CSV檔案")



if __name__ == '__main__':


    
    app = QApplication(sys.argv)
    
    # TODO: getResultValues(), getTargetDisplay()
    resultValues = []
    targetDisplay = ""

    w = OptimizationResult(resultValues, targetDisplay)
    w.show()
    app.exec_()
