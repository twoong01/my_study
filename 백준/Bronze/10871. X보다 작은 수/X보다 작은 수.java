import java.util.*;
import java.io.*;

public class Main {
	
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringBuilder sb = new StringBuilder();
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int x = Integer.parseInt(st.nextToken());
		
		int[] arr = new int[n];
		
		StringTokenizer st1 = new StringTokenizer(br.readLine());
		for(int i=0;i<n;i++) {
			arr[i] = Integer.parseInt(st1.nextToken());
		}
		
		for(int i = 0; i < arr.length; i++) {
			if(arr[i] < x) {
				sb.append(arr[i]).append(" ");
			}
		}
		System.out.println(sb.toString());
	}

}
