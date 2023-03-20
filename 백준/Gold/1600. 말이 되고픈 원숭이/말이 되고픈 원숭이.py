from collections import deque
g = int(input())
m, n = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]
isvisited = [[-1 for _ in range(m)] for _ in range(n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

h_dx = [-2, -2, -1, -1, 1, 1, 2, 2]
h_dy = [-1, 1, -2, 2, -2, 2, -1, 1]

q = deque()
q.append((0, 0, g, 0))
isvisited[0][0] = 1

while q:
    x, y, horse, total = q.popleft()
    if (x, y) == (n - 1, m - 1):
        print(total)
        break
    if horse >= 1:
        for k in range(8):
            nx, ny = x + h_dx[k], y + h_dy[k]
            if not(0 <= nx < n and 0 <= ny < m): continue
            if Map[nx][ny] == 1: continue
            if isvisited[nx][ny] < horse - 1:
                isvisited[nx][ny] = horse - 1
                q.append((nx, ny, horse - 1, total + 1))
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if not(0 <= nx < n and 0 <= ny < m): continue
        if Map[nx][ny] == 1: continue
        if isvisited[nx][ny] < horse:
            isvisited[nx][ny] = horse
            q.append((nx, ny, horse, total + 1))
else:
    print(-1)