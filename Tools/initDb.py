
# -*- encoding: utf-8 -*-

'''
* @File    :   main.py
* @Time    :   2020/06/27 22:27:35
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''

import os
import sys
sys.path.append(os.getcwd())
from DevTools.Database.DatabaseConfig import DatabaseConfig
from DevTools.Database.DatabaseInitializer import DatabaseInitializer


def initDb():
    config = DatabaseConfig
    databaseInitializer = DatabaseInitializer(config)
    databaseInitializer.initializeDatabase()


if __name__ == "__main__":
    initDb()