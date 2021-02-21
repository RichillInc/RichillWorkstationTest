# -*- encoding: utf-8 -*-

'''
* @File    :   ItemServiceTest.py
* @Time    :   2021/02/22 01:13:36
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from Devs.Services.ItemService import ItemService

class ItemServiceTest(object):
    """ 品項服務測試 """

    def __init__(self):
        self.itemService = ItemService()
        
    def addItemTest(self):
        """ 新增品項測試 """
        itemId = "1110004"
        itemName = "MP5 衝鋒槍"
        operationResult = self.itemService.addItem(itemId, itemName)
        print(operationResult)

    def findAllItemsTest(self):
        """ 查詢所有品項測試 """
        operationResult = self.itemService.findAllItems()
        items = operationResult.getData()
        for item in items:
            print(item)

    def deleteItemByIdTest(self):
        """ 根據品項代號刪除品項測試 """
        itemId = "1110002"
        operationResult = self.itemService.deleteItemByItemId(itemId)
        print(operationResult)


if __name__ == '__main__':
    
    
    test = ItemServiceTest()
    test.addItemTest()
    test.findAllItemsTest()
    test.deleteItemByIdTest()


