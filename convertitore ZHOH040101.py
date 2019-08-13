#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 15:53:35 2019

@author: davideluciano
"""


import os

os.chdir('/Users/davideluciano/Desktop/progetto')

with open("3id8.txt", 'r') as f2:
    data = f2.read()
    
    
data1=list(data[10:463])

lsc=[["A", 2.18],["L", 4.17],["R", 2.71],["K", 2.12],["N", 1.85],["M", 3.63],["D", 1.75],["F", 5.88],["C", 3.89],["P", 2.09],["Q", 2.16],["S", 1.66],["E",1.89],["T", 2.18],["G", 1.17],["W", 6.46],["H", 2.51],["Y", 5.01], ["I", 4.50], ["V", 3.77]]



ls=[]
for i in data1:
    k=0
    while k<20:
        if i==lsc[k][0]:
            n=lsc[k][1]
        k=k+1
    ls=ls+[n]
            

k=0 

o=[]           
while k<59:
    o=o+[0]
    k=k+1
    
    
    
import numpy as np    
import matplotlib.pyplot as plt

sp = np.fft.fft(i)
freq = np.fft.fftfreq(i.shape[-1])
plt.plot( freq, np.absolute(sp))

plt.xlim([0.1,0.5])
plt.ylim([-0.1,200])

plt.show()