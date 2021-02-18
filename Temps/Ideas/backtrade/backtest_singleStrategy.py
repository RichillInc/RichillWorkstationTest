

# -*- encoding: utf-8 -*-

'''
* @File    :   main.py
* @Time    :   2021/02/10 21:55:28
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())
import pandas
import numpy
from Temps.backtrade.getHistoricalData import getHis
from Temps.backtrade.DataSeries import DataSeries
import datetime 
import time

def crossOver(series1, series2):
    """ """
    return series1[-1] > series2[-1] and series1[-2] < series2[-2]

def crossUnder(series1, series2):
    """ """
    return series1[-1] < series2[-1] and series1[-2] > series2[-2]

def getSma(series, period):

    sma = pandas.Series(series).rolling(period).mean().values
    return sma

# S1
def onDataSeriesUpdatedS1(symbol, dataSeries):
    """ """
    smaLength = 20
    date = dataSeries.getDate()
    close = dataSeries.getClose()
    sma = getSma(close, smaLength)

    if crossOver(close, sma):
        datetime = date[-1]
        print(f"Strategy1 - {datetime} - 突破均線 SMA {sma[-1]}, 買進 {symbol} @ {close[-1]}")
        
    if crossUnder(close, sma):
        datetime = date[-1]
        print(f"Strategy1 - {datetime} - 跌破均線 SMA {sma[-1]}, 賣出 {symbol} @ {close[-1]}")    

# S2

def onDataSeriesUpdatedS2(symbol, dataSeries):
    """ """
    smaLength = 55
    date = dataSeries.getDate()
    close = dataSeries.getClose()
    sma = getSma(close, smaLength)

    if crossOver(close, sma):
        datetime = date[-1]
        print(f"Strategy2 - {datetime} - 突破均線 SMA {sma[-1]}, 買進 {symbol} @ {close[-1]}")
        
    if crossUnder(close, sma):
        datetime = date[-1]
        print(f"Strategy2 - {datetime} - 跌破均線 SMA {sma[-1]}, 賣出 {symbol} @ {close[-1]}")    






symbol = "AAPL"
historicalBars = getHis(symbol)
print(f"歷史數據下載完成.., symbol={symbol}, DataLength: {len(historicalBars)}")


dataSeries = DataSeries()
for bar in historicalBars:
    dataSeries.addKBar(bar)
    onDataSeriesUpdatedS1(symbol, dataSeries)
    onDataSeriesUpdatedS2(symbol, dataSeries) # strategy.onDataSeriesUpdated(dataSeriesUpdatedEvent)
