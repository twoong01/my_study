import java.util.*;
import java.io.*;
import java.lang.reflect.Array;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int t = Integer.parseInt(br.readLine());
        for(int test = 0; test < t; test++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int m = Integer.parseInt(st.nextToken());
            int n = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            
            int[][] maps = new int[m][n];
            for(int i = 0; i < m; i ++) {
                Arrays.fill(maps[i], 0);
            }
            for(int l = 0; l < k; l++) {
                StringTokenizer st1 = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st1.nextToken());
                int y = Integer.parseInt(st1.nextToken());
                maps[x][y] = 1;
            }
            int[] dx;
            int[] dy;
            dx = new int[] {-1, 1, 0, 0};
            dy = new int[] {0, 0, -1, 1};
            
            Queue<Point> q = new LinkedList<Point>();
            boolean[][] isvisited = new boolean[m][n];
            for(int i = 0; i < m; i ++) {
                Arrays.fill(isvisited[i], false);
            }
            int cnt = 0;
            for(int i = 0; i < m; i ++) {
                for(int j = 0; j < n; j ++) {
                    if (maps[i][j] == 0) continue;
                    if (isvisited[i][j]) continue;
                    q.add(new Point(i, j));
                    cnt += 1;
                    while(!q.isEmpty()) {
                        Point p = q.poll();
                        int x = p.x;
                        int y = p.y;
                        for(int dir=0;dir < 4; dir ++) {
                            int nx = x + dx[dir];
                            int ny = y + dy[dir];
                            if (!(0 <= nx && nx < m && 0 <= ny && ny < n)) continue;
                            if (maps[nx][ny] == 0) continue;
                            if (isvisited[nx][ny] == true) continue;
                            q.add(new Point(nx, ny));
                            isvisited[nx][ny] = true;
                        }
                    }
                }
            }
            System.out.println(cnt);
        }
        
    }
    static class Point {
        int x, y;
        
        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}