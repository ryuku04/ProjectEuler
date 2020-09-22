# usr/bin/python
# -*- coding:utf-8 -*-
#*******************************************************************************
#* Problem 15  : Lattice paths
#* Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#* How many such routes are there through a 20×20 grid?
#*******************************************************************************
import math

def factorial(n):
    if n == 1:
       return 1
    elif n > 1:
       return n*factorial(n-1)

def combination(n,r):
    ans = int(factorial(n)/(factorial(r)*factorial(n-r)))
    return ans

if __name__ == '__main__':
    num = 20
    
    print(combination(2*num,num))
    
