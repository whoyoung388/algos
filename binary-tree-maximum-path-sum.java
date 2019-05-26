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
    
    private int res;
    
    public int maxPathSum(TreeNode root) {
        this.res = root.val;
        maxGain(root);
        return res;
    }
    
    private int maxGain(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int left, right;
        left = Math.max(maxGain(root.left), 0);
        right = Math.max(maxGain(root.right), 0);
        if (root.val + left + right > this.res) {
            this.res = root.val + left + right;
        }
        if (root.val + Math.max(left, right) > this.res) {
            this.res = root.val + Math.max(left, right);
        }
        
        return root.val + Math.max(left, right);
    }
}
