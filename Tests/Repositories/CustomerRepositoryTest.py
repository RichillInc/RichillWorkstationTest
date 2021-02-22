# -*- encoding: utf-8 -*-

'''
* @File    :   CustomerRepositoryTest.py
* @Time    :   2021/02/22 07:39:04
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from Devs.Repositories.CustomerRepository import CustomerRepository, Customer

class CustomerRepositoryTest(object):
    """ 客戶數據庫訪問類測試 """

    def __init__(self):
        self.customerRepository = CustomerRepository()

    def insertTest(self):
        """ 新增測試 """

        customers = [
            Customer("001", "測試客戶1"),
            Customer("002", "測試客戶2"),
            Customer("003", "測試客戶3"),
            Customer("004", "測試客戶4"),
            Customer("005", "測試客戶5"),
            Customer("006", "測試客戶6"),
            Customer("007", "測試客戶7"),
            Customer("008", "測試客戶8"),
        ]    

        for customer in customers:
            self.customerRepository.insert(customer)

    def deleteByIdTest(self):
        """ 根據代號刪除測試 """
        customerId = "007"
        self.customerRepository.deleteByCustomerId(customerId)

    def queryAllTest(self):
        """ 查詢全部測試 """
        customers = self.customerRepository.queryAll()
        for customer in customers:
            print(customer)

    def queryByIdTest(self):
        """ 根據代號查詢測試 """
        customerId = "003"
        customer = self.customerRepository.queryByCustomerId(customerId)


if __name__ == '__main__':
    
    test = CustomerRepositoryTest()
    test.insertTest() 
    test.deleteByIdTest()


    test.queryAllTest()
