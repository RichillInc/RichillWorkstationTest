# -*- encoding: utf-8 -*-

'''
* @File    :   ItemRepositoryTest.py
* @Time    :   2021/02/22 08:02:25
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from Devs.Repositories.ItemRepository import Item, ItemRepository

class ItemRepositoryTest(object):
    """ 品項數據庫訪問測試 """

    def __init__(self):
        self.itemRepository = ItemRepository()

    def insertTest(self):
        """ 新增測試 """
        items = [
            Item("1110001", "火山爆發"),
            Item("1110002", "東方龍"),
            Item("1110003", "麻眼"),
            Item("1110004", "水手補派"),
            Item("1110005", "奢華"),
            Item("1110006", "AWP狙擊")
        ]
        for item in items:
            self.itemRepository.insert(item)

    def deleteByIdTest(self):
        """ 根據代號刪除測試 """
        itemId = "1110004"
        self.itemRepository.deleteByItemId(itemId)

    def queryAllTest(self):
        """ 查詢全部測試 """
        items = self.itemRepository.queryAll()

    def queryByIdTest(self):
        """ 根據代號查詢測試 """


if __name__ == '__main__':
    
    
    test = ItemRepositoryTest()
    test.insertTest()
    test.deleteByIdTest()
    test.queryAllTest()

