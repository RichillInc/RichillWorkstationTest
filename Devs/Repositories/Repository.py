# -*- encoding: utf-8 -*-

'''
* @File    :   Repository.py
* @Time    :   2021/02/22 00:45:21
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
import mysql.connector as mysql 
from Tools.Database.DatabaseConfig import DatabaseConfig
from Devs.Logging.LoggerFactory import LoggerFactory

class Repository(object):
    """ 數據庫訪問基類, 所有數據庫訪問類別必須繼承此類別 """

    def __init__(self):
        self.__logger = LoggerFactory.createLogger(self.__class__.__name__)

    def _getLogger(self):
        """ 獲取日誌器 """
        return self.__logger

    def _getConnection(self):
        """ 獲取數據庫連接 """
        connection = mysql.connect(**DatabaseConfig.LOCAL_HOST)
        cursor = connection.cursor()
        cursor.execute("Use BusinessTest")
        return connection, cursor

    def _release(self, connection, cursor):
        """ 釋放資源 
        Arguments:
            connection (MySqlConnection): 數據庫連接
            cursor (MySqlCursor): 數據庫指標對象
        """
        if cursor:
            cursor.close()
        if connection:
            connection.close()        

