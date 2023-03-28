import java.util.Scanner;

public class Main {
    public static void main(String[] args){
    	Scanner sc = new Scanner(System.in);
    	
    	int n = sc.nextInt();
    	int k = sc.nextInt();
    	int[] lst = new int[n + 1];
    	int j = 1;
    	
    	for(int i=1;i<n+1;i++) {
    		lst[i] = -1;
    	}
    	for(int i=1;i<n+1;i++) {
    		if(n % i == 0) {
    			lst[j] = i;
    			j++;
    		}
    	}
    	if(lst[k] == - 1)
    		System.out.println(0);
    	else
    		System.out.println(lst[k]);
    	
    }
}