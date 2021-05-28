public class Stack {
    private int[] values;
    private int front;
    private int size;

    public Stack(int size){
        this.values = new int[size];
        this.front = 0;
        this.size = size;
    }

    public int[] get_values(){
        return this.values;
    }

    public int get_front(){
        return this.front;
    }

    public int get_size(){
        return this.size;
    }

    public boolean stack_empty(){
        if (this.front == 0 && this.size == 0) {
            return true;
        } else {
            return false;
        }
    }

    public void push(int element){
        this.size = this.size + 1;
        this.values[this.front] = element;
        this.front = this.front + 1;
    }

    public int pop(){
        if (this.stack_empty()){
            throw new IndexOutOfBoundsException();
        } else {
            this.front = this.front - 1;
            return this.values[this.front + 1];
        }
    }
}
