# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


// TLE Solution, Time: O(kN), k = len(lists)
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = curr = ListNode(-1)
        
        while any(lists):
            nodeIndex = self.selectNext(lists)
            curr.next = ListNode(lists[nodeIndex].val)
            curr = curr.next
            lists[nodeIndex] = lists[nodeIndex].next
        return head.next

    def selectNext(self, lists):
        select = None
        for i, node in enumerate(lists):
            if not node:
                continue
            if select == None:
                select = i
                continue
            if node.val < lists[select].val:
                select = i
        return select




class PriorityQueue(object):
    def __init__(self, ):
        self.que = [None,]

    def isEmpty(self):
        return len(self.que) < 2
        
    def push(self, node: ListNode) -> None:
        self.que.append(node)
        self._compare_up()
    
    def pop(self) -> ListNode:
        if len(self.que) == 1:
            return None
        top = self.que[1]
        self._swape(1, len(self.que)-1)
        self.que.pop()
        self._compare_down()
        return top
    
    def _find_parentIndex(self, index):
        if index < 2:
            return None
        return index // 2

    def _find_childrenIndexes(self, index):
        res = []
        if index * 2 < len(self.que):
            res.append(index * 2)
        if index * 2 + 1 < len(self.que):
            res.append(index * 2 + 1)
        return res
    
    def _compare_up(self):
        currIndex = len(self.que) - 1
        while True:
            parentIndex = self._find_parentIndex(currIndex)
            if not parentIndex:
                return
            if self.que[parentIndex].val <= self.que[currIndex].val:
                return
            self._swape(currIndex, parentIndex)
            currIndex = parentIndex

    def _compare_down(self):
        currIndex = 1
        while True:
            childs = self._find_childrenIndexes(currIndex)
            if not childs:
                return
            if len(childs) == 1:
                if self.que[childs[0]].val >= self.que[currIndex].val:
                    return
                self._swape(childs[0], currIndex)
                currIndex = childs[0]
                return
            if self.que[childs[0]].val < self.que[childs[1]].val:
                if self.que[childs[0]].val >= self.que[currIndex].val:
                    return
                self._swape(childs[0], currIndex)
                currIndex = childs[0]
            else:
                if self.que[childs[1]].val >= self.que[currIndex].val:
                    return
                self._swape(childs[1], currIndex)
                currIndex = childs[1]

    def _swape(self, index1, index2):
        self.que[index1], self.que[index2] = self.que[index2], self.que[index1]

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        queue = PriorityQueue()
        for node in lists:
            if not node:
                continue
            queue.push(node)
        
        head = curr = ListNode(-1)
        while not queue.isEmpty():
            node = queue.pop()
            curr.next = node
            curr = curr.next
            if node.next:
                queue.push(node.next)
        
        return head.next
