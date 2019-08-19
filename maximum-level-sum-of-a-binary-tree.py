# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        res = 0
        curr_max = float('-inf')
        
        queue = deque([root])
        layer = 0
        
        while queue:
            layer += 1
            repeats = len(queue)
            level = []
            for _ in range(repeats):
                node = queue.popleft()
                if node is None: 
                    continue
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            if sum(level) > curr_max:
                curr_max = sum(level)
                res = layer
        
        return res
