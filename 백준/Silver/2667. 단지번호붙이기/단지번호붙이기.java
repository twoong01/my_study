import java.util.*;
import java.io.*;

public class Main {
	static List<Integer> lst;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		
		int n = Integer.parseInt(br.readLine());
		
		int[][] maps = new int[n][n];
		for(int i = 0; i < n; i ++) {
			char[] t = br.readLine().toCharArray();
			for(int j = 0; j < n;j ++) {
				maps[i][j] = t[j] - '0';
			}
		}
		
		lst = new ArrayList<>();
		
		int[] dx;
		int[] dy;
		dx = new int[] {-1, 1, 0, 0};
		dy = new int[] {0, 0, -1, 1};
		boolean[][] isvisited = new boolean[n][n];
		int total_cnt = 0;
		
		Queue<Point> q = new LinkedList<Point>();
		
		for(int i = 0; i < n;i++) {
			for(int j = 0; j < n; j++) {
				if(maps[i][j] == 0) continue;
				if(isvisited[i][j]) continue;
				q.add(new Point(i, j));
				isvisited[i][j] = true;
				int cnt = 1;
				while(!q.isEmpty()) {
					Point p = q.poll();
					int x = p.x;
					int y = p.y;
					for(int k = 0; k < 4;k++) {
						int nx = x + dx[k];
						int ny = y + dy[k];
						if (!(0 <= nx && nx < n && 0 <= ny && ny < n)) continue;
						if (isvisited[nx][ny]) continue;
						if (maps[nx][ny] == 0) continue;
						q.add(new Point(nx, ny));
						isvisited[nx][ny] = true;
						cnt ++;
					}
				}
				
				total_cnt ++;
				lst.add(cnt);
			}
		}
		
		Collections.sort(lst);
		
		System.out.println(total_cnt);
		for(int i = 0; i < lst.size(); i++) {
			System.out.println(lst.get(i));
		}
	}
	static class Point{
		int x, y;
		
		public Point(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
}