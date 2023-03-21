from collections import deque
t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(t):
    m, n = map(int, input().split())
    Map = [list(input()) for _ in range(n)]
    visited = [[-1] * m for _ in range(n)]
    ans = []
    fire, start = [], []
    for i in range(n):
        for j in range(m):
            if Map[i][j] == '@':
                start.append((i, j, 1))
                visited[i][j] = 0
                ans.append([i, j, 0])
            if Map[i][j] == '*':
                fire.append((i, j, 0))
                visited[i][j] = 0 
            if Map[i][j] == '#':
                visited[i][j] = '#'

    q = deque()
    if fire:
        q.extend(fire)
    if start:
        q.extend(start)
    while q:
        x, y, who = q.popleft()
        for i in range(4):
            nx = x + dx[i] # 행
            ny = y + dy[i] # 열
            if 0 <= nx < n and 0 <= ny < m:
                if who == 1:
                    if visited[nx][ny] == -1:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append([nx, ny, 1])
                        ans.append([nx, ny, visited[nx][ny]])
                else:
                    if visited[nx][ny] == -1:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append([nx, ny, 0])
    rlt = []
    for i in ans:
        if i[0] == n - 1 or i[1] == m - 1 or i[0] == 0 or i[1] == 0:
            rlt.append(i)
    if len(rlt) != 0:
        rlt.sort(key=lambda x : x[2])
        print(rlt[0][2] + 1)
    else:
        print("IMPOSSIBLE")