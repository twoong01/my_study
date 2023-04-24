import java.util.*;
import java.io.*;

public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
		
		int n = Integer.parseInt(br.readLine());
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int[] arr = new int[n];
		for(int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		int mx = -1000000;
		int mn = 1000000;
		for(int i = 0; i < n; i ++) {
			if(arr[i] > mx) {
				mx = arr[i];
			}
			if(arr[i] < mn) {
				mn = arr[i];
			}
		}
		sb.append(mn).append(" ");
		sb.append(mx);
		bw.write(sb.toString());
        bw.flush();
	}

}
