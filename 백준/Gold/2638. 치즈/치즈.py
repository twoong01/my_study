from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    q = deque()
    q.append([i, j])
    is_visited[i][j] = 1

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if not(0 <= nx < n and 0 <= ny < m): continue
            if maps[nx][ny] == 0 and is_visited[nx][ny] == 0:
                is_visited[nx][ny] = 1
                q.append([nx, ny])
            elif maps[nx][ny]:
                is_visited[nx][ny] += 1

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
hour = 0
while True:
    is_visited = [[0 for _ in range(m)] for _ in range(n)]
    bfs(0, 0)
    hour += 1

    for i in range(n):
        for j in range(m):
            if is_visited[i][j] >= 2:
                maps[i][j] = 0
    
    air_cnt = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                air_cnt += 1
    if air_cnt == n * m:
        break
print(hour)