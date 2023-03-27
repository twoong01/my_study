import java.util.Scanner;

public class Main {
    public static void main(String[] args){
    	Scanner sc = new Scanner(System.in);
    	
    	int t = sc.nextInt();
    	int A = 0;
    	int B = 0;
    	int C = 0;
    	
    	if (t % 10 != 0)
    		System.out.print(-1);
    	else {
    		A = t / 300;
    		B = (t % 300)/ 60;
    		C = (t % 300 % 60) / 10;
        	System.out.printf("%d ", A);
        	System.out.printf("%d ", B);
        	System.out.printf("%d ", C);
    	}
    }
}