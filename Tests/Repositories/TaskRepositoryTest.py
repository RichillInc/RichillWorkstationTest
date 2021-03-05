# -*- encoding: utf-8 -*-

'''
* @File    :   TaskRepositoryTest.py
* @Time    :   2021/03/02 02:54:52
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())

from Devs.Repositories.TaskRepository import TaskRepository
from Devs.Entities.Task import Task

class TaskRepositoryTest(object):
    """ 任務數據庫測試 """

    def __init__(self):
        self.taskRepository = TaskRepository()

    def insertTest(self):
        """ 新增任務測試 """

        tasks = [
            Task(1, "Task01", ""),
            Task(2, "Task02", ""),
            Task(3, "Task03", "")
        ]

        for task in tasks:
            self.taskRepository.insert(task)
        

    def deleteTest(self):
        """ 刪除任務測試 """    

    def queryByIdTest(self):
        """ 根據代號查詢測試 """

    def queryAllTest(self):
        """ 查詢全部測試 """        


if __name__ == '__main__':
    
    
    test = TaskRepositoryTest()
    test.insertTest()