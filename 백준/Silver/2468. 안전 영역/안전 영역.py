from collections import deque
n = int(input())
Map = [list(map(int, input().split())) for _ in range(n)]


def bfs(i, j):
    q = deque()
    q.append((i, j))
    visited[i][j] = country
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if not(0 <= nx < n and 0 <= ny < n): continue
            if visited[nx][ny]: continue
            if Map[nx][ny] == -1: continue
            visited[nx][ny] = country
            q.append((nx, ny))


def check():
    cnt = 0
    for i in Map:
        cnt += i.count(-1)
    if cnt == n**2:
        return False
    return True

mx_area = -1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
rain = 0
while True:
    visited = [[0] * n for _ in range(n)]
    country = 1
    for i in range(n):
        for j in range(n):
            if Map[i][j] <= rain:
                Map[i][j] = -1
    if not check():
        break


    for i in range(n):
        for j in range(n):
            if Map[i][j] == -1: continue
            if visited[i][j]: continue
            bfs(i, j)
            country += 1
            for row in visited:
                mx_area = max(mx_area, max(row))
    rain += 1
print(mx_area)
