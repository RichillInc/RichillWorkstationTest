# -*- encoding: utf-8 -*-

'''
* @File    :   TodoListWidgetItem.py
* @Time    :   2021/03/01 05:33:13
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from PyQt5.Qt import QWidget, QGridLayout, QCheckBox, QLabel

class TodoListWidgetItem(QWidget):
    """
    代辦事項清單項目
    """

    def __init__(self, title="", isDone=False):
        """
        Arguments:
            title (str): 標題 
            isDone (bool): 是否完成, 預設值為False
        """
        super(TodoListWidgetItem, self).__init__()
        self.__checkBox = QCheckBox()
        self.__titleLabel = QLabel()

        self.setTitle(title)
        self.setTitleTextStrikeOut(isDone)
        self.setDone(isDone)
        
        layout = QGridLayout(self)
        layout.addWidget(self.__checkBox, 0, 0, 1, 1)
        layout.addWidget(self.__titleLabel, 0, 1, 1, 9)

        self.__checkBox.clicked.connect(self.onCheckBoxClicked)


    def onCheckBoxClicked(self):
        """ 按下複選框 """  
        isDone = self.__checkBox.isChecked()
        self.setTitleTextStrikeOut(isDone)
        self.setDone(isDone)
        
    def setDone(self, isDone):
        """ 設置完成狀態 
        Arguments:
            isDone (bool): 是否完成
        """
        self.__checkBox.setChecked(isDone)

    def setTitle(self, title):
        """ 設置標題
        Arguments:
            title (str): 標題 
        """        
        self.__titleLabel.setText(title)

    def isDone(self):
        """
        是否完成
        """
        return self.__checkBox.isChecked()

    def getTitle(self):
        """
        獲取標題
        """    
        return self.__titleLabel.text()

    def setTitleTextStrikeOut(self, isDone):
        """ 
        設置標題文字刪除線
        """
        font = self.__titleLabel.font()
        font.setStrikeOut(isDone)
        self.__titleLabel.setFont(font)

if __name__ == '__main__':
    
    from PyQt5.Qt import QApplication
    app = QApplication(sys.argv)

    widget = TodoListWidgetItem()
    widget.setDone(False)
    widget.setTitle("Todo1")

    print(widget.isDone(), widget.getTitle())

    widget.show()
    app.exec_()


