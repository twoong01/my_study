
from collections import deque
from itertools import combinations
import copy
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]
isvisited = [[-1] * n for _ in range(n)]
virus = []
for i in range(n):
    for j in range(n):
        if Map[i][j] == 2:
            virus.append([i, j])
        if Map[i][j] == 1:
            isvisited[i][j] = -2
order = []
for i in combinations(virus, m):
    order.append(i)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 1e9
for v in order:
    visit = copy.deepcopy(isvisited)
    for x, y in v:
        visit[x][y] = 0
    q = deque()
    q.extend(v)
    while q:
        x, y = q.popleft()  
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if not(0 <= nx < n and 0 <= ny < n): continue
            if visit[nx][ny] != -1: continue
            if isvisited[nx][ny] == -2: continue
            visit[nx][ny] = visit[x][y] + 1
            q.append([nx, ny])
    tmp = 0
    can = True
    for i in range(n):
        if -1 in visit[i]:
            can = False
            break
        else:
            tmp = max(tmp, max(visit[i]))
    if can:
        ans = min(ans, tmp)
print(ans if ans != 1e9 else -1)