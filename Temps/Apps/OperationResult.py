# -*- encoding: utf-8 -*-

'''
* @File    :   OperationResult.py
* @Time    :   2021/02/22 04:53:22
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


class OperationResult(object):
    """ 操作結果 """

    def __init__(self, operationResultType, data, message):

        """
        Arguments:
            operationResultType (OperationResultType): 操作結果類型
            data (any): 操作結果返回的數據
            message (str): 操作結果返回的訊息
        """
        self.__operationResultType = operationResultType
        self.__data = data
        self.__message = message

    def getOperationResultType(self):
        """ 獲取操作結果類型 """
        return self.__operationResultType

    def getMessage(self):
        """ 獲取訊息 """
        return self.__message

    def getData(self):
        """ 獲取操作返回的數據 """
        return self.__data

    def __str__(self):
        return f"OperationResult [operationResultType={self.__operationResultType}, data={self.__data}, message={self.__message}]"    
    
    



