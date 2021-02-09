# -*- encoding: utf-8 -*-

'''
* @File    :   KBarUpdatedEvent.py
* @Time    :   2021/02/09 21:33:21
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


class KBarUpdatedEvent(object):
    """ K線數據更新事件 """

    def __init__(self, kBar):
        """ 
        Arguments:
            kBar: KBar() 新的K線對象
        """
        self.__kBar = kBar


    def getKBar(self):
        """ 獲取K線 """
        return self.__kBar
                    