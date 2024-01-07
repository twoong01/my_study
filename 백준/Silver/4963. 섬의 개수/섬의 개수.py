from collections import deque

def BFS(x, y):
    q = deque()
    q.append([x, y])
    maps[y][x] = 0

    while q:
        cx, cy = q.popleft()
        for k in range(8):
            nx = cx + dx[k]
            ny = cy + dy[k]
            if not(0 <= nx < n and 0 <= ny < m): continue
            if maps[ny][nx] == 0: continue
            q.append([nx, ny])
            maps[ny][nx] = 0

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]

while True:
    n, m = map(int, input().split())
    cnt = 0
    if n == 0 and m == 0:
        break
    maps = [list(map(int, input().split())) for _ in range(m)]
    for i in range(n):
        for j in range(m):
            if maps[j][i]:
                BFS(i, j)
                cnt += 1
    print(cnt)
