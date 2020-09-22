# usr/bin/python
# -*- coding:utf-8 -*-
#*******************************************************************************
#* Problem 16 : Power digit sum
#* 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#* What is the sum of the digits of the number 2^1000?
#*******************************************************************************

if __name__ == '__main__':
    num = 1000

    str_power2 = str(2**num)
    str_power2_list = list(str_power2)

    print(str_power2)
    print(sum(int(i) for i in str_power2_list))
    


