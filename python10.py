# usr/bin/python
# -*- coding:utf-8 -*-
#*******************************************************************************
#* Problem 10  : Summation of primes
#* The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#* Find the sum of all the primes below two million.
#*******************************************************************************
import math

def isPrime(n):
    if n <= 1:
        return False
    if n == 2 :
        return True
    if n%2 == 0 :
        return False

    m = math.floor(math.sqrt(n)) + 1
    for i in range(3,m,2):
        if n%i == 0 :
            return False
    return True

if __name__ == '__main__':
    num = 2000000
    ans = 0
    for i in range(1,num):
        if isPrime(i) == True:
#            print(i)
            ans = ans + i
    print(ans)
