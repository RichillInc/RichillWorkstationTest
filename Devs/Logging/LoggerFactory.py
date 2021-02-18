# -*- encoding: utf-8 -*-

'''
* @File    :   LoggerFactory.py
* @Time    :   2021/02/17 19:52:21
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from Devs.Logging.Logger import Logger
from Devs.Logging.LogLevel import LogLevel


class LoggerFactory(object):
    """ 日誌器工廠 """



    @staticmethod
    def createLogger(loggerName, logLevel=LogLevel.DEBUG):
        """ 創建日誌器 """
        logger = Logger(loggerName, logLevel)
        return logger


