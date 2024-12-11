#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    letters = s[-2:]
    time    = s[2:-2]
    hour    = s[:2]

    isPm = letters == 'PM'
    is12 = int(hour) == 12
    
    if isPm and not is12:
        return str(int(hour) + 12) + time
    elif isPm and is12:
        return hour + time
    elif not isPm and is12:
        return '00' + time
    else:
        return hour + time
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
