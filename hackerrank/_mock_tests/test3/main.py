#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def is_a_palindrome(s: str) -> bool:
    return s == s[::-1]


def remove_charater_at_index(s: str, index: int) -> str:
    return s[:index] + s[index + 1:]


def palindromeIndex(s: str) -> int:
    # is string is a palindrome?
    if is_a_palindrome(s):
        return -1
    else:
        # find index of character that does not fit the palindrome
        for i in range(len(s)):
            left_char = s[i]
            right_char = s[len(s) - i - 1]
            if left_char != right_char:
                # remove character from string
                s = remove_charater_at_index(s, i)
                # check if string is a palindrome
                if is_a_palindrome(s):
                    return i
                else:
                    return len(s) - i


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()
        result = palindromeIndex(s)
        print(result)

    #     fptr.write(str(result) + '\n')

    # fptr.close()
