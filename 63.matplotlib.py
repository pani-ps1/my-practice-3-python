# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 08:06:40 2020

@author: utob
"""

import numpy as np
import matplotlib.pyplot as plt

xticks = ['sat','sun','mon','tues']
x1 = [3,4,7,11]

yticks = ['math','physics','arabic','programming']
y1 = [12,21,4,3]

plt.plot(x1,y1,'ro')
plt.xticks(x1,xticks)
plt.yticks(y1,yticks)

plt.title('day')
plt.show()