# -*- encoding: utf-8 -*-

'''
* @File    :   Task.py
* @Time    :   2021/03/02 03:01:06
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


class Task(object):
    """ 任務 """

    def __init__(self,
        taskId,
        taskName,
        description
    ):
        """
        Arguments:
            taskId (str): 任務代號
            taskName (str): 任務名稱
            description (str): 任務說明
        """
        self.__taskId = taskId
        self.__taskName = taskName
        self.__description = description


    def getTaskId(self):
        """ 獲取任務代號 """
        return self.__taskId

    def getTaskName(self):
        """ 獲取任務名稱 """
        return self.__taskName

    def getDescription(self):
        """ 獲取任務說明 """
        return self.__description

    def __str__(self):
        return f"Task [taskId={self.__taskId}, taskName={self.__taskName}, description={self.__description}]"

        




