# -*- encoding: utf-8 -*-

'''
* @File    :   QuotationDetail.py
* @Time    :   2021/02/22 08:28:32
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


class QuotationDetail(object):
    """ 報價單明細 """
    CREATE = """
    Create Table If Not Exists QuotationDetail (
        QuotationId Varchar(255)
    )
    """

