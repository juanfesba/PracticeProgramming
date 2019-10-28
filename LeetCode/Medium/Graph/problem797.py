class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        ans=[]
        goal = len(graph)-1
        stack = []
        
        
        def DFS(node):
            nonlocal stack
            stack.append(node)
            
            if node==goal:
                ans.append(stack[:])
            else:
                for adjacent in graph[node]:
                    DFS(adjacent)
                    stack.pop()
                    
        DFS(0)    
        return ans
