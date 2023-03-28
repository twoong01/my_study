import java.util.Scanner;

public class Main {
    public static void main(String[] args){
    	Scanner sc = new Scanner(System.in);
    	
    	String b1 = sc.next();
    	String b2 = sc.next(); 
    	
    	long num1 = Integer.parseInt(b1, 2);
    	long num2 = Integer.parseInt(b2, 2);
    	
    	long num_ans = num1 * num2;
    	
    	
    	String ans = Long.toBinaryString(num_ans);
    	
    	System.out.print(ans);
    	
    }
}