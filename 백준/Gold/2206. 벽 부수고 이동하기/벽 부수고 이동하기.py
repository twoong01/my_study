from collections import deque
n, m = map(int, input().split())
Map = [list(map(int, input())) for _ in range(n)]

wall_break = 0
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
que = deque()
que.append((0, 0, 0))
visited[0][0][0] = 1

while que:
    x, y, z = que.popleft()
    if x == n - 1 and y == m - 1:
        print(visited[x][y][z])
        break
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if not(0 <= nx < n and 0 <= ny < m): continue
        if Map[nx][ny] == 1 and z == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                que.append((nx, ny, 1))
        elif Map[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                que.append((nx, ny, z))
else:
    print(-1)
