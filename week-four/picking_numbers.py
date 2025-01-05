#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    arrays = []
    a.sort()

    for i in range(len(a)):
        arrays.append([])
        arrays[i].append(a[i])
        iterate = a[i+1:]

        for j in range(len(iterate)):
            if abs(a[i] - iterate[j]) <= 1:
                arrays[i].append(iterate[j])
            else:
                break

    return len(max(arrays, key=len))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
