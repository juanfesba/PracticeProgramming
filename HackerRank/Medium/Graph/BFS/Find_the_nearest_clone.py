#!/bin/python3

import math
import os
import random
import re
import sys

from collections import defaultdict
from collections import deque
# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
def findShortest(nodes, graph, ids, val):
    queue=deque()
    visited=[-1]*nodes
    for e in range(len(ids)):
        if ids[e]==val:
            queue.append(e+1)
            visited[e]=0
    ans=-1
    level=1
    ref=len(queue)
    flag=True
    if ref<2:
        flag=False
    while(len(queue)!=0 and flag):
        current=queue.popleft()
        if(ref==0):
            level+=1
            ref=len(queue)
        ref-=1
        for e in graph[current]:
            if visited[e-1]==-1:
                visited[e-1]=level
                queue.append(e)
            elif level<=visited[e-1]+1:
                ans=level+visited[e-1]
                flag=False
                break

    # solve here
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph=defaultdict(list)
    for i in range(graph_edges):
        u,v=input().split()
        graph[int(u)].append(int(v))
        graph[int(v)].append(int(u))

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph,ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()
