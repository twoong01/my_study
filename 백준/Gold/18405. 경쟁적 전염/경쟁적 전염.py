from collections import deque

n, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
s, ans_x, ans_y = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
isvisited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if maps[i][j]:
            q.append((i, j, maps[i][j], 1))
q = sorted(q, key=lambda x : x[2])
q = deque(q)
while q:
    x, y, num, time = q.popleft()
    if time > s:
        break
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if not(0 <= nx < n and 0 <= ny < n): continue
        if isvisited[nx][ny]: continue
        if maps[nx][ny]: continue
        maps[nx][ny] = num 
        q.append((nx, ny, num, time + 1))
        isvisited[nx][ny] = True
print(maps[ans_x - 1][ans_y - 1])