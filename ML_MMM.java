import java.util.Arrays;

public class ML_MMM {
    double Mean(double[] input){
        double sum = 0;
        for (int i = 0; i <= input.length; i = i + 1){
            sum = sum + input[i];
        }
        return sum/input.length;
    }

    double Median(double[] input){
        Arrays.sort(input);
        if (input.length % 2 == 0){
            int median1 = input.length / 2;
            int median2 = median1 + 1;
            return (input[median1] + input[median2]) / 2;
        } else {
            int median = input.length / 2;
            return input[median];
        }
    }

    double Mode(double[] input){
        double maxValue = 0;
        double maxCount = 0;
        int i;
        int j;

        for (i = 0; i < input.length; ++i) {
            int count = 0;
            for (j = 0; j < input.length; ++j) {
                if (input[j] == input[i])
                    ++count;
            }

            if (count > maxCount) {
                maxCount = count;
                maxValue = input[i];
            }
        }
        return maxValue;
    }

    double Minimum(double[] input){
        double output = 100000.0;
        for (double v : input) {
            if (v < output) {
                output = v;
            }
        }
        return output;
    }

    double Maximum(double[] input){
        double output = -100000.0;
        for (double v : input) {
            if (v > output) {
                output = v;
            }
        }
        return output;
    }
}
