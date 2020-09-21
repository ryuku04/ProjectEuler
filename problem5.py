# usr/bin/python
# -*- coding:utf-8 -*-
#*******************************************************************************
#* Problem 5  : Smallest multiple
#* 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#* What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
#* lastupdate : 2020/05/20
#*******************************************************************************
import math

if __name__ == '__main__':
    nmax = 20
    spm = 1
    for i in range(1, nmax):
        spm = spm*i
#    print(spm)

    mmax = spm
    isSPM = False

    for i in range(nmax, mmax+1):
        for j in range(2, nmax+1):
            if i%j != 0:
                break
            if j == nmax:
                isSPM = True
        if isSPM == True:
            print(i)
            break
