import java.util.Scanner;


public class Main {
	
	public static void main(String[] args){
    	Scanner sc = new Scanner(System.in);
    	
    	int n = sc.nextInt(); 
    	int[] lst = new int[n + 1];
    	int[] dp = new int[n + 1];
    	
    	for(int i = 1;i < n + 1;i++) {
    		lst[i] = sc.nextInt();
    	}
    	dp[1] = lst[1];
    	if (n > 1)
    		dp[2] = lst[1] + lst[2];

    	for(int i = 3;i < n + 1;i++) {
    		dp[i] = Math.max(dp[i - 3] + lst[i] + lst[i - 1], dp[i - 2] + lst[i]);
    		dp[i] = Math.max(dp[i], dp[i - 1]);
    	}
    	System.out.println(dp[n]);
	}
}