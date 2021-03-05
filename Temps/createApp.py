

# -*- encoding: utf-8 -*-

'''
* @File    :   createApp.py
* @Time    :   2020/11/21 08:00:47
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from PyQt5.Qt import QApplication, QFont, QFile, QIODevice, QTextStream, QSplashScreen


class QssName:
    """ Qt樣式表名稱 """


    FIBRARY = "Fibrary" # 深黑紅 **
    PHOTOXO = "Photoxo" # 金屬黑灰 **
    TAKEZO = "Takezo" # 海軍藍 **
    HOOKMARK = "Hookmark" # 藍紫色     字體太黑 
    OBIT = "Obit" # 深紫色 * 字體太黑 
    COMBINEAR = "Combinear" # 淺灰風格 ComboBox需要調整
    DIFFNES = "Diffnes" # 深黑風格 * ComboBox 需要調整    
    
    DEEP_BOX = "DeepBox" # 淺灰風格 字體太黑
    DEVSION = "Devsion"  # 青澀風格 字體不清楚
    FIBERS = "Fibers" # 紅色 ComboBox 需調整
    GENETIVE = "Genetive" # 黑橘  須調整Label字體大小
    PIC_PAX = "PicPax" # 淺灰 字體顏色需調整
    SY_NET = "SyNet"  # 黑紅 須調整字體 PushButton大小

    NO_QSS = None




class App(QApplication):
    """ 應用程序 """

    def __init__(self):
        super(App, self).__init__(sys.argv)

        font = QFont("微軟正黑體", 10)
        self.setFont(font)
        self.setStyle("fusion")
        # 設置Qss        
        qssName = QssName.TAKEZO  # QSS名稱
        if qssName:
            filePath = f"Qss\{qssName}.qss" # 檔案路徑
            qssFile = QFile(filePath) # 創建Qss檔案對象
            qssFile.open(QIODevice.ReadOnly) # 開啟Qss檔案
            stylesheet = QTextStream(qssFile).readAll() # 讀取Qss
            self.setStyleSheet(stylesheet)
        
    def run(self, widget):
        """ 運行 """
        try:
            splashWindow = QSplashScreen()
            splashWindow.show()
            splashWindow.finish(widget)
            widget.showFullScreen()
            
            return self.exec_()
        except:
            pass
        


def createApp():
    app = App()
    return app
