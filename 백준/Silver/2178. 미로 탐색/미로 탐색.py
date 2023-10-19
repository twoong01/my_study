from collections import deque

n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

q = deque()
q.append([0, 0, 1])

while q:
    x, y, cnt = q.popleft()
    if (x, y) == (n - 1, m - 1):
        print(cnt)
        break
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if not(0 <= nx < n and 0 <= ny < m): continue
        if maps[nx][ny] == '0': continue
        q.append([nx, ny, cnt + 1])
        maps[nx][ny] = '0'
