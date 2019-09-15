from sys import stdin
from sys import stdout

from collections import defaultdict

from heapq import heappop,heappush

INF=float("inf")

N,M=[int(x) for x in stdin.readline().strip().split()]

global graph,inversegraph,forbidden

def forbidSSSP(source,destiny,n):
   global graph,forbidden
   dist=[ INF for i in range(n) ]
   dist[source]=0
   visited = [False for i in range(n)]
   parent=[list() for i in range(n)]
   parent[source]=[-1]
   heap=[ (0,source) ]
   forbidden=set()

   def forbid(node):
      nodes=parent[node]
      for nod in nodes:
         if (nod in forbidden) or (nod==source):
            continue
         forbidden.add(nod)
         forbid(nod)

   while len(heap)!=0:
      d,u=heappop(heap)

      if u==destiny:
         forbid(destiny)
         return d
      if not(visited[u]):
         visited[u]=True
         for v,w in graph[u]:
            if dist[v]>d+w:
               parent[v]=[u]
               dist[v]=d+w
               heappush(heap,(dist[v],v))
            elif dist[v]==d+w:
               parent[v].append(u)
   return INF

def almostSSSP(source,destiny,n,best):
   global inversegraph,forbidden
   dist=[ INF for i in range(n) ]
   dist[source]=0
   visited = [False for i in range(n)]
   heap=[ (0,source) ]

   for node in forbidden:
      visited[node]=True
   while len(heap)!=0:
      d,u=heappop(heap)
      if u==destiny:
         if d>best:
            return d
      elif not(visited[u]):
         visited[u]=True
         for v,w in inversegraph[u]:
            if v==destiny and d+w==best:
               continue
            if dist[v]>d+w:
               dist[v]=d+w
               heappush(heap,(dist[v],v))
   return -1

while(N!=0):
   source,destiny=[int(x) for x in stdin.readline().strip().split()]      
   graph=defaultdict(list)
   inversegraph=defaultdict(list)
   for i in range(M):
      u,v,d=[int(x) for x in stdin.readline().strip().split()]
      graph[u].append((v,d))
      inversegraph[v].append((u,d))
   best=forbidSSSP(source,destiny,N)
   ans=almostSSSP(destiny,source,N,best)

   stdout.write(str(ans)+"\n")

   N,M=[int(x) for x in stdin.readline().strip().split()]

stdout.close()
