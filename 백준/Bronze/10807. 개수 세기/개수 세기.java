import java.util.*;
import java.io.*;

public class Main {
	
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		String[] reader = new String[n];
		int[] arr = new int[n];
		int cnt = 0;
		
		reader = br.readLine().split(" ");
		for(int i = 0; i < n; i ++) { 
			arr[i] = Integer.parseInt(reader[i]);
		}
		
		int target = Integer.parseInt(br.readLine());
		for(int i = 0; i < arr.length; i ++) {
			if (arr[i] == target) {
				cnt ++;
			}
		}
		System.out.println(cnt);
		
		
		
	}

}
