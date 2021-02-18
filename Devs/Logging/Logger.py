# -*- encoding: utf-8 -*-

'''
* @File    :   Logger.py
* @Time    :   2021/02/17 19:52:06
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
import ctypes
from logging import Logger as PythonLogger
from logging import FileHandler, StreamHandler, Formatter
from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL

from Devs.Logging.LogLevel import LogLevel
from Devs.Logging.LogLevelColor import LogLevelColor




class Logger(PythonLogger):
    """ 日誌器 """

    # TODO: 日誌顏色分級
    # TODO: 檔案日誌
    __DEFAULT_LOG_FORMAT = "%(asctime)s - [%(name)s] [%(levelname)s]: %(message)s"
    __DEFAULT_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
    __logLevelMap = {
        LogLevel.DEBUG: DEBUG,
        LogLevel.INFO: INFO,
        LogLevel.WARNING: WARNING,
        LogLevel.ERROR: ERROR,
        LogLevel.CRITICAL: CRITICAL
    }
    
    def __init__(self, loggerName, logLevel):
        """
        Arguments:
            loggerName (str): 日誌器名稱 
            logLevel (LogLevel): 日誌等級
        """
        super(Logger, self).__init__(loggerName)
        self.__loggerName = loggerName
        self.__logLevel = logLevel

        self.__formatter = self.__createLogFormatter(Logger.__DEFAULT_LOG_FORMAT, Logger.__DEFAULT_DATETIME_FORMAT)

        self.__streamHandler = StreamHandler() # 創建Terminal處理器
        self.__streamHandler.setFormatter(self.__formatter) # 設置格式化器

        # TODO: 設定檔案日誌        
        # self.__fileHandler = FileHandler(filepath)
        # self.__fileHandler.setFormatter(self.__formatter)

        self.setLogLevel(logLevel) # 設置日誌等級
        self.addHandler(self.__streamHandler)

    def getLoggerName(self):
        """ 獲取日誌器名稱 """
        return self.__loggerName        

    def setLogLevel(self, logLevel):
        """ 設置日誌器等級 
        Arguments:
            logLevel (LogLevel): 日誌等級 
        """
        self.__logLevel = logLevel
        level = Logger.__logLevelMap[logLevel]
        super().setLevel(level)

    def __createLogFormatter(self, logFormat, datetimeFormat):
        """ 創建日誌格式化器
        Arguments:
            logFormate (str): 日誌格式
            datetimeFormat (str): 時間日期格式
        """
        logFormatter = Formatter(logFormat, datetimeFormat)
        return logFormatter


    def __setLogLevelColor(self, logLevelColor):
        """
        設置終端機日誌輸出顏色
        Arguments:
            color (LogLevelColor): 日誌等級顏色
        """
        return ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11), logLevelColor.value)    

    def debug(self, message):
        """ 輸出Debug級別日誌
        message (str): 日誌訊息
        """    
        self.__setLogLevelColor(LogLevelColor.DEBUG)  
        super().debug(message)
        self.__setLogLevelColor(LogLevelColor.DEBUG)

    def info(self, message):
        """ 輸出Info級別日誌 
        message (str): 日誌訊息
        """
        self.__setLogLevelColor(LogLevelColor.INFO)           
        super().info(message)
        self.__setLogLevelColor(LogLevelColor.DEBUG)

    def warning(self, message):
        """ 輸出Warning級別日誌 
        message (str): 日誌訊息
        """
        self.__setLogLevelColor(LogLevelColor.WARNING)          
        super().warning(message)
        self.__setLogLevelColor(LogLevelColor.DEBUG)

    def error(self, message):
        """ 輸出Error級別日誌 
        message (str): 日誌訊息
        """
        self.__setLogLevelColor(LogLevelColor.ERROR) 
        super().error(message)
        self.__setLogLevelColor(LogLevelColor.DEBUG)
        
    def critical(self, message):
        """ 輸出Critical級別日誌 
        message (str): 日誌訊息
        """
        self.__setLogLevelColor(LogLevelColor.CRITICAL)   
        super().critical(message)  
        self.__setLogLevelColor(LogLevelColor.DEBUG)  
                  
    def __str__(self):
        return f"Logger [loggerName={self.__loggerName}, logLevel={self.__logLevel}]"
