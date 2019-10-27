# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return TreeNode(val)
        tmp = root
        flag = True
        
        while flag:
            if val > tmp.val:
                if tmp.right == None:
                    tmp.right = TreeNode(val)
                    flag=False
                tmp = tmp.right
            else:
                if tmp.left == None:
                    tmp.left = TreeNode(val)
                    flag=False
                tmp = tmp.left
                
        return root
