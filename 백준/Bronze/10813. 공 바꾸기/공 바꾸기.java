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
		
		
		for(int i = 0; i < m; i++) {
			StringTokenizer st1 = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st1.nextToken());
			int b = Integer.parseInt(st1.nextToken());
			int tmp = arr[a - 1];
			arr[a - 1] = arr[b - 1];
			arr[b - 1] = tmp;
		}
		
		for(int i = 0; i < n; i++) {
			sb.append(arr[i]).append(" ");
		}
		bw.write(sb.toString());
		bw.flush();
	}
}
