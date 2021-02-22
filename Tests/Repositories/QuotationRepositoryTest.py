# -*- encoding: utf-8 -*-

'''
* @File    :   QuotationRepositoryTest.py
* @Time    :   2021/02/22 08:25:46
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())

from Devs.Repositories.QuotationRepository import QuotationRepository, Quotation

class QuotationRepositoryTest(object):


    def __init__(self):
        self.quotationRepository = QuotationRepository()


    def insertTest(self):
        """ 新增測試 """

    def deleteByIdTest(self):
        """ 根據代號刪除測試 """

    def queryAllTest(self):
        """ 查詢全部測試 """

    def queryByIdTest(self):
        """ 根據代號查詢測試 """

if __name__ == '__main__':
    test = QuotationRepositoryTest()
    test.insertTest()
    test.deleteByIdTest()
    test.queryAllTest()
    test.queryByIdTest()




