/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    
    public TreeNode solve(TreeNode node){
        if(node.left!=null)node.left=solve(node.left);
        if(node.right!=null)node.right=solve(node.right);
        if(node.val==0 && node.left==null && node.right==null)return null;
        return node;
    }
    
    public TreeNode pruneTree(TreeNode root) {
        TreeNode ans=solve(root);
        return ans;
    }
}