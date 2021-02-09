# -*- encoding: utf-8 -*-

'''
* @File    :   StrategyParameter.py
* @Time    :   2021/02/09 23:55:56
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


class StrategyParameter(object):
    """ 策略參數 """

    def __init__(self, parameterName, parameterValue):
        """
        Arguments:
            parameterName str: 參數名稱
            parameterValue float: 參數數值
        """
        self.__parameterName = parameterName 
        self.__parameterValue = parameterValue


    def getParameterName(self):
        """ 獲取參數名稱 """
        return self.__parameterName

    def getParmeterValue(self):
        """ 獲取參數數值 """
        return self.__parameterValue

    def setParameterValue(self, parmaeterValue):
        """ 設置參數數值 
        Arguments:
            parmaeterValue: any 參數數值
        """
        self.__parameterValue = parmaeterValue
