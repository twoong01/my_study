from collections import deque

def mark(i, j):
    q = deque()
    q.append((i, j))
    country[i][j] = country_cnt
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if not(0 <= nx < n and 0 <= ny < m): continue
            if not maps[nx][ny]: continue
            if country[nx][ny]: continue
            q.append((nx, ny))
            country[nx][ny] = country_cnt

def make_bridge(x, y, now):
    q = deque()
    for direction in range(4):
        q.append((x, y, 0, direction))
    while q:
        i, j, cnt, nowDir = q.popleft()
        if country[i][j] != 0 and country[i][j] != now:
            if cnt > 2:
                nodes.add((cnt - 1, now, country[i][j]))
            continue
        ni, nj = i + dx[nowDir], j + dy[nowDir]
        if not(0 <= ni < n and 0 <= nj < m): continue
        if country[ni][nj] == now: continue
        q.append((ni, nj, cnt + 1, nowDir))

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 나라 마킹
country_cnt = 1
country = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not maps[i][j]: continue
        if country[i][j]: continue
        mark(i, j)
        country_cnt += 1

# 다리 만들기
nodes = set()
for i in range(n):
    for j in range(m):
        if country[i][j] != 0:
            visited = [[False] * m for _ in range(n)]
            make_bridge(i, j, country[i][j])

nodes = list(nodes)
nodes.sort()

def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        parents[y] = parents[x]
    else:
        parents[x] = parents[y]

def find(k):
    if k != parents[k]:
        parents[k] = find(parents[k])
    return parents[k]

ans = 0
cnt = 0
parents = [i for i in range(country_cnt)]
for cost, a, b in nodes:
    if find(a) != find(b):
        cnt += 1
        union(a, b)
        ans += cost

if ans == 0 or cnt != country_cnt - 2:
    print(-1)
else:
    print(ans)