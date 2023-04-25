import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String word = br.readLine();
		int i = Integer.parseInt(br.readLine());
		
		System.out.println(word.charAt(i - 1));
	}

}
