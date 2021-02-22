# -*- encoding: utf-8 -*-

'''
* @File    :   CreateTableSqls.py
* @Time    :   2020/06/27 17:02:09
* @Author  :   Mengsyue Amao Tsai
* @Version :   1.0
* @Contact :   msat1027@gmail.com
* @License :   (C)Copyright, Mengsyue Amao Tsai
'''

import sys
import os
sys.path.append(os.getcwd())

from Tools.Database.Sqls.Item import Item
from Tools.Database.Sqls.Customer import Customer
from Tools.Database.Sqls.Supplier import Supplier

class CreateTableSqls(object):
    
    SQLS = {  
        "品項": Item,
        "客戶": Customer,
        "供應商": Supplier,
    }
    
      



