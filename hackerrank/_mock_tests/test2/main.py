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
# Given the initial configurations for q matrices, help reverse the
# rows and columns of each matrix in the best possible way SO that the
# sum of the elements in the matrix's upper-left quadrant is maximal.    
    # 1. Find the max sum of the upper-left quadrant
    # 2. Find the max sum of the upper-right quadrant
    # 3. Find the max sum of the lower-left quadrant
    # 4. Find the max sum of the lower-right quadrant 
    
    ## not sure

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
