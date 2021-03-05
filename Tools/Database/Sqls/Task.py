# -*- encoding: utf-8 -*-

'''
* @File    :   Task.py
* @Time    :   2021/03/02 02:57:51
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

    CREATE = """
    Create Table If Not Exists Task (
        TaskId Varchar(255),
        TaskName Varchar(255),
        Description Varchar(255)
    )
    """


