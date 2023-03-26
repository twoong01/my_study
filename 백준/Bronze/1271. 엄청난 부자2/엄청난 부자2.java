import java.math.BigInteger;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		BigInteger n = scan.nextBigInteger();
		BigInteger m = scan.nextBigInteger();
		BigInteger avg, rest;
		avg = n.divide(m);
		rest = n.subtract((avg.multiply(m)));
		System.out.printf("%d\n", avg);
		System.out.printf("%d", rest);
	}
}