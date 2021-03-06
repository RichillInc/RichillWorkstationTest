# -*- encoding: utf-8 -*-

'''
* @File    :   ItemRepository.py
* @Time    :   2021/02/22 08:00:06
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from Devs.Repositories.Repository import Repository
from Devs.Entities.Item import Item

class ItemRepository(Repository):
    """ 品項數據庫訪問器 """

    def __init__(self):
        super(ItemRepository, self).__init__()

    def insert(self, item):
        """ 新增 
        Arguments:
            item (Item): 品項
        """

        itemId = item.getItemId()
        itemName = item.getItemName()

        sql = f"""
        Insert Into Item Values (
            '{itemId}',
            '{itemName}'
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
    
    def deleteByItemId(self, itemId):
        """ 根據品項代號刪除 
        Arguments:
            itemId (str): 品項代號
        """

        sql = f"""
        Delete From Item 
        Where ItemId='{itemId}'
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
        items = []

        sql = "Select * From Item"
        
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
            for itemData in resultSet:
                itemId = itemData[0]
                itemName = itemData[1]

                item = Item(itemId, itemName)
                items.append(item)

        return items                


    def queryByItemId(self, itemId):
        """ 根據品項代號查詢 
        Arguments:
            itemId (str): 品項代號 
        """            



