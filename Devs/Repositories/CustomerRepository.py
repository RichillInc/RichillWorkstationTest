# -*- encoding: utf-8 -*-

'''
* @File    :   CustomerRepository.py
* @Time    :   2021/02/22 07:32:06
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from Devs.Entities.Customer import Customer
from Devs.Repositories.Repository import Repository

class CustomerRepository(Repository):
    """ 客戶數據庫訪問器 """

    def __init__(self):
        super(CustomerRepository, self).__init__()


    def insert(self, customer):
        """ 新增 
        Arguments:
            customer (Customer): 客戶
        """
        customerId = customer.getCustomerId()
        customerName = customer.getCustomerName()

        sql = f"""
        Insert Into Customer Values (
            '{customerId}',
            '{customerName}'
        )
        """

        connection, cursor = self._getConnection()

        try:
            cursor.execute(sql)
            connection.commit()
            self._getLogger().info(f"Insert success.")

        except Exception as exception:
            connection.rollback()
            self._getLogger().error(f"Insert failed. [{exception}]")

        finally:
            self._release(connection, cursor)        
    
    def deleteByCustomerId(self, customerId):
        """ 根據客戶代號刪除 
        Arguments:
            customerId (str): 客戶代號
        """
        sql = f"""
        Delete From Customer
        Where CustomerId='{customerId}'
        """
        connection, cursor = self._getConnection()

        try:
            cursor.execute(sql)
            connection.commit()
            self._getLogger().info(f"Delete success.")

        except Exception as exception:
            connection.rollback()
            self._getLogger().error(f"Delete failed. [{exception}]")

        finally:
            self._release(connection, cursor)           

    def queryAll(self):
        """ 查詢全部 """
        customers = []

        sql = "Select * From Customer"
        connection, cursor = self._getConnection()
        try:
            cursor.execute(sql)
            resultSet = cursor.fetchall()
            self._getLogger().info(f"Query success. {len(resultSet)} results found.")

        except Exception as exception:
            connection.rollback()
            self._getLogger().error(f"Query failed. [{exception}]")

        finally:
            self._release(connection, cursor)           

        if resultSet:
            for customerData in resultSet:
                customerId = customerData[0]
                customerName = customerData[1]

                customer = Customer(customerId, customerName) # 創建客戶
                customers.append(customer)
        return customers

    def queryByCustomerId(self, customerId):
        """ 根據客戶代號查詢 
        Arguments:
            customerId (str): 客戶代號
        """
        
        