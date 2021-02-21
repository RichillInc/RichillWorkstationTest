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
        itemId = "1110003"
        itemName = "M72火箭彈"
        self.itemService.addItem(itemId, itemName)


if __name__ == '__main__':
    
    
    test = ItemServiceTest()
    test.addItemTest()


