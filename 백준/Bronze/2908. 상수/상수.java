import java.util.*;

import javax.swing.plaf.synth.SynthSpinnerUI;

import java.io.*;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		String A = st.nextToken();
		String B = st.nextToken();
		
		char[] c1 = A.toCharArray();
		char[] c2 = B.toCharArray();
		
		c1 = reverse(c1);
		c2 = reverse(c2);

		int a = Integer.parseInt(String.valueOf(c1));
		int b = Integer.parseInt(String.valueOf(c2));
		
		if(a > b) {
			System.out.println(a);
		}else {
			System.out.println(b);
		}
		
	}
	static char[] reverse(char[] c) {
		char[] arr = new char[c.length];
		for(int i = 0;i < c.length;i ++) {
			arr[c.length - 1 - i] = c[i];
		}
		return arr;
	}
}