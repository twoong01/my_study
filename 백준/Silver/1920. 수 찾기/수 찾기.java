import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int a = Integer.parseInt(br.readLine());
		int[] a_lst = new int[a];
		StringTokenizer st = new StringTokenizer(br.readLine());
		for(int i = 0; i < a; i++) {
			a_lst[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(a_lst);
		int b = Integer.parseInt(br.readLine());
		int[] b_lst = new int[b];
		StringTokenizer st1 = new StringTokenizer(br.readLine());
		for(int i = 0; i < b; i++) {
			b_lst[i] = Integer.parseInt(st1.nextToken());
		}
		
		for(int i = 0; i < b_lst.length; i ++) {
			int start = 0;
			int end = a_lst.length - 1;
			int target = b_lst[i];
			int ans = 0;
			
			while(start <= end) {
				int mid = (start + end) / 2;
				
				if(a_lst[mid] > target) {
					end = mid - 1;
				}else if(a_lst[mid] < target) {
					start = mid + 1;
				}else {
					ans = 1;
					break;
				}
			}
			System.out.println(ans);
		}
	}
}