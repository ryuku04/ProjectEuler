# usr/bin/python
# -*- coding:utf-8 -*-
#*******************************************************************************
#* Problem 21 : Famicable Numbers
#* 
#* be d(n) defined as the sum of proper divisors of n
#* (numbers less than n which divide evenly into n).
#* If d(a)=b and d(b)=a, a!=b then a and b are an amicable pair and 
#* each of a and b are called amicable numbers.
#*
#* For example,
#* the proper divisors of 220 are 1,2,4,5,10,11,20,22,44,55 and 110;
#* therefore d(220) = 284.
#* The proper divisors of 284 are 1,2,4,71 and 142.;
#* so d(284) = 220.
#* Evaluate the sum of all the amicable numbers under 10000.
#*******************************************************************************
import math

def get_proper_divisors(num):
    list = [] 
    if num == 1:
        list.append(1)

    for i in range(1,num):
        if num%i == 0:
            list.append(i)

    return list

def sum_famicable_numbers(num_famicable):
    ans = 0
    list = [] 
    list.append(0)

    for i in range(1,num_famicable):
#        print(sum(get_proper_divisors(i)))
        list.append(sum(get_proper_divisors(i)))

#    print(list)
#    print(220,list[220],list[list[220]])
#    print(284,list[284],list[list[284]])

    for i in range(1,num_famicable):

        if list[i] < num_famicable and i == list[list[i]]and i != list[i]:
            ans = ans + i
            print(i,list[i])

    return ans

if __name__ == '__main__':
    num_famicable = 10000

    print(sum_famicable_numbers(num_famicable))

