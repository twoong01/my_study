import java.util.*;
import java.io.*;

public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		int mx = Integer.MIN_VALUE;
		float total = 0;
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i = 0; i < n; i ++) {
			int score = Integer.parseInt(st.nextToken());
			total += score;
			mx = Math.max(mx, score);
		}
		System.out.println(total / mx * 100 / n);
	}
}
