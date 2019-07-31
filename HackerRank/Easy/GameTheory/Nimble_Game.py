#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the nimbleGame function below.
def nimbleGame(s):
    ans=0
    for i,e in enumerate(s):
        if(i==0):
            continue
        if(e%2==0):
            continue
        ans^=i
    if(ans==0):
        return "Second"
    else:
        return "First"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        s = list(map(int, input().rstrip().split()))

        result = nimbleGame(s)

        fptr.write(result + '\n')

    fptr.close()
