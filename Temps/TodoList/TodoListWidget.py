# -*- encoding: utf-8 -*-

'''
* @File    :   TodoListWidget.py
* @Time    :   2021/03/01 05:43:26
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from PyQt5.Qt import QListWidget, QListWidgetItem, QSize
from Temps.TimeManager.TodoListWidgetItem import TodoListWidgetItem


class TodoListWidget(QListWidget):
    """ 代辦事項清單小部件 """

    def __init__(self):
        super(TodoListWidget, self).__init__()

    def addTodo(self, title, isDone):
        """
        新增代辦事項
        Arguments:  
            title (str): 標題
            isDone (bool): 是否完成
        """            
        todoListWidgetItem = TodoListWidgetItem(title, isDone)
        self._addTodoListWidgetItem(todoListWidgetItem)

    def _addTodoListWidgetItem(self, todoListWidgetItem):
        """
        新增代辦清單列表項目
        Arguments:
            todoListWidgetItem (TodoListWidgetItem): 代辦清單列表項目
        """
        listWidgetItem = QListWidgetItem()
        listWidgetItem.setSizeHint(
            QSize(
                self.width(), 
                60
            )
        )
        self.addItem(listWidgetItem)
        self.setItemWidget(listWidgetItem, todoListWidgetItem)

    def _setTodoListWidgetItems(self, todoListWidgetItems):
        """
        設置代辦清單列表項目
        Arguments:
            todoListWidgetItems (List[TodoListWidgetItem]): 代辦清單列表項目的列表
        """
        for todoListWidgetItem in todoListWidgetItems:
            self.addTodoListWidgetItem(todoListWidgetItem)



