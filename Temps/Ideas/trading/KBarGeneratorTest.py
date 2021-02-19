# -*- encoding: utf-8 -*-

'''
* @File    :   KBarGeneratorTest.py
* @Time    :   2021/02/20 03:45:27
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
from PyQt5.Qt import *
from Devs.Events.TickUpdatedEvent import TickUpdatedEvent
from Devs.Apis.SinopacApi import SinopacApi
from Temps.Ideas.trading.KBarGenerator import KBarGenerator
from Devs.Entities.Tick import Tick
from datetime import datetime



class KBarGeneratorTest(QWidget):

    def __init__(self):
        super(KBarGeneratorTest, self).__init__()

        self.api = SinopacApi()
        self.api.login("P123622990", "among7201")
        self.api.downloadAllContracts()
        self.api.setQuoteCallback(self.onQuote)
        self.kBarGenerator = KBarGenerator()

        self.startButton = QPushButton("Start")
        self.startButton.clicked.connect(self.onStart)
        self.informationWidget = QTextEdit()

        layout = QGridLayout(self)
        layout.addWidget(self.startButton)
        layout.addWidget(self.informationWidget)
    
    def onStart(self):
        """"""
        txf = self.api.Contracts.Futures['TXF']['TXF202103']
        self.api.quote.subscribe(txf, "tick")

        
      

    def onQuote(self, topic, data):
        """"""
        try:
            quoteType = topic.split("/")[0]
            tick = None
            if quoteType == "L":
                tick = self.quoteFutureL(data)
            if tick:
                tickUpdatedEvent = TickUpdatedEvent(tick)
                self.kBarGenerator.onTickUpdated(tickUpdatedEvent)
        except Exception as exception:
            print(exception)



    def quoteFutureL(self, data):
        tick = Tick(
            datetime.now(),
            data['Close'][0],
            data['Volume'][0]
        )   
        return tick    

if __name__ == '__main__':
    
    
    app = QApplication(sys.argv)
    widget = KBarGeneratorTest()
    widget.show()
    app.exec_()




