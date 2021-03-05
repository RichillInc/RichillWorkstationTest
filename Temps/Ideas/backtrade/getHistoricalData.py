# -*- encoding: utf-8 -*-

'''
* @File    :   getHistoricalData.py
* @Time    :   2021/02/10 21:44:47
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
import yfinance
from Temps.Ideas.backtrade.KBarFactory import KBarFactory
import pandas

def getHis(symbol):
    his = yfinance.Ticker(symbol).history(period="1y")
    his.index = pandas.to_datetime(his.index, format="%Y%m%d", errors="ignore")
    hisBars = []
    for date, barDAta in his.iterrows():
        
        kBar = KBarFactory.createKBar(
            symbol, 
            "TSE", 
            date, 
            "", 
            barDAta['Open'], 
            barDAta['High'], 
            barDAta['Low'], 
            barDAta['Close'], 
            barDAta['Volume']
        )

        hisBars.append(kBar)

    
    return hisBars
    
