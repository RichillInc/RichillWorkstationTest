
import numpy


class Series:

    def __init__(self, seriesName="", data=[], indicator=None, default=None):
        """
        Arguments:
            seriesName (str): 序列名稱 
            data (list): 儲存資料的列表
        
        """
        self.__seriesName = seriesName
        self.__default = default

        self.__windowSize = len(data)
        if len(data) == 0:
            self.__data = numpy.array([self.__default] * self.__windowSize)
        else:
            self.__data = data            
        
        self.__indicator = indicator
        self.__currentBarIndex = 0
        self.__realtime = False

    def resetData(self, data, windowSize):
        """ 
        Arguments:
            data (list): 資料列表
            windowSize (int): 窗格大小
        """
        self.__windowSize = windowSize
        if len(data) == 0:
            self.data = numpy.array([self.__default] * self.__windowSize)
        else:
            self.data = data                    


class NumericSeries(Series):
    """ 數字序列 """ 

    def __init__(self, seriesName="", data=[], indicator=None):
        """
        Arguments:
            seriesName (str): 序列名稱 
            data (list): 儲存資料的列表
        
        """        
        super(NumericSeries, self).__init__(seriesName, data, indicator, 0.0)

from datetime import datetime

class DatetimeSeries(Series):
    """ 日期時間序列 """

    def __init__(self, seriesName="", data=[], indicator=None):
        """
        Arguments:
            seriesName (str): 序列名稱 
            data (list): 儲存資料的列表
        
        """        
        super(DatetimeSeries, self).__init__(seriesName, data, indicator, datetime(1980, 1, 1))
