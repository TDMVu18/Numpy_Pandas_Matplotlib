# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 20:38:34 2020

@author: Administrator
"""

import numpy as np
A = np.array([[1,2,3], [2,3,4]])
B = np.array([[2,1,-1], [1,1,1]])
C = np.array([[0,-1], [1,1],[2,3]])
D = A+B
E = A.dot(C)
print("Ma trận A là:",A)
print("Ma trận B là:",B)
print("Ma trận C là:",C)
print("A + B =",D)
print("A x C =",E)
print("Chuyển vị của ma trận A là:",A.transpose())