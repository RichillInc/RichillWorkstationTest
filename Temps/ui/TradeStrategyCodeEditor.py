# -*- encoding: utf-8 -*-

'''
* @File    :   TradeStrategyCodeEditor.py
* @Time    :   2021/02/11 06:05:50
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())

from PyQt5.Qt import *


class TradeStrategyCodeEditor(QWidget):
    """ 策略編輯 """

    CREATE_NEW_FOLDER_ICON = "Resources\Icons\CreateNewFolder.png"
    ADD_FILE_ICON = "Resources\Icons\Add.png"

    def __init__(self):
        super(TradeStrategyCodeEditor, self).__init__()


        self.createNewFolderButton = QPushButton()
        self.createNewFolderButton.setIcon(QIcon(TradeStrategyCodeEditor.CREATE_NEW_FOLDER_ICON))
        self.createNewFolderButton.clicked.connect(self.onCreateNewFolderButtonClicked)
        self.addFileButton = QPushButton()
        self.addFileButton.setIcon(QIcon(TradeStrategyCodeEditor.ADD_FILE_ICON))
        self.addFileButton.clicked.connect(self.onAddFileButtonClicked)

        layout = QGridLayout(self)
        layout.addWidget(self.createNewFolderButton, 0, 0, 1, 1)
        layout.addWidget(self.addFileButton, 0, 1, 1, 1)

    def onCreateNewFolderButtonClicked(self):
        """ 創建新目錄按鈕 """

        self.createNewFolderDialog = QDialog()
        
        folderNameLabel = QLabel("目錄名稱")
        folderNameEdit = QLineEdit()
        okButton = QPushButton("確定")
        cancelButton = QPushButton("取消")
        
        layout = QGridLayout(self.createNewFolderDialog)

        layout.addWidget(folderNameLabel, 0, 0, 1, 1)
        layout.addWidget(folderNameEdit, 0, 1, 1, 3)
        layout.addWidget(okButton, 1, 0, 1, 2)
        layout.addWidget(cancelButton, 1, 2, 1, 2)

        self.createNewFolderDialog.exec_()

    def onAddFileButtonClicked(self):
        """ 新增檔案按鈕 """
        self.addFileDialog = QDialog()
        
        fileNameLabel = QLabel("檔案名稱")
        fileNameEdit = QLineEdit()
        okButton = QPushButton("確定")
        cancelButton = QPushButton("取消")
        
        layout = QGridLayout(self.addFileDialog)

        layout.addWidget(fileNameLabel, 0, 0, 1, 1)
        layout.addWidget(fileNameEdit, 0, 1, 1, 3)
        layout.addWidget(okButton, 1, 0, 1, 2)
        layout.addWidget(cancelButton, 1, 2, 1, 2)

        self.addFileDialog.exec_()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    widget = TradeStrategyCodeEditor()
    widget.show()
    app.exec_()
