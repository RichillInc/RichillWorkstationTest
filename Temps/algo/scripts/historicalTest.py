# -*- encoding: utf-8 -*-

'''
* @File    :   historicalTest.py
* @Time    :   2021/02/09 22:52:12
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
import yfinance
from DevSource.Backtest.KBar import KBar
def getHistoricalMarketData(symbol):
    return yfinance.Ticker(symbol).history(period="1y")



def getHistoricalKBarData(symbol):
    kBars = []
    historical = getHistoricalMarketData(symbol)
    
    for datetime, kBarData in historical.iterrows():
        
        open = kBarData['Open']
        high = kBarData['High']
        low = kBarData['Low']
        close = kBarData['Close']
        volume = kBarData['Volume']
        kBar = KBar(symbol, open, high, low, close, volume)
        kBars.append(kBar)
    return kBars

