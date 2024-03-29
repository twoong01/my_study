import java.util.Scanner;

public class Main {
	public static void main(String[] args){
    	Scanner sc = new Scanner(System.in);
    	int num = sc.nextInt();
    	solve(num);
    	
    }
    static void solve(int n) {
    	long[][] dp = new long[101][11];
    	// dp[n][l] = dp[n - 1][l - 1] + dp[n - 1][l + 1]
    	
    	for(int i = 1; i <= 9; i ++) {
    		dp[1][i] = 1;
    	}
		for(int i = 2; i <= n;i++) {
    		dp[i][0] = dp[i - 1][1];
    		for (int j = 1;j <= 9;j++) {
    			dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % 1000000000;
    		}
    	}
    	long sum = 0;
    	for(int i = 0; i < 10; i ++) {
    		sum += dp[n][i];
    	}
    	System.out.println(sum % 1000000000);
    }
}