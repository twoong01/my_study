import java.math.BigInteger;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		BigInteger A = scan.nextBigInteger();
		BigInteger B = scan.nextBigInteger();
		BigInteger sum, sub, mul;
		
		sum = A.add(B);
		sub = A.subtract(B);
		mul = A.multiply(B);
		
		
		System.out.printf("%d\n%d\n%d", sum, sub, mul);
		
	}
}