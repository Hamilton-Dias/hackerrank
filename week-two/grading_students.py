#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    newGrades = []
    
    for idx, grade in enumerate(grades):
        
        newGrade  = grade
        nextRound = 5 * math.ceil(float(grade)/5)
        diff      = nextRound - newGrade

        if grade >= 38 and diff < 3:
            newGrade = nextRound

        newGrades.append(newGrade)

    return newGrades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
