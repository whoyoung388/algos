# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []
        while root:
            layer = []
            root = self.dfs(root, layer)
            res.append(layer)
        return res


    def dfs(self, root, layer) -> TreeNode:
        if not root:
            return
        if not (root.left or root.right):
            layer.append(root.val)
            return
        
        root.left = self.dfs(root.left, layer)
        root.right = self.dfs(root.right, layer)
        return root
