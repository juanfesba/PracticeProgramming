#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

# Complete the pairs function below.
def pairs(k, arr):
    goal=defaultdict(int)
    ans=0
    for e in arr:
        if(goal[e]!=None):
            ans+=goal[e]
        goal[e+k]+=1
        goal[e-k]+=1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
