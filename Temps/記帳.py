# -*- encoding: utf-8 -*-

'''
* @File    :   記帳.py
* @Time    :   2021/03/13 04:06:46
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())



def isBalance(debitAmount, creditAmount):
    """ 借貸是否平衡 
    Arguments:
        debitAmount (float): 借方金額
        creditAmount (float): 貸方金額
    """
    if debitAmount == creditAmount:
        return True
    return False




