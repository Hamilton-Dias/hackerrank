#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def returnCode(step):
    if step == 'U':
        return 1
    return -1

def countingValleys(steps, path):
    level=valley=0
    
    for element in path:
        code = returnCode(element)        
        if level < 0 and level + code == 0:
            valley = valley + 1
        level = level + code
        
    return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
