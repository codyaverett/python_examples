#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesarCipher(string: str, rotation: int):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_lower = alphabet.lower()
    alphabet_upper = alphabet.upper()
    new_string = ""

    for char in string:
        if char.isalpha():
            if char.isupper():
                alphabet = alphabet_upper
            else:
                alphabet = alphabet_lower

            index = alphabet.index(char)
            new_index = (index + rotation) % 26
            new_string += alphabet[new_index]
        else:
            new_string += char
    return new_string


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
