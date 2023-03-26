import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		String c = scan.next();
		
		int ans = Integer.parseInt(c, 16);
		
		
		System.out.printf("%d", ans);
	}
}