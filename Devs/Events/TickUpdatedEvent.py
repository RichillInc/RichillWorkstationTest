# -*- encoding: utf-8 -*-

'''
* @File    :   TickUpdatedEvent.py
* @Time    :   2021/02/20 03:47:36
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())


class TickUpdatedEvent(object):
    """ 成交明細更新事件 """

    def __init__(self, tick):
        """
        Arguments:
            tick (Tick): 成交明細
        """
        super(TickUpdatedEvent, self).__init__()
        self.__tick = tick

    def getTick(self):
        """ 獲取成交明細 """
        return self.__tick

    def __str__(self):
        return f"TickUpdatedEvent [tick={self.__tick}]"
        


