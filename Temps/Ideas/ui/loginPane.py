# -*- encoding: utf-8 -*-

'''
* @File    :   loginPane.py
* @Time    :   2021/02/16 10:28:18
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())

from PyQt5.Qt import *

class LoginPane(QWidget):
    """ 登入窗格 """

    def __init__(self):
        super(LoginPane, self).__init__()
        self.setupUi()

    def setupUi(self):
        """ 初始化界面 """
        self.userIdLabel = QLabel("使用者代號")
        self.userIdEdit = QLineEdit()
        self.passwordLabel = QLabel("使用者密碼")
        self.passwordEdit = QLineEdit()
        self.passwordEdit.setEchoMode(QLineEdit.Password)
        self.loginButton = QPushButton("登入")

        layout = QGridLayout(self)
        layout.addWidget(self.userIdLabel)
        layout.addWidget(self.userIdEdit)        
        layout.addWidget(self.passwordLabel)
        layout.addWidget(self.passwordEdit)
        layout.addWidget(self.loginButton)
        self.__connectSignals()

    def __connectSignals(self):    
        """ 連接訊號 """
        self.loginButton.clicked.connect(self.onLoginButtonClicked)

    def onLoginButtonClicked(self):
        """ 按下登入按鈕 """
        # 接收數據
        userId = self.getUserId()
        password = self.getPassword()
        print(userId, password)
        self.login(userId, password)

    def getUserId(self):
        """ 獲取使用者代號 """
        userId = self.userIdEdit.text()
        return userId

    def getPassword(self):
        """ 獲取登入密碼 """
        password = self.passwordEdit.text()
        return password

    def login(self, userId, password):
        """ 
        Arguments:
            userId (str): 使用者代號
            password (str): 使用者密碼
        """    
        # 進行數據檢驗
        if not userId or userId.isspace():
            print("使用者代號不可為空")
            return 

        # 進行業務邏輯處理: 登入流程
        # 返回操作結果
                    

        if not password or password.isspace():
            print("登入密碼不可為空")
            return




if __name__ == '__main__':
    
    
    app = QApplication(sys.argv)
    widget = LoginPane()
    widget.show()
    app.exec_()



