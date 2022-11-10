# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 21:57:47 2022

@author: Jon


Use numpy.array to define a 3-by-7 array, A.  In array location (i,j), row i, column j,  put the number i*j

Use slicing to produce and print:

1)  row 2 of A

2) row 2 of A in reverse order

3) the sub-matrix consisting or the bottom right 2x2 sub-array 

4) the sub-array consisting of the bottom left 2x2 sub-array

5) the 3x3 sub-array in the middle of A


"""

import numpy as np

A = np.zeros(shape = (3,7))

for i in range(3):
    for j in range(7):
        A[i,j] = i*j

print(A,"\n")
## 1)  row 2 of A
print('row 2 of A')
print(A[2,:])

## 2) row 2 of A in reverse order
print('\n row 2 of A in reverse order')
print(A[2,::-1])

## 3) the sub-matrix consisting or the bottom right 2x2 sub-array
print('\n the sub-matrix consisting or the bottom right 2x2 sub-array')
print(A[1:,5:])

## 4) the sub-array consisting of the bottom left 2x2 sub-array
print('\n the sub-array consisting of the bottom left 2x2 sub-array')
print(A[1:,:2])

## 5) the 3x3 sub-array in the middle of A
print('\n the 3x3 sub-array in the middle of A')
print(A[:,2:5])