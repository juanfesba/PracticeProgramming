#!/bin/python3

import math
import os
import random
import re
import sys

class dforest():
    def __init__(self,sizeIn):
        self.size=[1 for e in range(sizeIn)]
        self.rank=[1 for e in range(sizeIn)]
        self.parent=[e for e in range(sizeIn)]
        self.components=n

    def __len__(self):
        return len(self.parent)

    def find(self,x):
        if(x!=self.parent[x]):
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        px,py=self.find(x),self.find(y)
        if(px!=py):
            nx,ny=self.rank[px],self.rank[py]
            if(nx<=ny):
                self.parent[px]=py
                self.size[py]+=self.size[px]
                if(nx==ny):
                    self.rank[py]+=1
            else:
                self.parent[py]=px
                self.size[px]+=self.size[py]
            self.components-=1

    def sizeF(self,x):
        return self.size[self.find(x)]


# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_road>=c_lib:
        return n*c_lib
    components = dforest(n)
    for e in cities:
        components.union(e[0]-1,e[1]-1)
    
    return components.components * c_lib + (n-1) * c_road - (components.components - 1) * c_road

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
