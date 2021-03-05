# -*- encoding: utf-8 -*-

'''
* @File    :   TaskRepository.py
* @Time    :   2021/03/02 02:52:39
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from Devs.Repositories.Repository import Repository



class TaskRepository(Repository):
    """ 任務數據庫 """

    def __init__(self):
        super(TaskRepository, self).__init__()

    def insert(self, task):
        """ 新增 """
        taskId = task.getTaskId()
        taskName = task.getTaskName()
        description = task.getDescription()

        sql = f"""
        Insert Into Task Values (
            '{taskId}',
            '{taskName}',
            '{description}'
        )
        """


