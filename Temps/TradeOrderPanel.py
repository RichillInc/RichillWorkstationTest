# -*- encoding: utf-8 -*-

'''
* @File    :   TradeOrderPanel.py
* @Time    :   2021/02/16 05:07:57
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from PyQt5.Qt import *

from Devs.Constants.TradeAction import TradeAction
from Devs.Constants.TradeOrderPriceType import TradeOrderPriceType
from Devs.Constants.TradeOrderType import TradeOrderType

class TradeOrderPanel(QWidget):
    

    def __init__(self):
        super(TradeOrderPanel, self).__init__()
        self.tradeAccountCombo = QComboBox()
        self.buyButton = QPushButton("買進")
        self.buyButton.clicked.connect(self.onBuyButtonClicked)
        self.sellButton = QPushButton("賣出")
        self.sellButton.clicked.connect(self.onSellButtonClicked)

        for button in [self.buyButton, self.sellButton]:
            button.setCheckable(True)
            button.setAutoExclusive(True) 

        self.quantityEdit = QDoubleSpinBox()
        self.quantityEdit.setValue(1)
        self.quantityEdit.setRange(0, 10000)

        self.priceEdit = QDoubleSpinBox()
        self.priceEdit.setRange(0, 10000)

        self.tradeOrderTypeCombo = QComboBox()

        for index, data in enumerate(TradeOrderType, 0):
            self.tradeOrderTypeCombo.addItem(data.value)
            self.tradeOrderTypeCombo.setItemData(index, data)

        self.tradeOrderPriceTypeCombo = QComboBox()

        for index, data in enumerate(TradeOrderPriceType, 0):
            self.tradeOrderPriceTypeCombo.addItem(data.value)
            self.tradeOrderPriceTypeCombo.setItemData(index, data)
        self.sendButton = QPushButton("送出")
        self.sendButton.clicked.connect(self.onSendButtonClicked)

        layout = QGridLayout(self)
        layout.addWidget(self.tradeAccountCombo, 0, 0, 1, 2)
        layout.addWidget(self.buyButton, 1, 0, 1, 1)
        layout.addWidget(self.sellButton, 1, 1, 1, 1)
        layout.addWidget(self.quantityEdit, 2, 0, 1, 2)
        layout.addWidget(self.priceEdit, 3, 0, 1, 2)
        layout.addWidget(self.tradeOrderTypeCombo, 4, 0, 1, 1)
        layout.addWidget(self.tradeOrderPriceTypeCombo, 4, 1, 1, 1)
        layout.addWidget(self.sendButton, 5, 0, 1, 2)

        self.quantityEdit.valueChanged.connect(self.onQuantityEditValueChanged)
        self.priceEdit.valueChanged.connect(self.onPriceEditValueChanged)
        self.tradeOrderPriceTypeCombo.currentTextChanged.connect(self.onTradeOrderPriceTypeComboCurrentTextChanged)

    def onSendButtonClicked(self):
        """ 按下送出按鈕 """
        tradeAccountId = self.getTradeAccountId()
        tradeAction = self.getTradeAction()
        quantity = self.getQuantity()
        price = self.getPrice()
        tradeOrderType = self.getTradeOrderType()
        tradeOrderPriceType = self.getTradeOrderPriceType()

        print(f"""
TradeOrder [
    tradeAccountId={tradeAccountId},
    tradeAction={tradeAction},
    quantity={quantity},
    price={price},
    tradeOrderType={tradeOrderType},
    tradeOrderPriceType={tradeOrderPriceType}        
]
""")

    def getTradeAccountId(self):
        return self.tradeAccountCombo.currentData()

    def getTradeAction(self):
        """ 獲取買賣別 """

        tradeAction = None
        if self.buyButton.isChecked():
            tradeAction = TradeAction.BUY

        elif self.sellButton.isChecked():
            tradeAction = TradeAction.SELL
        return tradeAction 

    def getQuantity(self):
        """ 獲取委託數量 """
        return float(self.quantityEdit.text())

    def getPrice(self):
        """ 獲取委託價格 """
        return float(self.priceEdit.text())

    def getTradeOrderType(self):
        """ 獲取委託類型 """
        return self.tradeOrderTypeCombo.currentData()

    def getTradeOrderPriceType(self):
        """ 獲取價格類型 """
        return self.tradeOrderPriceTypeCombo.currentData()        

    def onTradeOrderPriceTypeComboCurrentTextChanged(self):
        """ 當委託單價格類型組合框當前文字改變 """
        if self.getTradeOrderPriceType() == TradeOrderPriceType.MARKET:
            self.priceEdit.setValue(0)
        elif self.getTradeOrderPriceType() == TradeOrderPriceType.LIMIT:
            print("TODO: 判斷是買進還賣出, 買進設置BidPrice1, 賣出設置AskPrice1")
  
    def onBuyButtonClicked(self):
        """ 按下買進按鈕 """
        self.updateSendButtonDisplayText()  

    def onSellButtonClicked(self):
        """ 按下賣出按鈕 """
        self.updateSendButtonDisplayText()             

    def setSendButtonDisplayText(self, action, quantity, price):
        """ 更新送出委託按鈕顯示文字 """
        if action == TradeAction.BUY:
            actionText = "買進"
        else: 
            actionText = "賣出"

        if price == 0:
            price = "市價"

        displayText = f"{actionText} {quantity}@{price}"
        self.sendButton.setText(displayText)

    def updateSendButtonDisplayText(self):
        """ 更新送出委託按鈕顯示文字 """
        self.setSendButtonDisplayText(self.getTradeAction(), self.getQuantity(), self.getPrice())

    def onQuantityEditValueChanged(self):
        """ 當數量編輯框數值改變 """
        # if self.getTradeAction():
        self.updateSendButtonDisplayText()    

    def onPriceEditValueChanged(self):
        """ 價格編輯框數值改變 """    
        # if self.getTradeAction():
        self.updateSendButtonDisplayText()

if __name__ == '__main__':
    
    
    app = QApplication(sys.argv)
    widget = TradeOrderPanel()
    widget.show()
    app.exec_()


