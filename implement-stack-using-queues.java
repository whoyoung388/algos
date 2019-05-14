class MyStack {

    private Queue<Integer> que1, que2;
    private int top;

    /** Initialize your data structure here. */
    public MyStack() {
        this.que1 = new LinkedList<>();
        this.que2 = new LinkedList<>();
    }
    
    /** Push element x onto stack. */
    public void push(int x) {
        que1.add(x);
        top = x;
    }
    
    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        while (que1.size() != 1) {
            top = que1.poll();
            que2.add(top);
        }
        int res = que1.poll();
        Queue<Integer> temp = que1;
        que1 = que2;
        que2 = temp;
        return res;
    }
    
    /** Get the top element. */
    public int top() {
        return top;
    }
    
    /** Returns whether the stack is empty. */
    public boolean empty() {
        return que1.size() == 0;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */
