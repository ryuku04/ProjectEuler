# usr/bin/python
# -*- coding:utf-8 -*-
#*******************************************************************************
#* Problem 17 : Number letter counts
#* If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#* If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#* NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
#*******************************************************************************
import math

def number_character(n):
    num_chr = ''

    if n < 0 or 1000 < n :
        return False

    thousand = math.floor(n/1000)
    hundred = math.floor((n-1000*thousand)/100)
    ten = math.floor((n-1000*thousand-100*hundred)/10)
    one = n%10

    if thousand == 1:
        num_chr = num_chr + 'one thousand '

    if hundred == 1:
        num_chr = num_chr + 'one hundred '
    elif hundred==2:
        num_chr = num_chr + 'two hundred '
    if hundred == 3:
        num_chr = num_chr + 'three hundred '
    elif hundred==4:
        num_chr = num_chr + 'four hundred '
    if hundred == 5:
        num_chr = num_chr + 'five hundred '
    elif hundred==6:
        num_chr = num_chr + 'six hundred '
    if hundred == 7:
        num_chr = num_chr + 'seven hundred '
    elif hundred==8:
        num_chr = num_chr + 'eight hundred '
    if hundred == 9:
        num_chr = num_chr + 'nine hundred '
    
    if len(num_chr) > 0 :
        if ten != 0 or one != 0:
            num_chr = num_chr + 'and '
     
    if ten == 2:
        num_chr = num_chr + 'twenty '
    elif ten == 3:
        num_chr = num_chr + 'thirty '
    elif ten == 4:
        num_chr = num_chr + 'forty '
    elif ten == 5:
        num_chr = num_chr + 'fifty '
    elif ten == 6:
        num_chr = num_chr + 'sixty '
    elif ten == 7:
        num_chr = num_chr + 'seventy '
    elif ten == 8:
        num_chr = num_chr + 'eighty '
    elif ten == 9:
        num_chr = num_chr + 'ninety '
    
    if ten == 1:
        if one==0:
            num_chr = num_chr + 'ten'
        elif one==1:
            num_chr = num_chr + 'eleven'
        elif one==2:
            num_chr = num_chr + 'twelve'
        elif one==3:
            num_chr = num_chr + 'thirteen'
        elif one==4:
            num_chr = num_chr + 'fourteen'
        elif one==5:
            num_chr = num_chr + 'fifteen'
        elif one==6:
            num_chr = num_chr + 'sixteen'
        elif one==7:
            num_chr = num_chr + 'seventeen'
        elif one==8:
            num_chr = num_chr + 'eighteen'
        elif one==9:
            num_chr = num_chr + 'nineteen'

    if ten != 1:
        if one == 1:
            num_chr = num_chr + 'one'
        elif one == 2:
            num_chr = num_chr + 'two'
        elif one == 3:
            num_chr = num_chr + 'three'
        elif one == 4:
            num_chr = num_chr + 'four'
        elif one == 5:
            num_chr = num_chr + 'five'
        elif one == 6:
            num_chr = num_chr + 'six'
        elif one == 7:
            num_chr = num_chr + 'seven'
        elif one == 8:
            num_chr = num_chr + 'eight'
        elif one == 9:
            num_chr = num_chr + 'nine'

    return num_chr

if __name__ == '__main__':
    num = 1000
    ans = 0
    for i in range(1,num+1):
        print(number_character(i))
        ans = ans + len(number_character(i).replace(' ', ''))

    print(ans)
    


