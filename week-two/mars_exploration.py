#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    count = 0

    for i, char in enumerate(s):
        stop = i + 1
        if stop % 3 == 0:
            start  = stop - 3
            string = s[start:stop]
            
            if string[:1] != 'S':
                count += 1
            if string[1:2] != 'O':
                count += 1
            if string[2:3] != 'S':
                count += 1
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
