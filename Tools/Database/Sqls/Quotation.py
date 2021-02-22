# -*- encoding: utf-8 -*-

'''
* @File    :   Quotation.py
* @Time    :   2021/02/22 08:24:50
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


class Quotation(object):
    """ 報價單 """
    CREATE = """
    Create Table If Not Exists Quotation (
        QuotationId Varchar(255),
        Date Date
    )"""


