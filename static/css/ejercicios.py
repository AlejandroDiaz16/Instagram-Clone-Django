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
    # Write your code here
    for num in grades:
        mult = False

        if num % 5 >= 3:
            mult = True
            if num + 2 >= 40:
                if (num + 2) % 5 == 0:
                    print(num + 2)
                elif (num + 1) % 5 == 0:
                    print(num + 1)
            else:
                print(num)
        else:
            print(num)


if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

