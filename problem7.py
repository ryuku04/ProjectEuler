# usr/bin/python
# -*- coding:utf-8 -*-
#*******************************************************************************
#* Problem 7  : 10001st prime
#* By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#* What is the 10001st prime number?
#*******************************************************************************
import math

def isPrime(n):
    if n <= 1:
        return False

    for i in range(2,n):
        if n%i == 0 :
            return False
    return True

if __name__ == '__main__':
    num = 10001
    count = 0
    i = 1
    while count < num:
        i = i + 1
        if isPrime(i) == True:
            count = count + 1
            ans = i
#        print(count,ans)
    print(count,ans)
