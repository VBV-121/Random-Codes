#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    s=len(arr)-1
    r=0
    sum1=0
    sum2=0
    for i in range(0,len(arr),4):
        #s=s+arr[i]
        for i in arr:
            sum1=sum1+i[s]
            s=s-1
            sum2=sum2+i[r]
            r=r+1
            print(sum1)
            print(s)
    return abs(sum1-sum2)

if __name__ == '__main__':
    n = 3
    arr = [[11,2,4],[4, 5, 6],[10, 8,-12]]
 
    result = diagonalDifference(arr)

    print(result)
