from collections import deque
n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dis = set()
q = deque()
for i in range(n):
    for j in range(m):
        isvisited = [[False] * m for _ in range(n)]
        if maps[i][j] == 'W': continue
        q.append((i, j, 0))
        isvisited[i][j] = True
        while q:
            x, y, distance = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if not(0 <= nx < n and 0 <= ny < m): continue
                if isvisited[nx][ny]: continue
                if maps[nx][ny] == 'W': continue
                q.append((nx, ny, distance + 1))
                isvisited[nx][ny] = True
        dis.add(distance)
print(max(dis))