# -*- encoding: utf-8 -*-

'''
* @File    :   Quotation.py
* @Time    :   2021/02/22 08:22:18
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

    def __init__(self,
        quotationId,
        date
    ):
        """
        Arguments:
            quotationId (str): 報價單號
            date (date): 報價日期
        """

        self.__quotationId = quotationId
        self.__date = date

    def getQuotationId(self):
        """ 獲取報價單號 """
        return self.__quotationId

    def getDate(self):
        """ 獲取報價日期 """
        return self.__date        

    def __str__(self):
        return f"Quotation [quotationId={self.__quotationId}, date={self.__date}]"



