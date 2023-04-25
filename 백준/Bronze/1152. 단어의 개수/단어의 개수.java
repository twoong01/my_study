import java.util.*;

import javax.swing.plaf.synth.SynthSpinnerUI;

import java.io.*;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		
		int cnt = 0;
		int block = ' ';
		while (true) {
			int word = System.in.read();
			if(word == '\n') {
				if(block != ' ') cnt ++;
				break;
			}
			if(word == ' ') {
				if (block != ' ') cnt ++;
			}
			block = word;
		}
		System.out.println(cnt);
	}
}