from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(sx, sy, arr, len_list):
    q = deque()
    isvisited = [[False] * n for _ in range(m)]

    q.append([sx, sy, 0])
    isvisited[sx][sy] = True

    while q:
        x, y, cnt = q.popleft()
        if arr[x][y] not in ['.', 'x'] and (x != sx or y != sy):
            point = int(arr[x][y])
            len_list[point] = cnt

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if not(0 <= nx < m and 0 <= ny < n): continue
            if arr[nx][ny] == 'x': continue
            if not isvisited[nx][ny]:
                isvisited[nx][ny] = True
                q.append([nx, ny, cnt + 1])
    return len_list

def search_ans(len_list, now, visited_cnt, cnt, visited):
    if visited_cnt == len(len_list):
        global ans
        ans = min(ans, cnt)
        return
    for nxt in range(len(len_list)):
        if len_list[now][nxt] == 0 or visited[nxt]:
            continue
        visited[nxt] = True
        search_ans(len_list, nxt, visited_cnt + 1, cnt + len_list[now][nxt], visited)
        visited[nxt] = False

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    sx, sy = -1, -1
    start = []
    Map = []
    point_num = 0
    for i in range(m):
        Map.append(list(input().strip()))
        for j in range(n):
            if Map[i][j] == 'o':
                sx, sy = i, j
                start.append([i, j])
                Map[i][j] = str(point_num)
                point_num += 1
            elif Map[i][j] == '*':
                start.append([i, j])
                Map[i][j] = str(point_num)
                point_num += 1
    len_list = [[] for _ in range(len(start))]
    ans = 10000
    start_point = int(Map[sx][sy])
    for x, y in start:
        point = int(Map[x][y])
        len_list[point] = bfs(x, y, Map, [0] * len(start))

    visited = [False] * len(len_list)
    visited[start_point] = True
    search_ans(len_list, start_point, 1, 0, visited)
    print(ans if ans != 10000 else -1)