package hackerrank.java.easy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class JavaPrimalityTest {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String n = bufferedReader.readLine();

        System.out.println(new BigInteger(n).isProbablePrime(1) ? "prime" : "not prime");

        bufferedReader.close();
    }
}
