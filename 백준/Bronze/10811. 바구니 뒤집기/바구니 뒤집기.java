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
		for(int i = 0; i < n; i ++) {
			arr[i] = i + 1;
		}
		for(int i = 0; i < m; i ++) {
			StringTokenizer st1 = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st1.nextToken()) - 1;
			int b = Integer.parseInt(st1.nextToken()) - 1;
			while(a < b) {
				int tmp = arr[a];
				arr[a++] = arr[b];
				arr[b--] = tmp;
			}
		}
		for(int i = 0;i < arr.length;i++) {
			sb.append(arr[i]).append(" ");
		}
		System.out.println(sb.toString());
	}
}
