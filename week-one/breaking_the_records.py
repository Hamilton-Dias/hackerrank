#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    minRecord = 10**8
    maxRecord = 0
    breaks = [0, 0]
    
    for idx, score in enumerate(scores):
        isFirstRun = idx == 0
        
        if score < minRecord:
            minRecord = score
            if not isFirstRun:
                breaks[1] += 1
                
        if score > maxRecord:
            maxRecord = score
            if not isFirstRun:
                breaks[0] += 1
    
    return breaks
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
