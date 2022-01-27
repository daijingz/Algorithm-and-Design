// Jingze Dai, 400201059, daij24

public class KMP {
    private static int[] longest_suffix_prefix(String A, String B){
        String P = B + A;
        int i = 0;
        int k = -1;
        int m = P.length();
        int[] next = new int[m + 1];
        next[0] = -1;
        while (i < m) {
            while (k >= 0 && P.charAt(k) != P.charAt(i)){
                k = next[k];
            }
            i = i + 1;
            k = k + 1;
            next[i] = k;
        }
        return next;
    }

    public static void main(String[] args){
        String A = "aabbccdd";
        String B = "bbccddaaddee";
        int[] output = longest_suffix_prefix(A, B);
        System.out.println("Matched Longest Suffix with Prefix: ");
        if (output[A.length() + B.length()] > 0) {
            System.out.println(B.substring(0, output[A.length() + B.length()]));
            System.out.println("Length: " + output[A.length() + B.length()]);
        } else {
            System.out.println("This is an empty string (with length 0)");
        }
    }
}
