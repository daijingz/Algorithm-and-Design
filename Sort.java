// Array Numbers must be unrepeated

public class Sort{
    int[] Selection_Sort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n-1; i++){
            int min_idx = i;
            for (int j = i+1; j < n; j++)
                if (arr[j] < arr[min_idx])
                    min_idx = j;

            int temp = arr[min_idx];
            arr[min_idx] = arr[i];
            arr[i] = temp;
        }
        return arr;
    }

    int[] Insertion_Sort(int[] arr){
        int n = arr.length;
        for (int i = 1; i < n; ++i) {
            int key = arr[i];
            int j = i - 1;

            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key;
        }
        return arr;
    }

    void merge(int arr[], int l, int m, int r) {
        int n1 = m - l + 1;
        int n2 = r - m;

        int L[] = new int[n1];
        int R[] = new int[n2];

        for (int i = 0; i < n1; ++i) {
            L[i] = arr[l + i];
        }
        for (int j = 0; j < n2; ++j) {
            R[j] = arr[m + 1 + j];
        }

        int i = 0, j = 0;
        int k = l;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            }
            else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }

        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }

    int[] Merge_Sort(int arr[], int l, int r) {
        if (l < r) {
            int m =l+ (r-l)/2;
            Merge_Sort(arr, l, m);
            Merge_Sort(arr,m + 1, r);
            merge(arr, l, m, r);
        }
        return arr;
    }

    int[] Shell_Sort(int[] arr) {
        int n = arr.length;
        for (int gap = n/2; gap > 0; gap /= 2) {
            for (int i = gap; i < n; i += 1) {
                int temp = arr[i];
                int j;
                for (j = i; j >= gap && arr[j - gap] > temp; j -= gap)
                    arr[j] = arr[j - gap];
                arr[j] = temp;
            }
        }
        return arr;
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
