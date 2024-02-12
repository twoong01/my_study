from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

visited = [[-1 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

for i in range(n):
    for j in range(m):
        if maps[i][j] == 2:
            q.append([i, j])
            visited[i][j] = 0
        elif maps[i][j] == 0:
            visited[i][j] = 0

while q:
    x, y = q.popleft()

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if not(0 <= nx < n and 0 <= ny < m): continue
        if maps[nx][ny] == 0: continue
        if visited[nx][ny] != -1: continue
        q.append([nx, ny])
        visited[nx][ny] = visited[x][y] + 1

for i in range(n):
    print(*visited[i])