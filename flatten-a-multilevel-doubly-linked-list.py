"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return
        self.dfs(head)
        return head
    
    
    def dfs(self, node: 'Node') -> 'Node':
        """
        Return the last not None node
        """
        if node.child:
            tail = self.dfs(node.child)
            tail.next = node.next
            if tail.next:
                node.next.prev = tail
            node.next = node.child
            node.next.prev = node
            node.child = None
            node = tail
            
        if node.next is None:
            return node
        
        return self.dfs(node.next)
