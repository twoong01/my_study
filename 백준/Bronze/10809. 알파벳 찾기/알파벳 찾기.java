import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		String word = br.readLine();
		
		for(char c = 'a'; c <= 'z'; ++c) {
			sb.append(word.indexOf(c)).append(" ");
		}
		System.out.println(sb.toString());
	}
}