# -*- encoding: utf-8 -*-

'''
* @File    :   User.py
* @Time    :   2021/02/11 20:47:18
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


class User(object):
    """ 使用者 """

    def __init__(self, userId):
        """ 實例化方法
        Arguments:
            userId (str): 使用者代號

        """
        
        self.__userId = userId


    def __str__(self):
        return f"User [userId={self.__userId}]"
        


