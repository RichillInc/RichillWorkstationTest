
# -*- encoding: utf-8 -*-

'''
* @File    :   KBarGenerator.py
* @Time    :   2021/02/20 03:43:27
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from Devs.Entities.KBar import KBar


class KBarGenerator(object):
    """ K線生成器 """

    def __init__(self):
        super(KBarGenerator, self).__init__()

        self.__currentKBar = None
        self.__lastTick = None



    def onTickUpdated(self, tickUpdatedEvent):
        """ 處理Tick更新事件 """
        tick = tickUpdatedEvent.getTick()
        isNewMinute = False

        if not tick.getClose():
            return

        if self.__lastTick and tick.getDatetime() < self.__lastTick.getDatetime():
            return

        if not self.__currentKBar:
            isNewMinute = True
        elif self.__currentKBar.getDatetime().minute != tick.getDatetime().minute or self.__currentKBar.getDatetime().hour != tick.getDatetime().hour:
            self.__currentKBar.setDatetime(self.__currentKBar.getDatetime().replace(second=0, microsecond=0))
            # onBar
            print(self.__currentKBar)
            isNewMinute = True
        
        if isNewMinute:
            self.__currentKBar = KBar(
                tick.getDatetime(),
                tick.getClose(),
                tick.getClose(),
                tick.getClose(),
                tick.getClose()
            )
            print(self.__currentKBar)
        else:
            high = max(self.__currentKBar.getHigh(), tick.getClose())
            low = min(self.__currentKBar.getLow(), tick.getClose())
            close = tick.getClose()
            self.__currentKBar.setDatetime(tick.getDatetime())
            self.__currentKBar.setHigh(high)
            self.__currentKBar.setLow(low)
            self.__currentKBar.setClose(close)

        # 更新成交量
        # if self.__lastTick:
            # volumeChange = tick.getVolume() - self.__lastTick.getVolume()
            # kBarVolume = self.__currentKBar.getVolume() += max(volumeChange, 0)
        self.__lastTick = tick

