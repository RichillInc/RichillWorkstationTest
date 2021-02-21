# -*- encoding: utf-8 -*-

'''
* @File    :   Item.py
* @Time    :   2021/02/22 00:19:22
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


class Item(object):
    """ 品項表 """
    CREATE = """
    Create Table If Not Exists Item (
        ItemId Varchar(255),
        ItemName Varchar(255)
    )
    """

