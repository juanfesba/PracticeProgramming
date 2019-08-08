#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    ans=0
    dict=defaultdict(list)
    for e in range(len(arr)):
        
        keycheck=arr[e]/(r*r)
        if(keycheck==int(keycheck)):
            check=dict.get(int(keycheck))
            if(check!=None):
                ans+=check[0]
                ans+=check[1]*check[2]

        keycheck=arr[e]/r
        if(keycheck==int(keycheck)):
            check=dict.get(int(keycheck))
            if(check!=None):
                dict[int(arr[e]/r)][2]+=1

        check=dict.get(arr[e])
        if(check==None):
            dict[arr[e]].append(0)
            dict[arr[e]].append(1)
            dict[arr[e]].append(0)
        else:
            dict[arr[e]][0]+=dict[arr[e]][1]*dict[arr[e]][2]
            dict[arr[e]][1]+=1
            dict[arr[e]][2]=0
        
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
