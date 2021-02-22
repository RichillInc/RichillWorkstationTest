# -*- encoding: utf-8 -*-

'''
* @File    :   Supplier.py
* @Time    :   2021/02/22 06:56:37
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


class Supplier(object):
    """ 供應商 """

    def __init__(self, 
        supplierId,
        supplierName
    ):
        """
        Arguments:
            supplierId (str): 供應商代號
            supplierName (str): 供應商名稱
        """
        self.__supplierId = supplierId
        self.__supplierName = supplierName

    def getSupplierId(self):
        """ 獲取供應商代號 """
        return self.__supplierId

    def getSupplierName(self):
        """ 獲取供應商名稱 """
        return self.__supplierName

    def __str__(self):
        return f"Supplier [supplierId={self.__supplierId}, supplierName={self.__supplierName}]"            