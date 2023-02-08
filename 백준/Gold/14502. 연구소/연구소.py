import sys



input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
origin_lab = []
ex_lab = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    origin_lab.append(list(map(int, input().split())))

di = [-1, 1, 0, 0] # 상하좌우
dj = [0, 0, -1, 1]
q = deque()
result = 0
def bfs():
    global result
    for i in range(n):
        for j in range(m):
            ex_lab[i][j] = origin_lab[i][j]
            if ex_lab[i][j] == 2:
                 q.append([i, j])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]
            if 0 <= nx < n and 0 <= ny < m:
                if ex_lab[nx][ny] == 0:
                    ex_lab[nx][ny] = 2
                    q.append([nx, ny])
    ans = 0
    for i in ex_lab:
         ans += i.count(0)
    result = max(ans, result)
    return
def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if origin_lab[i][j] == 0:
                origin_lab[i][j] = 1
                wall(cnt + 1)
                origin_lab[i][j] = 0

wall(0)
print(result)