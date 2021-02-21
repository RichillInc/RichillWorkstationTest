
# -*- encoding: utf-8 -*-

'''
* @File    :   ItemRepositoryTest.py
* @Time    :   2021/02/22 00:50:04
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())

from Devs.Repositories.ItemRepository import ItemRepository
from Devs.Entities.Item import Item
from Tools.initDb import initDb

class ItemRepositoryTest(object):
    """ 品項數據庫測試 """

    def __init__(self):
        initDb()
        self.itemRepository = ItemRepository()

    def insertTest(self):
        """ 新增測試 """
        item = Item("1110001", "煙霧火山")
        self.itemRepository.insert(item) 
        item = Item("1110002", "東方龍")
        self.itemRepository.insert(item)         

    def queryByItemIdTest(self):
        """ 根據品項代號查詢測試 """
        itemId = "1110001"
        item = self.itemRepository.queryByItemId(itemId)

    def queryByItemNameTest(self):
        """ 根據品項名稱查詢測試 """
        itemName = "煙霧火山"
        item = self.itemRepository.queryByItemName(itemName)

    def queryAllTest(self):
        """ 查詢全部測試 """
        items = self.itemRepository.queryAll()

        for item in items:
            print(item)

    def deleteItemByIdTest(self):
        """ 根據品項代號刪除品項測試 """
        itemId = "1110001"
        self.itemRepository.deleteByItemId(itemId)
        itemId = "1110002"
        self.itemRepository.deleteByItemId(itemId)
        

if __name__ == '__main__':
    
    
    test = ItemRepositoryTest()
    test.insertTest()
    test.deleteItemByIdTest()
    test.queryAllTest()

    test.insertTest()
    test.queryByItemIdTest()
    test.queryByItemNameTest()





