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
            isvisited[i][j] = -3
        if Map[i][j] == 1:
            isvisited[i][j] = -2
cnt = 0
for i in range(n):
    cnt += isvisited[i].count(-1)
if cnt == 0:
    print(0)
    exit()
order = []
for i in combinations(virus, m):
    order.append(i)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 1e9
can = True
for v in order:
    visit = copy.deepcopy(isvisited)
    visit_num = 0
    for x, y in v:
        visit[x][y] = 0
    q = deque()
    tmp = copy.deepcopy(v)
    q.extend(tmp)
    for i in range(len(q)):
        q[i].append(visit_num)
    while q:
        x, y, visit_num = q.popleft()  
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if not(0 <= nx < n and 0 <= ny < n): continue
            if visit[nx][ny] >= 0: continue
            if isvisited[nx][ny] == -2: continue
            if visit[nx][ny] == -4: continue
            if isvisited[nx][ny] == -3:
                visit[nx][ny] = -4
                q.append([nx, ny, visit_num + 1])
            else:
                visit[nx][ny] = visit_num + 1
                q.append([nx, ny, visit_num + 1])
    tmp = 0
    for i in range(n):
        if -1 in visit[i]:
            can = False
            break
        else:
            tmp = max(tmp, max(visit[i]))
            can = True
    if can:
        ans = min(ans, tmp)
print(ans if ans != 1e9 else -1)