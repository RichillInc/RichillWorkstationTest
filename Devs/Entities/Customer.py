# -*- encoding: utf-8 -*-

'''
* @File    :   Customer.py
* @Time    :   2021/02/22 06:52:11
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


class Customer(object):
    """ 客戶 """

    def __init__(self,
        customerId,
        customerName
    ):
        """
        Arguments:
            customerId (str): 客戶代號
            customerName (str): 客戶名稱
        """
        self.__customerId = customerId
        self.__customerName = customerName

    def getCustomerId(self):
        """ 獲取客戶代號 """
        return self.__customerId

    def getCustomerName(self):
        """ 獲取客戶名稱 """
        return self.__customerName

    def __str__(self):
        return f"Customer [customerId={self.__customerId}, customerName={self.__customerName}]"            


