// Array Numbers must be unrepeated

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Collections;

public class Sort{
    double[] SelectionSort(double[] input){
        double[] output = new double[input.length];
        for (int i = 0; i < input.length; i++){
            output[i] = SelectMIN(input);
        }
        return output;
    }

    double SelectMIN(double[] input){
        double output = 100000.0;
        for (double v : input) {
            if (v < output) {
                output = v;
            }
        }
        return output;
    }

    int IndexMIN(double[] input){
        double num = 100000.0;
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
