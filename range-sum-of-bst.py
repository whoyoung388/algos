# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        
        res = []
        self.dfs(root, L, R, res)
        
        return sum(res)

    def dfs(self, node, L, R, res):
        if L <= node.val <= R:
            res.append(node.val)
        if node.val <= R and node.right:
            self.dfs(node.right, L, R, res)
        if node.val >= L and node.left:
            self.dfs(node.left, L, R, res)
            

# BFS
from collections import deque

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        if not root: return 0
        
        queue = deque([root,])
        total = 0
        while queue:
            node = queue.popleft()
            if L <= node.val <= R:
                total += node.val
            
            if node.val <= R and node.right:
                queue.append(node.right)
            if node.val >= L and node.left:
                queue.append(node.left)
    
        return total
