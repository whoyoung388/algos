# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        prev_node = dummy

        while head:
            if head.val == prev_node.val:
                prev_node.next = head.next
            else:
                prev_node = head
            head = head.next
            
        
        return dummy.next
