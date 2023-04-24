import java.util.*;
import java.io.*;

public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int mx = Integer.MIN_VALUE;
		int idx = 0;
		int[] arr = new int[9];
		for(int i = 0; i < 9; i ++) {
			int tmp = Integer.parseInt(br.readLine());
			if(tmp > mx) {
				idx = i + 1;
				mx = tmp;
			}
		}
		System.out.println(mx);
		System.out.println(idx);
	}

}
