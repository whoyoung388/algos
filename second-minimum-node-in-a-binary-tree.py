# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        res = [root.val, float("inf")]
        self.dfs(root, res)
        return -1 if res[1] == float("inf") else res[1]
    
    def dfs(self, root, res):
        if not root:
            return
        self.dfs(root.left, res)
        self.dfs(root.right, res)
        
        if res[0] < root.val < res[1]:
            res[1] = root.val
