# -*- encoding: utf-8 -*-

'''
* @File    :   QuotationDetailRepositoryTest.py
* @Time    :   2021/02/22 08:27:38
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())

from Devs.Repositories.QuotationDetailRepository import QuotationDetail, QuotationDetailRepository

class QuotationDetailRepositoryTest(object):
    """ 報價單明細數據庫訪問測試 """

    def __init__(self):
        self.quotationDetailRepository = QuotationDetailRepository()

    def insertTest(self):
        """ 新增測試 """
        quotationId = "Q202102230001"
        
        quotationDetails = [
            QuotationDetail(quotationId, "東方龍", 2, "支", 2980, 5960, ""),
            QuotationDetail(quotationId, "BongMate", 3, "罐", 420, 1260, ""),

        ]

        for quotationDetail in quotationDetails:
            self.quotationDetailRepository.insert(quotationDetail)

    def deleteByIdTest(self):
        """ 根據代號刪除測試 """

    def queryAllTest(self):
        """ 查詢全部測試 """

    def queryByIdTest(self):
        """ 根據代號查詢測試 """

if __name__ == '__main__':
    test = QuotationDetailRepositoryTest()
    test.insertTest()
    test.deleteByIdTest()
    test.queryAllTest()
    test.queryByIdTest()


