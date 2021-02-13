





def getProfitLossRatio(avgWin, avgLoss):
    """ 盈虧比 """

    return round(avgWin / avgLoss, 2)


def getExpectedValue(winR, avgProfitLoss):
    """ 期望值 """
    return round(winR * avgProfitLoss, 2)

def getF(b, p):
    """ 
    b: 盈虧比
    p: 勝率
    q: 敗率
    """
    q = (1 - p)
    f = round((b * p - q) / b  , 2)
    return f



def cardSet(cardSet, games, amountPerGame, win1R, loss1R, loss2R, loss3R):
    print(f"HandCard: {cardSet}")

    winTime = round(win1R * games, 2) # 獲利次數
    lossTime = round(loss1R * games + loss2R * games + loss3R * games, 2) # 虧損次數
    
    winAmount = round(winTime * amountPerGame, 2)
    lossAmount = round(loss1R * games * amountPerGame + loss2R * games * amountPerGame * 2 + loss3R * games * amountPerGame * 3, 2)

    avgWin = winAmount / winTime
    avgLoss = lossAmount / lossTime
    avgProfitLoss = getProfitLossRatio(avgWin, avgLoss)
    expectedValue = getExpectedValue(win1R, avgProfitLoss)
    f = getF(avgProfitLoss, win1R)
    fAmount = round(5000 * f)
    print(f"\n手牌: {cardSet}")
    # print(f"獲利金額: {winAmount}, 虧損金額: {lossAmount}")
    # print(f"平均獲利: {avgWin}, 平均虧損: {avgLoss}, 盈虧比: {avgProfitLoss}")
    # print(f"期望值: {expectedValue}")     
    print(f"\tF比例: {f * 100} % \n\t金額: {fAmount}")

cardSet("AA, KK", 100, 100, 12/13, 0/13, 0/13, 1/13)
cardSet("22, QQ", 100, 100, 11/13, 1/13, 0/13, 1/13)
cardSet("33, JJ", 100, 100, 10/13, 2/13, 0/13, 1/13)
cardSet("44, 10s", 100, 100, 9/13, 3/13, 0/13, 1/13)
cardSet("55, 9s", 100, 100, 8/13, 4/13, 0/13, 1/13)

cardSet("AK", 100, 100, 11/13, 0/13, 2/13, 0/13)
cardSet("2K AQ", 100, 100, 10/13, 1/13, 2/13, 0/13)
cardSet("3K 2Q AJ", 100, 100, 9/13, 2/13, 2/13, 0/13)
cardSet("4K 3Q 2J A10", 100, 100, 8/13, 3/13, 2/13, 0/13)
cardSet("5K 4Q 3J 210 A9", 100, 100, 7/13, 4/13, 2/13, 0/13)