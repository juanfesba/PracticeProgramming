# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        
        ans=0
        
        def inOrder(node):
            nonlocal ans
            left,right=0,0
            if node.left!=None:
                left=inOrder(node.left)
            if node.right!=None:
                right=inOrder(node.right)
            if left==1 or right==1:
                ans+=1
                return 2
            if left==2 or right==2:
                return 0
            else:
                return 1
            
        if inOrder(root)==1:
            ans+=1
        return ans
