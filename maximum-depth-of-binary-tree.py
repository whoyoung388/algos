# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

// BFS
import collections
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = 0
        que = collections.deque()
        que.append(root)
        while que:
            for _ in range(len(que)):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            depth += 1

        return depth


// DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = self.dfs(root, 0)
        return depth

    def dfs(self, root, depth):
        if not root:
            return depth

        return max(self.dfs(root.left, depth+1),
                   self.dfs(root.right, depth+1))

