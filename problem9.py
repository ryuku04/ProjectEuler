# usr/bin/python
# -*- coding:utf-8 -*-
#*******************************************************************************
#* Problem 9  : Special Pythagorean triplet
#* A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#* a^2 + b^2 = c^2
#* For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#* There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#* Find the product a*b*c.
#*******************************************************************************
import math

def check_Pythagorean_triplet(a,b,c):
    if a*a + b*b == c*c:
        return True
    return False

if __name__ == '__main__':
    num = 1000
    ans = 0
    for i in range(1,int(num/3)):
        for j in range(1,num-i):
            if check_Pythagorean_triplet(i,j,num-i-j) == True:
                ans = i*j*(num-i-j)
                print(i,j,num-i-j)
    print(ans)
