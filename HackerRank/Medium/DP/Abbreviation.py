#!/bin/python3

import math
import os
import random
import re
import sys

sys.setrecursionlimit(10000)

DP={}
a=""
b=""

# Complete the abbreviation function below.
def abbreviation(ia,ib):
    if ia==len(a) and ib==len(b):
        return True
    if ia==len(a):
        return False
    elif ib==len(b):
        while(ia<len(a)):
            if a[ia].isupper():
                return False
            ia+=1
        return True
    if DP.get((ia,ib))==None:
        if a[ia].isupper():
            if a[ia]!=b[ib]:
                DP[(ia,ib)]=False
            else:
                DP[(ia,ib)]=abbreviation(ia+1,ib+1)
        else:
            if a[ia].upper()!=b[ib]:
                DP[(ia,ib)]=abbreviation(ia+1,ib)
            else:
                DP[(ia,ib)]=DP[(ia,ib)]=abbreviation(ia+1,ib) or abbreviation(ia+1,ib+1)
    return DP[(ia,ib)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        DP={}
        a = input()

        b = input()

        result = abbreviation(0,0)
        if result==True:result="YES"
        else: result="NO"

        fptr.write(result + '\n')

    fptr.close()
