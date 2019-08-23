# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        ans=list()
        if root==None:
            return ans
        delkeys=set()
        for e in to_delete:
            delkeys.add(e)
            
        def buildForest(node,flag):
            tmp=TreeNode(node.val)
            if node.val in delkeys:
                tmp=None
                if node.left!=None:
                    buildForest(node.left,True)
                if node.right!=None:
                    buildForest(node.right,True)
            else:
                if node.left!=None:
                    tmp.left=buildForest(node.left,False)
                if node.right!=None:
                    tmp.right=buildForest(node.right,False)
            if flag and tmp!=None:
                ans.append(tmp)
            return tmp
            
        
        buildForest(root,True)
        return ans
