
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;


public class Main {
	
	private static int[][] Map = new int[25][25];
	private static boolean[][] visit = new boolean[25][25];
	private static int dx[] = {-1, 1, 0, 0};
	private static int dy[] = {0, 0, -1, 1};
	private static int n;
	private static int num = 0;
	private static int[] cnt = new int[25*25];
	
	public static void main(String[] args){
    	Scanner sc = new Scanner(System.in);
    	
    	n = sc.nextInt();
    	
    	Map = new int[n][n];
    	
    	for(int i = 0;i < n; i ++) {
    		String input = sc.next();
    		for(int j = 0; j < n; j++) {
    			Map[i][j] = input.charAt(j) - '0';
    		}
    	}
    	for(int i = 0; i < n; i++) {
    		for(int j = 0;j < n; j++) {
    			if(Map[i][j] == 0) continue;
    			if(visit[i][j]) continue;
    			num++;
    			bfs(i, j);
    		}
    	}
    	Arrays.sort(cnt);
    	System.out.println(num);
    	
    	for(int i = 0; i < cnt.length;i++) {
    		if(cnt[i] == 0) {
    		}else{System.out.println(cnt[i]);
    		}
    	}
    	
    	
	}
	static void bfs(int x, int y) {
		Queue<int []> q = new LinkedList<>();
		q.add(new int[] {x, y});
		visit[x][y] = true;
		cnt[num]++;
		
		while(!q.isEmpty()) {
			int curx = q.peek()[0];
			int cury = q.peek()[1];
			q.poll();
			
			for(int k = 0;k<4;k++) {
				int nx = curx + dx[k];
				int ny = cury + dy[k];
				if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue; 
				if (Map[nx][ny] != 1) continue;
				if (visit[nx][ny]) continue;
				q.add(new int[] {nx, ny});
				visit[nx][ny] = true;
				cnt[num]++;
				
			}
			
		}
	}
}