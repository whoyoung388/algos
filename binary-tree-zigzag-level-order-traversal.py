# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# DFS
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, node, layer, res) -> None:
        if not node:
            return
        
        if layer == len(res):
            res.append(deque())
            
        if layer % 2 == 1:
            res[layer].appendleft(node.val)
        else:
            res[layer].append(node.val)

        self.dfs(node.left, layer+1, res)
        self.dfs(node.right, layer+1, res)
        


# BFS
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])
        zag = 0
        while queue:
            layer = deque([])
            for _ in range(len(queue)):
                node = queue.popleft()
                if zag:
                    layer.appendleft(node.val)
                else:
                    layer.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            zag = 1 - zag
            res.append(layer)
        return res

    
# Reverse layer (I think this is not valid solution)
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([root])
        zag = 0
        while queue:
            layer = []
            for _ in range(len(queue)):
                node = queue.popleft()
                layer.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if zag:
                layer = layer[::-1]
            zag = 1 - zag
            res.append(layer)
        return res
