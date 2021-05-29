# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 10:16:12 2020

@author: utob
"""

import numpy as np
import matplotlib.pyplot as plt




def f(t):
    return np.sin(2*np.pi*t)*np.cos(np.pi*2*t)

t1 = np.arange(0,10,0.01)
t2 = np.arange(2,20,0.1)

plt.plot(t1,f(t1))
plt.xlabel('time(sec)')
plt.ylabel('output')
plt.title('sin')

plt.show()

#t2


plt.plot(t2,f(t2))
plt.xlabel('time(sec)')
plt.ylabel('output')
plt.title('sin')

plt.show()


