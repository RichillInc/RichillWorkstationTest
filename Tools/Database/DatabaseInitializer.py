# -*- encoding: utf-8 -*-

'''
* @File    :   DatabaseInitializer.py
* @Time    :   2020/06/27 16:42:41
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''

import os
import sys
sys.path.append(os.getcwd())
import mysql.connector
from Tools.Database.CreateTableSqls import CreateTableSqls

class DatabaseInitializer(object):
    """ 數據庫初始化 """

    def __init__(self, config):
        """ 初始化數據庫配置 """
        self.config = config
        self.connection = None
        self.cursor = None

    def initializeDatabase(self):
        """ 運行 """
        print("\n---------- %s running ----------\n" % self.__class__.__name__)
        self.createConnection(self.config.LOCAL_HOST)
        self.resetDatabase(self.config.DEFAULT_DATABASE_NAME)
        self.createTables()
        # 顯示運行結果
        self.showDatabases()
        self.showTables()
        self.closeConnection()

# ============================== 執行過程 ==============================
    def resetDatabase(self, databaseName):
        """ 重設數據庫 """
        print("\nReset database. DatabaseName = %s\n" % databaseName)
        sqls = [
            "Drop Database If Exists %s" % databaseName,
            "Create Database If Not Exists %s" % databaseName,
            "Use %s" % databaseName
        ]
        self.executeMany(sqls)
        
    def createTables(self):
        """ 創建數據表 """
        
        print("\nCreate tables.")
        for table in CreateTableSqls.SQLS.values():
            sql = table.CREATE
            self.execute(sql)
        print("Tables created.\n")

# ============================== 基本操作方法 ==============================
    def execute(self, sql):
        """ 執行SQL """
        try:
            self.cursor.execute(sql)
            
        except Exception as exception:
            print("Execute failed.", exception)

    def executeMany(self, sqls):
        """ 執行多個SQL """
        for sql in sqls:
            self.execute(sql)
        print("All sqls executed.\n")

    def closeConnection(self):
        """ 關閉數據庫連接 """
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
        print("\nConnection closed.\n\n")

    def createConnection(self, connectionConfig):
        """ 建立數據庫連接 """
        try:
            self.connection = mysql.connector.connect(**connectionConfig)    
            self.cursor = self.connection.cursor()
            print("Database connected. Config = %s" % connectionConfig)

        except Exception as exception:
            print("Connect failed. %s" % exception)

    def showDatabases(self):
        """ 顯示所有數據庫 """
        print("\n---------- All Databases ----------")
        self.cursor.execute("Show Databases")          
        for result in self.cursor:
            databaseName = result[0]
            print(databaseName)

    def showTables(self):
        """ 顯示所有資料表 """
        print("\n---------- All Tables ----------")
        self.cursor.execute("Show Tables")          
        for result in self.cursor:
            tableName = result[0]
            print(tableName)

            