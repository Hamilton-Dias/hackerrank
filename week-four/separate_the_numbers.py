#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    result = "NO"
    
    if len(s) > 1:
        for i in range(1, len(s)//2 + 1):
            s2   = s[:i]
            prev = int(s2)
            
            while len(s2) < len(s):
                nextN = prev + 1
                s2 += str(nextN)
                prev = nextN
                
                if s2 == s:
                    result = "YES " + s[:i]
        
    print(result)

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
