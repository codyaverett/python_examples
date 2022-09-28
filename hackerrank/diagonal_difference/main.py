#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    
    l2r_diagonal = 0
    r2l_diagonal = 0
    
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            if x == y: # left to right diagonal
                l2r_diagonal += arr[y][x]
            if x + y == len(arr) - 1: # right to left diagonal
                r2l_diagonal += arr[y][x]
                
    return abs(l2r_diagonal - r2l_diagonal)
       
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
