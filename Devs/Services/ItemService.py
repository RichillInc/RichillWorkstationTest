# -*- encoding: utf-8 -*-

'''
* @File    :   ItemService.py
* @Time    :   2021/02/22 01:12:22
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())

from Devs.Logging.LoggerFactory import LoggerFactory

from Devs.Entities.Item import Item
from Devs.Services.Service import Service
from Devs.Repositories.ItemRepository import ItemRepository

class ItemService(Service):
    """ 品項服務 """

    def __init__(self):
        self.__logger = LoggerFactory.createLogger(self.__class__.__name__)
        self.__itemRepository = ItemRepository()

    def addItem(self, itemId, itemName):
        """ 新增品項 
        Arguments:
            itemId (str): 品項代號
            itemName (str): 品項名稱
        """

        if self.isItemIdExists(itemId):
            self.__logger.error("Add item failed. ItemId exists.")
            return False
        if self.isItemNameExists(itemName):
            self.__logger.error("Add item failed. ItemName exists.")  
            return False

        item = Item(itemId, itemName)
        self.__itemRepository.insert(item)    
        self.__logger.info(f"Add item success. {item}")
        return True        
        
    def isItemIdExists(self, itemId):
        """
        判斷品項代號是否存在
        Arguments:
            itemId (str): 品項代號
        """        
        item = self.__itemRepository.queryByItemId(itemId)
        if item:
            return True
        return False

    def isItemNameExists(self, itemName):
        """
        判斷品項名稱是否重複
        Arguments:
            itemName (str): 品項名稱
        """    
        item = self.__itemRepository.queryByItemName(itemName)
        if item:
            return True
        return False    





