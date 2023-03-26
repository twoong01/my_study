import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int n = scan.nextInt();
		int t = scan.nextInt();
		int c = scan.nextInt();
		int p  = scan.nextInt();
	
		System.out.printf("%d", (n - 1) / t * c * p);
	}
}