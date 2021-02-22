# -*- encoding: utf-8 -*-

'''
* @File    :   QuotationDetail.py
* @Time    :   2021/02/22 08:29:14
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

    def __init__(self,
        quotationId
    ):
        """
        Arguments:
            quotationId (str): 報價單號

        """
        self.__quotationId = quotationId 

    def getQuotationId(self):
        """ 獲取報價單號 """
        return self.__quotationId

    def __str__(self):
        return f"QuotationDetail [quotationId={self.__quotationId}]"        
    



