# -*- encoding: utf-8 -*-

'''
* @File    :   QuotationDetailRepository.py
* @Time    :   2021/02/22 08:31:27
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())

from Devs.Repositories.Repository import Repository
from Devs.Entities.QuotationDetail import QuotationDetail

class QuotationDetailRepository(Repository):
    """ 報價單明細數據庫訪問器 """

    def __init__(self):
        super(QuotationDetailRepository, self).__init__()


    def insert(self, quotationDetail):
        """ 新增 
        Arguments:
            quotationDetail (QuotationDetail): 報價單明細 
            
        """



