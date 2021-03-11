
"""
閃電下單

- 一般設定 GenrialSetting
    - 委託前跳出確認視窗 setShowComfirmWindowBeforeSendTradeOrder()
    - 刪單前跳出確認視窗 setShowComfirmWindowBeforeCancelTradeOrder()
    - 委託成功音效 
    - 委託失敗音效 
    - 成交音效 

"""
import sys 


from PyQt5.Qt import *

app = QApplication(sys.argv)

# 閃電下單介面

table = QTableWidget()

columnNames = [
    "觸價",
    "買進",
    "委買",
    "",
    "委賣",
    "賣出",
    "觸價"
]

table.setColumnCount(len(columnNames))
table.setHorizontalHeaderLabels(columnNames)

table.resizeColumnsToContents()
table.resize(600, 1000)
table.show()
app.exec_()