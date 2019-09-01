"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        dummy = curr = Node(-1, None, None)
        table = {}
        
        # go through "next" pointer only
        root = head
        while root:
            # record the mapping
            node = Node(root.val, None, None)
            table[root] = node
            
            curr.next = node
            curr = curr.next
            root = root.next
        
        # copy the "random" pointer
        root = head
        while root:
            if not root.random:
                root = root.next
                continue
            cnode = table[root]
            rnode = table[root.random]
            cnode.random = rnode
            
            root = root.next
            
        return dummy.next
        
        
        
