# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import copy

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if root==None:
            return []
        
        def depth(node):
            if node.left==None and node.right==None:
                node.val=1
            
            if node.left!=None:
                depth(node.left)
                left=node.left.val
            else:
                left=0
            if node.right!=None:
                depth(node.right)
                right=node.right.val
            else:
                right=0
            node.val=max(left,right)+1
                
            
        
        rootNew=copy.deepcopy(root)
        depth(rootNew)
        
        
        def solve(node,nodeNew):
            if(node.left==None and node.right==None):
                return node
            if(node.right==None):
                return solve(node.left,nodeNew.left)
            if(node.left==None):
                return solve(node.right,nodeNew.right)
            if nodeNew.left.val == nodeNew.right.val:
                return node
            if nodeNew.left.val > nodeNew.right.val:
                return solve(node.left,nodeNew.left)
            else:
                return solve(node.right,nodeNew.right)
        
        return solve(root,rootNew)
