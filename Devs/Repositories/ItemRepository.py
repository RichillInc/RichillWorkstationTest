# -*- encoding: utf-8 -*-

'''
* @File    :   ItemRepository.py
* @Time    :   2021/02/22 00:44:06
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from Devs.Logging.LoggerFactory import LoggerFactory

from Devs.Repositories.Repository import Repository
from Devs.Entities.Item import Item

class ItemRepository(Repository):
    """ 品項數據庫 """

    def __init__(self):
        self.__logger = LoggerFactory.createLogger(self.__class__.__name__)

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
            self.__logger.info(f"Insert {item} success.")
            return True
        except Exception as exception:
            connection.rollback()
            self.__logger.error(f"Insert {item} failed. [{exception}]")
            return False
        finally:
            cursor.close()
            connection.close()

    def deleteByItemId(self, itemId):
        """ 根據品項代號刪除 
        Arguments:
            itemId (str): 品項代號
        """        
        sql = f"""
        Delete From Item Where ItemId='{itemId}'
        """

        connection, cursor = self._getConnection()

        try:
            cursor.execute(sql)
            connection.commit()
            self.__logger.info(f"Delete by itemId({itemId}) success. itemId={itemId}")
        except Exception as exception:
            connection.rollback()
            self.__logger.error(f"Delete by itemId({itemId}) failed. [{exception}]")
        finally:
            cursor.close()
            connection.close()   

    def queryAll(self):
        """ 查詢全部 """
        sql = """
        Select * From Item
        """
        items = []
        connection, cursor = self._getConnection()
        try:
            cursor.execute(sql)
            resultSet = cursor.fetchall()
            if resultSet:
                for itemData in resultSet:
                    itemId = itemData[0]
                    itemName = itemData[1]
                    item = Item(itemId, itemName)
                    items.append(item)
            self.__logger.info(f"Query all items success. {len(resultSet)} items found.")
            return items    
        
        except Exception as exception:
            self.__logger.error(f"Query all items failed. [{exception}]")
        
        finally:
            cursor.close()
            connection.close()                

    def queryByItemId(self, itemId):
        """ 根據品項代號查詢 
        Arguments:
            itemId (str): 品項代號
        """
        
        sql = f"""
        Select * From Item
        Where ItemId='{itemId}'
        """
        connection, cursor = self._getConnection()

        try:
            cursor.execute(sql)
            resultSet = cursor.fetchall()
            if resultSet:
                itemData = resultSet[0]
                itemId = itemData[0]
                itemName = itemData[1]
                
                item = Item(itemId, itemName)
                self.__logger.info(f"Query by itemId({itemId}) sucess. {len(resultSet)} item found.")
                return item
            else:
                self.__logger.info(f"ItemId({itemId}) not found.")   
                return None 
            
        except Exception as exception:
            self.__logger.error(f"Query by itemId failed. [{exception}]")
            return False
        finally:
            cursor.close()
            connection.close()        

    def queryByItemName(self, itemName):
        """ 根據品項名稱查詢 
        Arguments:
            itemName (str): 品項名稱
        """

        sql = f"""
        Select * From Item
        Where itemName='{itemName}'
        """
        connection, cursor = self._getConnection()

        try:
            cursor.execute(sql)
            resultSet = cursor.fetchall()
            if resultSet:
                itemData = resultSet[0]
                itemId = itemData[0]
                itemName = itemData[1]
                item = Item(itemId, itemName)
                self.__logger.info(f"Query by itemName({itemName}) success. {len(resultSet)} item found.")
                return item
            else:
                self.__logger.info(f"ItemName({itemName}) not found.")   
                return None 
            
        except Exception as exception:
            self.__logger.error(f"Query by itemName({itemName}) failed. [{exception}]")
            return False
        finally:
            cursor.close()
            connection.close()    

                     