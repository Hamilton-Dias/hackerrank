#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    ids   = {}
    maxId = {
        'curId': -1,
        'value': -1
    }
    
    for a in arr:
        ids[a] = ids.get(a, 0) + 1

    for i, value in ids.items():
        maxValue = maxId.get('value')
        
        if (value > maxValue) or (value == maxValue and i < maxId['curId']):
            maxId['curId'] = i
            maxId['value'] = value
    
    return maxId['curId']

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
