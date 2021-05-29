# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 04:19:46 2020

@author: utob
"""

import xlrd

esme_file = '000.xlsx'

wb = xlrd.open_workbook(esme_file)
sh = wb.sheet_by_index(0)

for i in range(sh.ncols-1):
    for j in range(sh.nrows):
        print(sh.cell_value(j,i+1))
        