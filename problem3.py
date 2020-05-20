# usr/bin/python
# -*- coding:utf-8 -*-
#*******************************************************************************
#* Problem 3  : Largest prime factor
#* The prime factors of 13195 are 5, 7, 13 and 29.
#* What is the largest prime factor of the number 600851475143 ?
#* lastupdate : 2020/05/20
#*******************************************************************************

def get_LPF(num):
    i = 1
    lpf = 1
    while i < num:
        i = i + 1
        if i != 1 and num%i == 0:
            lpf = num
            num = num/i
            i = 0
        if i == num:
            break
    return lpf

if __name__ == '__main__':
#    n = 13195
    n = 600851475143
    print(get_LPF(n))


