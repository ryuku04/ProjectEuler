# usr/bin/python
# -*- coding:utf-8 -*-
#*******************************************************************************
#* Problem 1  : If we list all the natural numbers below 10 
#*              that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
#*              The sum of these multiples is 23.
#*              Find the sum of all the multiples of 3 or 5 below 1000.
#* lastupdate : 2020/05/15
#*******************************************************************************

def get_sum_3or5mod(n):
    sum = 0
    for i in range(1, n):
        if i%3 == 0 or i%5 == 0:
            sum = sum + i
    return sum

if __name__ == '__main__':
    print(get_sum_3or5mod(1000))
