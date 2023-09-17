# usr/bin/python
# -*- coding:utf-8 -*-
#*******************************************************************************
#* Problem 18 : Maximum Path Sum I
#* By starting at the top of the triangle below and moving to adjacent numbers 
# on the row below, the maximum total from top to bottom is 23.
# 
# 3
# 7 4
# 2 4 6
# 8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23.
# 
# Find the maximum total from top to bottom of the triangle below:
# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
# NOTE: As there are only 16384 routes, 
# it is possible to solve this problem by trying every route. 
# However, Problem 67, is the same challenge with a triangle containing one-hundred rows; 
# it cannot be solved by brute force, and requires a clever method! ;o)
#*******************************************************************************
import math

def find_maxinu_path(matrix):
    ans = 0
    ans_tmp=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    for i1 in range(0,1):
      ans_tmp[0] = int(matrix[0][i1])
      for i2 in range(i1,i1+2):
        ans_tmp[1] = int(matrix[1][i2])
        for i3 in range(i2,i2+2):
          ans_tmp[2] = int(matrix[2][i3])
          for i4 in range(i3,i3+2):
            ans_tmp[3] = int(matrix[3][i4])
            for i5 in range(i4,i4+2):
              ans_tmp[4] = int(matrix[4][i5])
              for i6 in range(i5,i5+2):
                ans_tmp[5] = int(matrix[5][i6])
                for i7 in range(i6,i6+2):
                  ans_tmp[6] = int(matrix[6][i7])
                  for i8 in range(i7,i7+2):
                    ans_tmp[7] = int(matrix[7][i8])
                    for i9 in range(i8,i8+2):
                      ans_tmp[8] = int(matrix[8][i9])
                      for i10 in range(i9,i9+2):
                        ans_tmp[9] = int(matrix[9][i10])
                        for i11 in range(i10,i10+2):
                          ans_tmp[10] = int(matrix[10][i11])
                          for i12 in range(i11,i11+2):
                            ans_tmp[11] = int(matrix[11][i12])
                            for i13 in range(i12,i12+2):
                              ans_tmp[12] = int(matrix[12][i13])
                              for i14 in range(i13,i13+2):
                                ans_tmp[13] = int(matrix[13][i14])
                                for i15 in range(i14,i14+2):
                                  ans_tmp[14] = int(matrix[14][i15])
                                  if ans < sum(ans_tmp):
                                      print(ans_tmp, sum(ans_tmp))
                                      ans = sum(ans_tmp)

    return ans


if __name__ == '__main__':
    matrix = []

    matrix.append([75])
    matrix.append([95, 64])
    matrix.append([17, 47, 82])
    matrix.append([18, 35, 87, 10])
    matrix.append([20, 4, 82, 47, 65])
    matrix.append([19, 1, 23, 75, 3, 34])
    matrix.append([88, 2, 77, 73, 7, 63, 67])
    matrix.append([99, 65, 4, 28, 6, 16, 70, 92])
    matrix.append([41, 41, 26, 56, 83, 40, 80, 70, 33])
    matrix.append([41, 48, 72, 33, 47, 32, 37, 16, 94, 29])
    matrix.append([53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14])
    matrix.append([70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57])
    matrix.append([91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48])
    matrix.append([63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31])
    matrix.append([4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23])

#    print(matrix)

    print(find_maxinu_path(matrix))
    


