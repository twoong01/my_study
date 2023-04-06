from collections import deque

def bfs(i, j, cnt):
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if not(0 <= nx < n and 0 <= ny < m): continue
            if isvisited[nx][ny]: continue
            if not maps[nx][ny]: continue
            isvisited[nx][ny] = cnt
            q.append((nx, ny))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]
n, m, k = map(int, input().split())
maps = [[0] * m for _ in range(n)]
for _ in range(k):
    i, j = map(int, input().split())
    maps[i - 1][j - 1] = 1
isvisited = [[0] * m for _ in range(n)]
cnt = 1
for i in range(n):
    for j in range(m):
        if not maps[i][j]: continue
        if isvisited[i][j]: continue
        isvisited[i][j] = cnt
        bfs(i, j, cnt)
        cnt += 1
ans = 0
for i in range(1, k + 1):
    total = 0
    for j in isvisited:
        total += j.count(i)
    ans = max(ans, total)
print(ans)