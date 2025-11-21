class MyQueue {
    int[] queue;
    int rear, front;
    public MyQueue() {
        queue = new int[10000];
        rear = 0;
        front = 0;
        
    }
    
    public void push(int x) {
        queue[rear] = x;
        rear++;
    }
    
    public int pop() {
        if(empty()) return -1;
        int value = queue[front];
        front++;
        return value;
    }
    
    public int peek() {
        if(empty()) return -1;
        return queue[front];
    }
    
    public boolean empty() {
        return rear == front;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
