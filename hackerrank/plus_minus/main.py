#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    denominator = len(arr)
    
    for number in arr:
        if number > 0:
            pos += 1
        elif number < 0:
            neg += 1
        else:
            zero += 1
        
    print(pos / denominator)
    print(neg / denominator)
    print(zero / denominator)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
