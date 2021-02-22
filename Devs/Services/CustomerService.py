# -*- encoding: utf-8 -*-

'''
* @File    :   CustomerService.py
* @Time    :   2021/02/22 07:36:33
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''


import os
import sys
sys.path.append(os.getcwd())

from Devs.Services.Service import Service

class CustomerService(Service):
    """ 客戶服務 """

    def __init__(self):
        super(CustomerService, self).__init__()



