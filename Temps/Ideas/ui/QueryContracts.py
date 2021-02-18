# -*- encoding: utf-8 -*-

'''
* @File    :   QueryContracts.py
* @Time    :   2021/02/12 04:24:14
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())

from PyQt5.Qt import *





class QueryContract(QWidget):

    def __init__(self):
        super(QueryContract, self).__init__()

        self.searchingEdit = QLineEdit()
        self.searchingEdit.setPlaceholderText("搜尋")
        self.searchingEdit.setClearButtonEnabled(True)
        # self.searchingEdit.textChanged.connect(self.onSearchingEditTextChanged)

        allButton = QPushButton("全部")
        stockButton = QPushButton("股票")
        futuresButton = QPushButton("期貨")
        optionButton = QPushButton("選擇權")
        fundButton = QPushButton("基金")
        forexButton = QPushButton("外匯")
        cryptoButton = QPushButton("加密貨幣")
        buttons = [allButton, stockButton, futuresButton, optionButton, fundButton, forexButton, cryptoButton]
        for button in buttons:
            button.setAutoExclusive(True)
            button.setCheckable(True)


        columnNames = [
            "合約代號",
            "名稱",
            "交易所",
            "商品類型",
            
        ]
        self.contractDataGrid = QTableWidget()
        self.contractDataGrid.setColumnCount(len(columnNames))
        self.contractDataGrid.setHorizontalHeaderLabels(columnNames)
        

        layout = QGridLayout(self)
        layout.addWidget(self.searchingEdit, 0, 0, 1, 10)
        for i in range(0, len(buttons)):
            layout.addWidget(buttons[i], 1, i, 1, 1)

        layout.addWidget(self.contractDataGrid, 2, 0, 8, 10)


        # load all contracts    
        contracts = contractService.getAllContracts()
        for contract in contracts:
            self.addContractToDataGrid(contract)



    def addContractToDataGrid(self, contract):
        """ 新增合約到資料表 
        Arguments:
            contract (Contract): 合約
        """
        row = self.contractDataGrid.rowCount()
        self.contractDataGrid.insertRow(row)

        symbolCell = QTableWidgetItem(contract.getSymbol())
        nameCell = QTableWidgetItem(contract.getName())
        exchangeCell = QTableWidgetItem(contract.getExchange())
        instrumentType = QTableWidgetItem(contract.getInstrumentType())

        self.contractDataGrid.setItem(row, 0, symbolCell)
        self.contractDataGrid.setItem(row, 1, nameCell)
        self.contractDataGrid.setItem(row, 2, exchangeCell)
        self.contractDataGrid.setItem(row, 3, instrumentType)

        
        
        



if __name__ == '__main__':
    
    
    
    app = QApplication(sys.argv)
    widget = QueryContract()
    widget.show()
    app.exec_()
