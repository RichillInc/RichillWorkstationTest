# -*- encoding: utf-8 -*-

'''
* @File    :   FundDataCrawler.py
* @Time    :   2021/01/31 02:16:00
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())

import pandas
import urllib.request



class Fund(object):
    """ 基金 """

    def __init__(self,
        fundId="",
        fundName="",
        isinCode="",
        generalAgent="",
        fundCompany="",
        establishDate="",
        fundType="",
        registeredPlace="",
        size=0

    ):
        
        self.__fundId = fundId # 基金代號
        self.__fundName = fundName # 基金名稱
        self.__isinCode = isinCode # ISIN Code
        self.__generalAgent = generalAgent # 總代理
        self.__fundCompany = fundCompany # 基金公司
        self.__establishDate = establishDate # 成立日期
        self.__fundType = fundType # 基金類型
        self.__registeredPlace = registeredPlace # 註冊地
        self.__size = size # 基金規模
        self.__depository = None # 保管機構 depository
        self.__custodyFeeRate = 0 # 保管費率 custody fee rate
        self.__managementFeeRate = 0 # 管理費率 management fee rate
        self.__isDividend = False # 收益分配 dividend
        self.__subscritionFee = 0 # 申購手續費 subscription fee

    def __str__(self):
        return f"Fund({self.__fundId}, {self.__fundName}, {self.__isinCode})"

class FundDataCrawler(object):
    """ 基金資料搜尋器 """


    FUND_RICH_COLUMNS = [
        "基金代號",
        "基金名稱",
        "ISIN Code",
        "淨值日/淨值",
        "漲跌幅(%)/漲跌",
        "幣別",
        "基金規模(百萬)",
        "操作"
    ]

    def __init__(self):
        self.__currentPage = 1
        self.__isEndPage = False
        self.__funds = []

    def getPageFunds(self):
        # 根據頁數判定要打開的網頁
        print(f"目前頁數: {self.__currentPage}")
        if self.__currentPage == 1:
            url = "https://www.fundrich.com.tw/theme-fund/"
        else:
            url = f"https://www.fundrich.com.tw/theme-fund/?page={self.__currentPage}"      

        # 打開網頁Html
        html = urllib.request.urlopen(url).read()
        html = html.decode("utf-8")

        # 將Html轉換成DataFrame
        dataFrame = pandas.read_html(html)[1]
        dataFrame.columns = self.FUND_RICH_COLUMNS
        dataFrame = dataFrame.drop(self.FUND_RICH_COLUMNS[3:], axis=1)

        # 創建Fund對象
        for i in range(0, len(dataFrame)):
            fundId = dataFrame[self.FUND_RICH_COLUMNS[0]][i]
            fundName = dataFrame[self.FUND_RICH_COLUMNS[1]][i]
            isinCode = dataFrame[self.FUND_RICH_COLUMNS[2]][i]
            fund = Fund(fundId, fundName, isinCode)
            self.addFund(fund)
        self.__currentPage += 1

    def addFund(self, fund):
        """ 新增基金 """
        self.__funds.append(fund)            

    def getFunds(self):
        return self.__funds



    def start(self):
        while not self.__isEndPage:
            try:
                self.getPageFunds()
            except Exception as exception:
                self.__currentPage -= 1
                self.__isEndPage = True
                print(f"已搜尋所有資料, 總頁數: {self.__currentPage}, 基金總數: {len(self.getFunds())}")                
            

            
    def getFundDetail(self, fundId):
        """ 獲取基金詳細資料 """
        url = f"https://www.fundrich.com.tw/fund/{fundId}.html?id={fundId}"

        # 打開網頁   
        html = urllib.request.urlopen(url).read()
        html = html.decode("utf-8")
        # 獲取資料表
        dataFrames = pandas.read_html(html)

        # 最新報價
        # latestQuote = dataFrames[0]

        # 近30日淨值
        # print(dataFrames[1])
        # print(dataFrames[2])
        # print(dataFrames[3])

        # 績效表現
        # print(dataFrames[4])
        # print(dataFrames[5])

        # 基本資料
        # print(dataFrames[6])

        # 代銷&費用說明
        # print(dataFrames[7])

        # 資產配置-行業比重
        # print(dataFrames[8])

        # 風險評等
        # print(dataFrames[9])

        # 資產配置-風險評估
        # print(dataFrames[10])

        # 資產配置-前十大持股
        # print(dataFrames[11])

        # 配息紀錄
        # print(dataFrames[12])


    def login(self, userId, password):
        """ 登入基富通 """


        url = "https://www.fundrich.com.tw/login.html?redirect=%2FECWeb2%2F%23%2FquotaCompo"



c = FundDataCrawler()
c.getFundDetail("019002")
