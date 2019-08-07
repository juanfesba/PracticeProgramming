#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the isValid function below.
def isValid(s):
    frecuency=collections.defaultdict(int)
    peak=1
    old=len(frecuency)
    peakT=0
    special=0
    for e in s:
        frecuency[e]+=1
        if frecuency[e]==1:special+=1
        if frecuency[e]==2:special-=1
        if frecuency[e]==peak:
            peakT+=1
            old-=1
        elif frecuency[e]==peak-1:old+=1
        elif frecuency[e]>peak:
            peak+=1
            old=peakT-1
            peakT=1
    print(str(peak))
    if(old==len(frecuency) or peakT==len(frecuency) or (old+1==len(frecuency) and peakT==1) or ((old+1==len(frecuency) or peakT+1==len(frecuency)) and special==1 and len(frecuency)>2) and peak>1):return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
