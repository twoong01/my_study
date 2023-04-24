import java.util.*;
import java.io.*;

public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		int[] arr = new int[n];
		for(int i = 0; i < m; i ++) {
			StringTokenizer st1 = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st1.nextToken());
			int b = Integer.parseInt(st1.nextToken());
			int k = Integer.parseInt(st1.nextToken());
			for(int j = a - 1; j < b;j++) {
				arr[j] = k;
			}
		}
		for(int i = 0;i < arr.length; i ++) {
			sb.append(arr[i]).append(" ");
		}
		bw.write(sb.toString());
		bw.flush();
	}

}
