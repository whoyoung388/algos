/* Solution I */
class Node {
    int val, minVal;
    Node next;
    
    public Node(int v, int min) {
        this(v, min, null);
    }
    
    public Node(int v, int min, Node next) {
        this.val = v;
        this.minVal = min;
        this.next = next;
    }
}


class MinStack {

    Node head;
    int minVal;
    
    public void push(int x) {
        if (head == null) {
            minVal = x;
        } else {
            minVal = Math.min(minVal, x);
        }
        head = new Node(x, minVal, head);
    }
    
    public void pop() {
        head = head.next;
        if (head == null) return;
        minVal = head.minVal;
    }
    
    public int top() {
        return head.val;
    }
    
    public int getMin() {
        return head.minVal;
    }
}


/* Solution II */
class MinStack {

    Stack<Integer> stack;
    Stack<Integer> minStack;
    
    /** initialize your data structure here. */
    public MinStack() {
        stack = new Stack<>();
        minStack = new Stack<>();
    }
    
    public void push(int x) {
        stack.push(x);
        int min = minStack.empty() ? x : Math.min(x, getMin());
        minStack.push(min);
    }
    
    public void pop() {
        stack.pop();
        minStack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
