# -*- encoding: utf-8 -*-

'''
* @File    :   Supplier.py
* @Time    :   2021/02/22 06:58:13
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
    CREATE = """
    Create Table If Not Exists Supplier (
        SupplierId Varchar(255),
        SupplierName Varchar(255)
    )
    """

