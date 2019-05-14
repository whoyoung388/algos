class MovingAverage {
    
    private Queue<Integer> queue;
    private int size;
    private double sum;
    
    /** Initialize your data structure here. */
    public MovingAverage(int size) {
        queue = new LinkedList<Integer>();
        this.size = size;
    }
    
    public double next(int val) {
        queue.offer(val);
        sum += val;
        
        if (queue.size() > size) {
            sum -= queue.poll();
        }
        return sum / queue.size();
    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.next(val);
 */
