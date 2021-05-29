# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 03:10:09 2020

@author: utob
"""
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0,10,0.01)
y = np.sin(2*np.pi*t)

plt.plot(t,y)
plt.xlabel('time(sec)')
plt.ylabel('output')
plt.title('sin')

plt.show()