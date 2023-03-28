import java.util.Scanner;

public class Main {
    public static void main(String[] args){
    	Scanner sc = new Scanner(System.in);
    
    	int t = sc.nextInt();
    	for(int i=0;i<t;i++) {
    		int n = sc.nextInt();
    		
    		System.out.println(recursive(n));
    	}
    	
    }
    static int dp[] = new int[12];
    static int recursive(int num) {
    	if(num == 1)
    		return 1;
    	else if(num == 2)
    		return 2;
    	else if (num == 3)
    		return 4;
    	dp[num] = recursive(num - 1) + recursive(num - 2) + recursive(num - 3);
    	return dp[num];
    }
}