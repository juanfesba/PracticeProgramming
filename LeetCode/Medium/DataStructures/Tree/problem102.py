# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans=[]
        
        
        def BFS(node):
            current=list()
            queue=[node]
            sizeLevel=1
            while(len(queue)>0):
                peek=queue.pop(0)
                current.append(peek.val)
                sizeLevel-=1
                
                if peek.left!=None:
                    queue.append(peek.left)
                if peek.right!=None:
                    queue.append(peek.right)
                
                if(sizeLevel==0):
                    ans.append(current)
                    current=list()
                    sizeLevel=len(queue)
        
        if root!=None:
            BFS(root)
        return ans
