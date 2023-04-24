import java.util.*;
import java.io.*;

public class Main {
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		HashSet<Integer> hash_set = new HashSet<Integer>();
		for(int i = 0; i < 10; i++) {
			int n = Integer.parseInt(br.readLine());
			int tmp = n % 42;
			hash_set.add(tmp);
		}
		System.out.println(hash_set.size());
	}
}
