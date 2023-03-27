import java.util.Scanner;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args){
    	Scanner sc = new Scanner(System.in);
    	BigInteger A = sc.nextBigInteger();
    	BigInteger B = sc.nextBigInteger();
    	BigInteger C = sc.nextBigInteger();
    	
    	System.out.printf("%d", A.add(B.add(C)));
    }
}