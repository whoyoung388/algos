class DLNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.table = {}
        self.capacity = capacity
        self.head = DLNode(-1, -1)
        self.tail = DLNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.table:
            return -1
        
        node = self.table[key]
        
        # remove node from DL list
        node.prev.next = node.next
        node.next.prev = node.prev
        
        # attach to the front
        node.prev = self.head
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            node = self.table[key]
            node.val = value
            return
    
        if len(self.table) == self.capacity:
            leastUsedNode = self.tail.prev
            del self.table[leastUsedNode.key]
            leastUsedNode.prev.next = self.tail
            self.tail.prev = leastUsedNode.prev
        
        node = DLNode(key, value)
        self.table[key] = node
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
