#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    matches   = 0
    lastFound = -1
    ar.sort()

    for i, a in enumerate(ar):
        if i + 1 < n:
            nextItem = ar[i + 1]
                
            if a == nextItem and lastFound != i:
                matches += 1
                lastFound = i + 1

    return matches

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
