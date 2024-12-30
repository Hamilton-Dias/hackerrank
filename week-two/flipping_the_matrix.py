#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    result = 0
    length = len(matrix)

    for i in range(length // 2):
        for j in range(length // 2):
            result += max(matrix[i][j],
                        max(matrix[i][length - 1 - j],
                           max(matrix[length - 1 - i][j], matrix[length - 1 - i][length - 1 - j])
                        )
                    )

    return result
                
    
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
