# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.dfs(root, root)

    def dfs(self, left, right):
        if not left and not right:
            return True

        if not (left and right):
            return False

        if left.val != right.val:
            return False

        return self.dfs(left.left, right.right) and self.dfs(left.right, right.left)
