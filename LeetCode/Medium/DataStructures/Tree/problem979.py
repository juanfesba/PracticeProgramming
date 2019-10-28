# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        ans=0
        
        def calc(node):
            nonlocal ans
            val = node.val - 1
            
            if node.left!=None:
                left=calc(node.left)
            else:
                left=0
            if node.right !=None:
                right=calc(node.right)
            else:
                right=0
                
            val+=left + right
            ans+=abs(val)
            
            return val
        
        calc(root)
        return ans
