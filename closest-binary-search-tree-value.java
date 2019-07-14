/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

// Iteration
class Solution {
    public int closestValue(TreeNode root, double target) {
        int res = root.val;
        while (root != null) {
            if (Math.abs(root.val - target) < 0.5) {
                return root.val;
            }
            if (Math.abs(root.val - target) < Math.abs(res - target)) {
                res = root.val;
            }
            root = root.val > target ? root.left : root.right;
        }
        return res;
    }
}


// Recursion
class Solution {
    public int closestValue(TreeNode root, double target) {
        TreeNode next = root.val < target ? root.right : root.left;
        if (next == null) {
            return root.val;
        }
        int nextClosest = closestValue(next, target);
        return Math.abs(root.val - target) < Math.abs(nextClosest - target) ? root.val : nextClosest;
    }
}
