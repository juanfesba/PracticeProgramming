#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    for e in range(len(arr)):
        if e==0:
            ans=1
            peek=1
            last=1
            acc=0
        else:
            if(arr[e]>arr[e-1]):
                last+=1
                peek=last
                ans+=last
                acc=0
            elif(arr[e]==arr[e-1]):
                peek=1
                acc=0
                last=1
                ans+=1
            else:
                last=1
                acc+=1
                if(acc==peek):
                    peek+=1
                    ans+=1
                ans+=acc
    return int(ans)





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
