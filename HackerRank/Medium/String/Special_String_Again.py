#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    old="#"
    current=s[0]
    oldT=0
    currentT=1
    ans=1
    keyT=0
    for e in range(1,len(s)):
        if s[e]==current:
            currentT+=1
            ans+=currentT
            oldT=0
            old="#"
            if(keyT>0):
                keyT-=1
                ans+=1
        else:
            if(oldT>0 and s[e]==old):
                keyT=oldT-1
                ans+=1
            else:
                keyT=0
            old=current
            oldT=currentT
            current=s[e]
            currentT=1
            ans+=1
    return ans
            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
