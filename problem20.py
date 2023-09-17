# usr/bin/python
# -*- coding:utf-8 -*-
#*******************************************************************************
#* Problem 20 : Factorial Digit Sum
#* 
#* n! means n * (n-1) * ... * 2 * 1.
#* 
#* For example, 10! = 3628800,
#* and the sum of the digits in the number 10! is 3+6+2+8+8+0+0 = 27.
#* Find the sum of the digits in the number 100!.
#*******************************************************************************
import math

def digit_sum_fact(num_fact):

    ans = 0
    fact = list(str(math.factorial(num_fact)))
    
    for fa in fact:
        ans = ans + int(fa)

    return ans

if __name__ == '__main__':
    num_fact = 100
    print(digit_sum_fact(num_fact))


