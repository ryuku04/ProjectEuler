# usr/bin/python
# -*- coding:utf-8 -*-
#*******************************************************************************
#* Problem 6  : Sum square difference
#* The sum of the squares of the first ten natural numbers is,
#* 1^2 + 2^2 + ... + 10^2 =385
#* The square of the sum of the first ten natural numbers is,
#* (1+ 2 + ... + 10)^2 = 55^2 = 3025
#* Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
#* 3025 - 385 = 2640
#* Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#*******************************************************************************
import math

def square_of_sum(n):
    ans = 0
    for i in range(1,n+1):
        ans = ans + i*i
#    print(ans)
    return(ans)

def sum_of_square(n):
    ans = 0
    for i in range(1,n+1):
        ans = ans + i
    ans = ans*ans
#    print(ans)
    return(ans)

if __name__ == '__main__':
    num = 100
    square_sum = square_of_sum(num)
    sum_square = sum_of_square(num)
    diff = sum_square - square_sum
    print(diff)
