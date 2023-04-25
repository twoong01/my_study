import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		for(int i = 0; i < n; i ++) {
			String word = br.readLine();
			System.out.print(word.charAt(0));
			System.out.println(word.charAt(word.length() - 1));
		}
	}
}
