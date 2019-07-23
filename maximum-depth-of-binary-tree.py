# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = self.dfs(root, 0)
        return depth

    def dfs(self, root, depth):
        if not root:
            return depth

        return max(self.dfs(root.left, depth+1),
                   self.dfs(root.right, depth+1))

