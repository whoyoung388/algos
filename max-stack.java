class Node {
    int val;
    Node prev, next;
    public Node(int x) {
        this.val = x;
    }
}

class DoubleLinkedList {
    Node head, tail;
    
    public DoubleLinkedList() {
        head = new Node(-1);
        tail = new Node(-1);
        head.next = tail;
        tail.prev = head;
    }
    
    public Node add(int x) {
        // You better return the Node obj
        // Think about why?
        Node node = new Node(x);
        node.prev = tail.prev;
        node.next = tail;
        tail.prev.next = node;
        tail.prev = node;
        return node;
    }
    
    public int peek() {
        return tail.prev.val;
    }
    
    public Node pop() {
        return unlink(tail.prev);
    }
    
    public Node unlink(Node node) {
        node.next.prev = node.prev;
        node.prev.next = node.next;
        return node;
    }
}


class MaxStack {

    DoubleLinkedList dl;
    TreeMap<Integer, List<Node>> map;
    
    /** initialize your data structure here. */
    public MaxStack() {
        dl = new DoubleLinkedList();
        map = new TreeMap();
    }
    
    public void push(int x) {
        // Create Node obj
        Node node = dl.add(x);
        // Add the Node obj to TreeMap
        if (!map.containsKey(x)) {
            map.put(x, new ArrayList<Node>());
        }
        map.get(x).add(node);
    }
    
    public int pop() {
        Node node = dl.pop();
        List<Node> l = map.get(node.val);
        l.remove(l.size() - 1);
        if (l.isEmpty()) {
            map.remove(node.val);
        }
        return node.val;
    }
    
    public int top() {
        return dl.peek();
    }
    
    public int peekMax() {
        return map.lastKey();
    }
    
    public int popMax() {
        int max = peekMax();
        List<Node> l = map.get(max);
        Node maxNode = l.remove(l.size() - 1);
        if (l.isEmpty()) {
            map.remove(max);
        }
        dl.unlink(maxNode);
        return max;
    }
}

/**
 * Your MaxStack object will be instantiated and called as such:
 * MaxStack obj = new MaxStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.peekMax();
 * int param_5 = obj.popMax();
 */
