# -*- encoding: utf-8 -*-

'''
* @File    :   Task.py
* @Time    :   2021/03/02 02:34:49
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


class Task(object):


    def __init__(self,
        taskId,
        taskName,
        deadline,
        description
    ):
        """
        Arguments:
            taskId (int): 任務編號
            taskName (str): 任務名稱
            deadline (date): 期限
            description (str): 任務說明
        """
        self.__taskId = taskId
        self.__taskName = taskName
        self.__deadline = deadline
        self.__description = description


    def getTaskId(self):
        """ 獲取任務代號 """
        return self.__taskId

    def getTaskName(self):
        """ 獲取任務名稱 """
        return self.__taskName

    def getDeadline(self):
        """ 獲取期限 """
        return self.__deadline

    def getDescription(self):
        """ 獲取任務說明 """
        return self.__description

    def __str__(self):
        return f"Task [taskId={self.__taskId}, taskName={self.__taskName}, deadline={self.__deadline}, description={self.__description}]"








