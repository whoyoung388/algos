//
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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

    
// Reverse layer (I think this is not valid solution)
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
