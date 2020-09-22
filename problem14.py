# usr/bin/python
# -*- coding:utf-8 -*-
#*******************************************************************************
#* Problem 14  : Longest Collatz sequence
#* The following iterative sequence is defined for the set of positive integers:
#* n → n/2 (n is even)
#* n → 3n + 1 (n is odd)
#* Using the rule above and starting with 13, we generate the following sequence:
#* 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#* It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), 
#* it is thought that all starting numbers finish at 1.
#* Which starting number, under one million, produces the longest chain?
#* NOTE: Once the chain starts the terms are allowed to go above one million.
#*******************************************************************************

import math

def sequence(n):
    if n % 2 == 0:
        return n/2
    elif n % 2 == 1:
        return 3*n + 1
    else:
        return False

if __name__ == '__main__':

    num = 1000000
    ans = 0
    max_count = 1

    for i in range(1,num+1):
        j=i
        count = 1
        while j > 1:
            j = sequence(j)
            count = count + 1
        if count > max_count:
            max_count = count
            ans = i
#        print(i,count)

    print(ans)
