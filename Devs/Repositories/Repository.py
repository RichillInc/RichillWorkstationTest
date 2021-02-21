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

class Repository(object):
    """ 數據庫訪問 """

    def _getConnection(self):
        connection = mysql.connect(**DatabaseConfig.LOCAL_HOST)
        cursor = connection.cursor()
        cursor.execute("Use BusinessTest")
        return connection, cursor

