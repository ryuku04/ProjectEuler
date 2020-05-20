# usr/bin/python
# -*- coding:utf-8 -*-
#*******************************************************************************
#* Problem 4  : Largest palindrome product
#* A palindromic number reads the same both ways.
#* The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#* Find the largest palindrome made from the product of two 3-digit numbers.
#* lastupdate : 2020/05/20
#*******************************************************************************
import math

def check_palindrome(num,nd):
    flg = False
    list_digit = [""]*nd

    for i in range(0,nd):
        list_digit[i] = num%10
        num = math.floor(num/10)

    for i in range(0,nd):
        if list_digit[i] != list_digit[(nd-i-1)]:
            return False

    flg = True
    return flg

if __name__ == '__main__':
    nmax = 1000
    nd = 6
    lpp = 1
    for i in range(10, nmax):
        for j in range(10, nmax):
            if check_palindrome(i*j, nd) == True and i*j > lpp:
                 lpp = i*j
    print(lpp)
