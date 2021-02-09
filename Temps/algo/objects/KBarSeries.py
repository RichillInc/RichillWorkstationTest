
import numpy

class KBarSeries:
    """ K棒數列 
    用於儲存K棒開高低收量數列
    """

    def __init__(self, maximumLength=1024):
        """
        Arguments:
            maximumLength: int 序列的最大長度, 預設為1024
        """

        # 判斷是否有效的最大長度
        
        
        if self.__isValidMaximumLength(maximumLength):
            self.__openArray = numpy.zeros(maximumLength)
            self.__highArray = numpy.zeros(maximumLength)
            self.__lowArray = numpy.zeros(maximumLength)
            self.__closeArray = numpy.zeros(maximumLength)
            self.__volumeArray = numpy.zeros(maximumLength)

    
    def __isValidMaximumLength(self, maximumLength):
        """ 判斷最大長度是否有效 """
        if not maximumLength > 0:
            raise ValueError("Maximum length must > 0")
        else:
            return True




    def getOpen(self):
        """ 獲取開盤價 """
        return self.__openArray

    def getHigh(self):
        """ 獲取最高價 """
        return self.__highArray

    def getLow(self):
        """ 獲取最低價 """
        return self.__lowArray

    def getClose(self):
        """ 獲取收盤價 """
        return self.__closeArray

    def getVolume(self):
        """ 獲取成交量 """
        return self.__volumeArray          

    def addKBar(self, kBar):
        """ 新增K棒 """
        
        self.__openArray[:-1] = self.__openArray[1:]
        self.__highArray[:-1] = self.__highArray[1:]
        self.__lowArray[:-1] = self.__lowArray[1:]
        self.__closeArray[:-1] = self.__closeArray[1:]
        self.__volumeArray[:-1] = self.__volumeArray[1:]

        # 新增K棒資料到數列
        self.__openArray[-1] = kBar.getOpen()
        self.__highArray[-1] = kBar.getHigh()
        self.__lowArray[-1] = kBar.getLow()
        self.__closeArray[-1] = kBar.getClose()
        self.__volumeArray[-1] = kBar.getVolume()



    def __str__(self):
        return f"""
KBarSeries
    Open: {self.getOpen()}, 
    High: {self.getHigh()}, 
    Low: {self.getLow()}
    Close: {self.getClose()}
    Volume: {self.getVolume()}        
        
        """        

