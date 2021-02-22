# -*- encoding: utf-8 -*-

'''
* @File    :   Customer.py
* @Time    :   2021/02/22 06:48:28
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

    CREATE = """
    Create Table If Not Exists Customer (
        CustomerId Varchar(255),
        CustomerName Varchar(255)
    )
    """

