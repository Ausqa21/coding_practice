package leetcode.medium;

/**
 * constraints
 * --
 * -231 <= x <= 231 - 1
 * 
 * base case(s)
 * --
 * 
 * 
 * pseudocode
 * --
 * convert int into a string
 * reverse the string
 * convert string into int and return int
 * catch overflow exception and return 0
 */

public class ReverseInteger {
    public int reverse(int x) {
        String str = x < 0 ? String.valueOf(x * (-1)) : String.valueOf(x);

        if (str.length() == 1) {
            return x;
        }

        char[] reversed = new char[str.length()];
        for (int i = str.length() - 1; i >= 0; i--) {
            int m = (str.length() - 1) - i;
            reversed[m] = str.charAt(i);
        }

        String res_str = String.valueOf(reversed);

        int n;
        try {
            n = x < 0 ? Integer.parseInt(res_str) * (-1) : Integer.parseInt(res_str);
        } catch (Exception e) {
            return 0;
        }
        
        return n;
    }

    public static void main(String[] args) {
        ReverseInteger reverseInteger = new ReverseInteger();
        System.out.println(reverseInteger.reverse(2122222299));
        System.out.println(reverseInteger.reverse(2147483647));
        System.out.println(reverseInteger.reverse(-2147483648));
        System.out.println(reverseInteger.reverse(-11));
        System.out.println(reverseInteger.reverse(0));
    }
}
