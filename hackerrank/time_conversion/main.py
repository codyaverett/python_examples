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
    # is afternoon?
    if s[8:] == "PM":
        # is noon?
        if s[:2] == "12":
            return s[:8]
        else:
            # Add the first 12 hours to the time
            return str(int(s[:2]) + 12) + s[2:8]
    # is an AM time
    else:
        # 12 am is 00
        if s[:2] == "12":
            # 00:00:00 and exclude the AM/PM
            return "00" + s[2:8]
        else:
            # only exclude the AM/PM
            return s[:8]    
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()