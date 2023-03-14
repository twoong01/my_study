import sys
from collections import deque
n, m, k = map(int, sys.stdin.readline().split())
Map = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[[0] * m for _ in range(n)] for _ in range(k + 1)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def bfs():
    q = deque()
    q.append((0, 0, 0, 1))
    for i in range(k + 1):
        visited[i][0][0] = 1
    while q:
        x, y, z, total = q.popleft()
        if x == n - 1 and y == m - 1:
            return total
        for l in range(4):
            nx = x + dx[l]
            ny = y + dy[l]
            if not(0 <= nx < n and 0 <= ny < m): continue
            if Map[nx][ny] == 1 and z < k and visited[z + 1][nx][ny] == 0:
                visited[z + 1][nx][ny] = 1
                q.append((nx, ny, z + 1, total + 1))
            elif Map[nx][ny] == 0 and visited[z][nx][ny] == 0:
                visited[z][nx][ny] = 1
                q.append((nx, ny, z, total + 1))
    return -1
print(bfs())