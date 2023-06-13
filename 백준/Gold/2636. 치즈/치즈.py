from collections import deque

def bfs():
    q = deque([(0, 0)])
    melt = deque([])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if not(0 <= nx < n and 0 <= ny < m): continue
            if visited[nx][ny]: continue
            visited[nx][ny] = True
            if maps[nx][ny] == 0:
                q.append((nx, ny))
            else:
                melt.append((nx, ny))
    for x, y in melt:
        maps[x][y] = 0
    return len(melt)


n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
total = 0
for i in range(n):
    total += sum(maps[i])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

time = 1
while True:
    visited = [[False for _ in range(m)] for _ in range(n)]
    meltcnt = bfs()
    total -= meltcnt
    if total == 0:
        break
    time += 1
print(time)
print(meltcnt)