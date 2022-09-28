#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    
    lookup = {}
    
    # find max and min value in arr
    max_value = max(arr)
    min_value = min(arr)
    
    # populate lookup with keys from min to max value
    for i in range(min_value, max_value + 1):
        lookup[i] = 0
        
    # count the number of times each value appears in arr
    for number in arr:
        lookup[number] += 1
    
    print(max_value, min_value)
    print(lookup)

    # reduce lookup to a list of values
    lookupCounts = [item[1] for item in lookup.items()]
    return lookupCounts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
