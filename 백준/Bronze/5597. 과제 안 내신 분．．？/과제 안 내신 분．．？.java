import java.util.*;
import java.io.*;

public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		boolean[] arr = new boolean[31];
		int tmp;
		for(int i = 0; i < 28; i ++) {
			tmp = Integer.parseInt(br.readLine());
			arr[tmp] = true;
		}
		for(int i = 1; i < 31; i ++) {
			if (!arr[i]) {
				System.out.println(i);
			}
		}
	}
}
