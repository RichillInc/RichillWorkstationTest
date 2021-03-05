# -*- encoding: utf-8 -*-

'''
* @File    :   DailyTaskWidget.py
* @Time    :   2021/03/02 02:22:38
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from PyQt5.Qt import QWidget, QListWidget, QGridLayout, QPushButton, QLabel, QFont




class DailyTaskWidget(QWidget):
    """ 每日任務 """
    __widgetName = "每日任務"

    def __init__(self):
        super(DailyTaskWidget, self).__init__()
        self.setObjectName(self.__widgetName)

        dailyTaskLabelFont = QFont()
        dailyTaskLabelFont.setPointSize(12)
        dailyTaskLabel = QLabel("今日任務")
        dailyTaskLabel.setFont(dailyTaskLabelFont)
        selectFromListButton = QPushButton("從清單中選取")

        self.__taskList = QListWidget()

        layout = QGridLayout(self)
        layout.addWidget(dailyTaskLabel, 0, 0, 1, 2)
        layout.addWidget(selectFromListButton, 0, 8, 1, 2)
        layout.addWidget(self.__taskList, 1, 0, 1, 10)

        selectFromListButton.clicked.connect(self.onSelectFromListButtonClicked)

    def onSelectFromListButtonClicked(self):
        """ 按下從清單中選取按鈕 """
        print("TODO: Show task list with searching edit")




if __name__ == '__main__':
    
    from PyQt5.Qt import QApplication

    app = QApplication(sys.argv)

    widget = DailyTaskWidget()
    widget.show()

    app.exec_()



        
        



