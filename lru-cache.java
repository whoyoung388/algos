class DListNode {
    public int key;
    public int value;
    public DListNode prev;
    public DListNode next;
    
    public DListNode(int key, int value) {
        this.key = key;
        this.value = value;
        this.prev = null;
        this.next = null;
    }
}

class LRUCache {
    
    private int capacity;
    private DListNode head = new DListNode(-1, -1);
    private DListNode tail = new DListNode(-1, -1);
    private HashMap<Integer, DListNode> hashmap = new HashMap<>();

    public LRUCache(int capacity) {
        this.capacity = capacity;
        head.next = tail;
        tail.prev = head;
    }

    public int get(int key) {
        if (!hashmap.containsKey(key)) {
            return -1;
        }
        DListNode node = hashmap.get(key);
        node.prev.next = node.next;
        node.next.prev = node.prev;

        node.next = tail;
        node.prev = tail.prev;
        tail.prev.next = node;
        tail.prev = node;
        return node.value;
    }

    public void put(int key, int value) {
        if (get(key) != -1) {
            DListNode node = hashmap.get(key);
            node.value = value;
            return;
        }
        
        if (hashmap.size() == capacity) {
            hashmap.remove(head.next.key);
            head.next = head.next.next;
            head.next.prev = head;
        }
        
        DListNode node = new DListNode(key, value);
        hashmap.put(key, node);
        node.next = tail;
        node.prev = tail.prev;
        tail.prev.next = node;
        tail.prev = node;
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
