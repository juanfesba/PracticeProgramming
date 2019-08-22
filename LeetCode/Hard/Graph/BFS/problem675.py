class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        ans=0
        curx=0
        cury=0
        delta=[(1,0),(0,1),(-1,0),(0,-1)]
        def BFS(i,j):
            if curx==i and cury==j:return 0
            visited=[[False for e in range(len(forest[0]))] for ee in range(len(forest))]
            dist=-1
            visited[curx][cury]=True
            queue=[(curx,cury)]
            level=0
            sizelevel=len(queue)
            while(len(queue)>0):
                node=queue.pop()
                sizelevel-=1
                for move in delta:
                    newx=node[0]+move[0]
                    newy=node[1]+move[1]
                    if 0<=newx<len(forest) and 0<=newy<len(forest[0]) and not visited[newx][newy]:
                        visited[newx][newy]=True
                        if newx==i and newy==j:
                            return level+1
                        if forest[newx][newy]!=0:
                            queue.insert(0,(newx,newy))
                if sizelevel==0:
                    level+=1
                    sizelevel=len(queue)
            return dist
        
        order=[]
        for i in range(len(forest)):
            for j in range(len(forest[0])):
                if forest[i][j]>1:
                    order.append((forest[i][j],i,j))
        order.sort(key=lambda x:x[0])
        for tree in order:
            new=BFS(tree[1],tree[2])
            if new==-1:
                return -1
            ans+=new
            curx=tree[1]
            cury=tree[2]
        return ans
