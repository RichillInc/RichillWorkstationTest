# -*- encoding: utf-8 -*-

'''
* @File    :   Item.py
* @Time    :   2021/02/22 00:48:06
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


class Item(object):
    """ 品項 """

    def __init__(self, itemId, itemName):
        """
        Arguments:
            itemId (str): 品項代號
            itemName (str): 品項名稱 
        """
        self.__itemId = itemId
        self.__itemName = itemName

    def getItemId(self):
        """ 獲取品項代號 """
        return self.__itemId

    def getItemName(self):
        """ 獲取品項名稱 """
        return self.__itemName

    def __str__(self):
        return f"Item [itemId={self.__itemId}, itemName={self.__itemName}]"
        
                            

