import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int A = scan.nextInt();
		int B = scan.nextInt();
		
		System.out.printf("%d\n", A + B);
		System.out.printf("%d\n", A - B);
		System.out.printf("%d\n", A * B);
		System.out.printf("%d\n", A / B);
		System.out.printf("%d", A % B);
	}

}
