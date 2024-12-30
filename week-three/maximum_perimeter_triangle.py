#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#

def maximumPerimeterTriangle(sticks):
    length = len(sticks)
    triangles = []
    bigTriang = [0, 0, 0]
    
    sticks.sort()
    
    for i in range(length - 2):
        a = sticks[i]
        b = sticks[i + 1]
        c = sticks[i + 2]
        
        if a + b > c:
            triangles.append([a, b, c])
                
    if len(triangles) == 0:
        return [-1]

    for triangle in triangles:
        if (sum(triangle), triangle[2], triangle[0]) >= (sum(bigTriang), bigTriang[2], bigTriang[0]):
            bigTriang = triangle
            
    return bigTriang

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
