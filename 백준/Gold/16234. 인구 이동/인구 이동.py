def bfs(sx, sy):
    global changed
    open_countries =[[sx, sy]]
    population = people[sx][sy]
    q = deque()
    q.append([sx, sy])
    isvisited[sx][sy] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if not(0 <= nx < n and 0 <= ny < n): continue
            if not isvisited[nx][ny]:
                if l <= abs(people[x][y] - people[nx][ny]) <= r:
                    q.append([nx, ny])
                    isvisited[nx][ny] = True
                    population += people[nx][ny]
                    open_countries.append([nx, ny])
    if len(open_countries) >= 2:
        changed = True
        new = population // len(open_countries)
        for i in open_countries:
            people[i[0]][i[1]] = new

from collections import deque
n, l, r = map(int, input().split())
people = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
time = 0
changed = True
while changed:
    changed = False
    population = 0
    isvisited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not isvisited[i][j]:
                bfs(i, j)
    if changed:
        time += 1
print(time)