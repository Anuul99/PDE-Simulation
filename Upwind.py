# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uVJaoNvwq7QgsDeIKzxILyMdyKXjMze7
"""

import numpy as np
import matplotlib.pyplot as plt
# initial values
u = 1.0 
dt = 0.1
dx = 1.0
# time span and x
x = np.arange(0, 100+dx, dx)
t = np.arange(0, 600+dt, dt)
# assigning f(0,x)
f = np.zeros(x.shape[0])
f[40:60] = 1
fx=np.copy(f)
# Plotting in case of 10,200,400 and 600
for iter in t:
    fx = fx+C*(np.roll(fx,int(np.sign(u)),0)-fx)
    if iter==10:
        plt.plot(x,fx, label= f't = {iter}')
        plt.legend()
    if iter==200: 
        plt.plot(x,fx, label= f't = {iter}')
        plt.legend()
    if iter==400: 
        plt.plot(x,fx, label= f't = {iter}')
        plt.legend()
    if iter==600: 
        plt.plot(x,fx, label= f't = {iter}')
        plt.legend()