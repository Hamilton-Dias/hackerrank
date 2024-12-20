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
    primary      = 0
    secondary    = 0
    matrixLength = len(arr[0]) - 1
    
    for i, iValue in enumerate(arr):
        for j, jValue in enumerate(arr):
            if i == j:
                primary += arr[i][j]
            
            if i + j == matrixLength:
                secondary +=  arr[i][j]

    return abs(primary - secondary)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
