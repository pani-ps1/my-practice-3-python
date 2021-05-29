# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 04:35:41 2020

@author: utob
"""

import xlwt
from xlwt import Workbook

wb = Workbook()
sh1 = wb.add_sheet('sheet 1')
sh1.write(0,0,125)
sh1.write(2,4,)