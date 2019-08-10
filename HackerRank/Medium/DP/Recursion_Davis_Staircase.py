#!/bin/python3

import math
import os
import random
import re
import sys

ans=[0]*37
ans[1]=1
ans[2]=2
ans[3]=4
i=4
while i<37:
    ans[i]=(ans[i-1]+ans[i-2]+ans[i-3])%10000000007
    i+=1

# Complete the stepPerms function below.
def stepPerms(n):
    return ans[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
