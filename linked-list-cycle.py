# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Two pointers: Space O(1)
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        dummy = ListNode(-1)
        dummy.next = head
        fast, slow = dummy, dummy
        
        while fast and fast.next and slow:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True
        return False

# HashTable: Space O(n)
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        seen = set()
        node = head
        while node:
            if node in seen:
                return True
            seen.add(node)
            node = node.next
        
        return False
        
