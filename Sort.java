// Array Numbers must be unrepeated

public class Sort{
    int[] SelectionSort(int[] input){
        int[] output = new int[input.length];
        for (int i = 0; i < input.length; i++){
            output[i] = SelectMIN(input);
            int index = IndexMIN(input);
            input[index] = - 100000;
        }
        return output;
    }

    int SelectMIN(int[] input){
        int output = 100000;
        for (int v : input) {
            if (v < output) {
                output = v;
            }
        }
        return output;
    }

    int IndexMIN(int[] input){
        int num = 100000;
        int output = 0;
        for (int i = 0; i < input.length; i++) {
            if (input[i] < num) {
                num = input[i];
                output = i;
            }
        }
        return output;
    }

    double SelectMAX(double[] input){
        double output = -100000.0;
        for (double v : input) {
            if (v > output) {
                output = v;
            }
        }
        return output;
    }

    int IndexMAX(double[] input){
        double num = -100000.0;
        int output = 0;
        for (int i = 0; i < input.length; i++) {
            if (input[i] > num) {
                num = input[i];
                output = i;
            }
        }
        return output;
    }
}
