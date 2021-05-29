# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 11:58:13 2020

@author: utob
"""

import numpy as np
import matplotlib.pyplot as plt




def f(t):
    return np.sin(2*np.pi*t)*np.cos(np.pi*2*t)

t1 = np.arange(0,10,0.01)
t2 = np.arange(2,20,0.1)

plt.figure(1)
plt.subplot(2,1,1)
plt.plot(t1,f(t1),'bo',t2,f(t2),'r')
plt.xlabel('time(sec)')
plt.ylabel('output')
plt.show()
