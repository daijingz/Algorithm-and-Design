public class Queue {
    private int[] values;
    private int length;
    private int front;
    private int back;

    public Queue() {
        this.values = new int[10];
        this.length = 0;
        this.front = 0;
        this.back = 0;
    }

    public int[] get_values(){
        return this.values;
    }

    public int get_length(){
        return this.length;
    }

    public int get_front(){
        return this.front;
    }

    public int get_back(){
        return this.back;
    }

    public void enqueue(int value) {
        if (this.back == this.values.length - 1) {
            this.back ++;
            this.length ++;
            int[] new_values = new int[this.length];
            System.arraycopy(this.values, 0, new_values, 0, this.values.length);
            new_values[this.length - 1] = value;
            this.values = new_values;
        } else {
            this.length ++;
            this.values[back] = value;
            this.back++;
        }
    }

    public int dequeue() {
        int output = this.values[this.front];
        this.length = this.length - 1;
        if (this.front == this.length) {
            this.front = 1;
        } else {
            this.front ++;
        }
        return output;
    }
}
