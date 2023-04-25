import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		
		int t = Integer.parseInt(br.readLine());
		for(int i = 0; i < t; i ++) {
			StringBuilder sb = new StringBuilder();
			StringTokenizer st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			String tmp = st.nextToken();
			for(int k = 0; k < tmp.length();k ++) {
			for(int j = 0; j < n; j ++) {
				sb.append(tmp.charAt(k));
			}}
			System.out.println(sb.toString());
		}
	}
}