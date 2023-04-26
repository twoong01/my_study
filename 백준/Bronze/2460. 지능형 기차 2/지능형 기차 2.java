import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int now = 0;
		int mx = Integer.MIN_VALUE;
		for (int i = 0;i < 10; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int outside = Integer.parseInt(st.nextToken());
			int inside = Integer.parseInt(st.nextToken());
			now += inside - outside;
			mx = Math.max(mx, now);
		}
		System.out.println(mx);
	}
}
