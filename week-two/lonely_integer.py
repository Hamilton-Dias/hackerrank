#!/bin/python3

import math
import os
import random
import re
import sys
import copy

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    repeated = []
    
    for i, ia in enumerate(a):
        for j, ja in enumerate(a):
            if ia == ja and i != j:
                repeated.append(ia)

    diff = list(set(a) - set(repeated))
    return diff[0]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
