# -*- encoding: utf-8 -*-

'''
* @File    :   QuotationRepository.py
* @Time    :   2021/02/22 08:21:24
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from Devs.Repositories.Repository import Repository
from Devs.Entities.Quotation import Quotation


class QuotationRepository(Repository):
    """ 報價單數據庫訪問器 """

    def __init__(self):
        super(QuotationRepository, self).__init__()


    def insert(self, quotation):
        """ 新增 
        Arguments:
            quotation (Quotation): 報價單
        """

        


