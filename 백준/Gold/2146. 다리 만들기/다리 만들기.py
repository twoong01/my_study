from collections import deque
n = int(input())
Map = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def mark(i, j):
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if not(0 <= nx < n and 0 <= ny < n): continue
            if Map[nx][ny] == 0: continue
            if visited[nx][ny]: continue
            visited[nx][ny] = country
            q.append((nx, ny))

def find_edge():
    edge = [set() for _ in range(country - 1)]
    for i in range(n):
        for j in range(n):
            if Map[i][j] == 0: continue
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if not(0 <= nx < n and 0 <= ny < n): continue
                if Map[nx][ny] == 0:
                    edge[visited[i][j] - 1].add((i, j))
    return edge

def make_bridge(i, j, num):
    global mn_bridge
    q = deque()
    q.append((i, j))
    bridge = [[0] * n for _ in range(n)]
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if not(0 <= nx < n and 0 <= ny < n): continue
            if Map[nx][ny] != 0:
                if visited[nx][ny] != num:
                    mn_bridge = min(mn_bridge, bridge[x][y])
                    continue
            if bridge[nx][ny]: continue
            if visited[nx][ny] == country: continue
            bridge[nx][ny] = bridge[x][y] + 1
            q.append((nx, ny))


country = 1
for i in range(n):
    for j in range(n):
        if visited[i][j]: continue
        if Map[i][j] == 0: continue
        visited[i][j] = country
        mark(i, j)
        country += 1
edge_lst = find_edge()

mn_bridge = 1e9
for i in edge_lst:
    for x, y in i:
        country = visited[x][y]
        make_bridge(x, y, country)
print(mn_bridge)