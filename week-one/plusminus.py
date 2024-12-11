#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    minus = 0
    plus  = 0
    zeros = 0
    total = len(arr)
    
    for number in arr:
        if number < 0:
            minus += 1
        elif number > 0:
            plus += 1
        else:
            zeros += 1
    
    print(round(plus/total, 6))
    print(round(minus/total, 6))
    print(round(zeros/total, 6))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
