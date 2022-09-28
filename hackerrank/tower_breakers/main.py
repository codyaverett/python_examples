
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#
#   Two players are playing a game of Tower Breakers! Player 1 always moves first, and both players always play optimally.
#   The rules of the game are as follows:
#   1. Initially there are n towers.
#   2. Each tower is of height m.
#   3. The players move in alternating turns.
#   4. In a single move, a player can choose a tower of height x and reduce its height to y, where 1 <= y <= x and y evenly divides x.
#   5. If the current player is unable to make a move, they lose the game.
#   Given the values of n and m, determine which player will win. If the first player wins, return 1. Otherwise, return 2.

def towerBreakers(n, m): 
    # if m is 1, then the second player will always win
    if m == 1: 
        return 2
    
    # if n is even, then player 2 will win
    if n % 2 == 0: 
        return 2
    
    # n is odd
    return 1;

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
