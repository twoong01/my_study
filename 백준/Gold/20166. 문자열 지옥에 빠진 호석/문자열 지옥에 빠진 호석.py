
from collections import deque
n, m, k = map(int, input().split())
world = [list(input()) for _ in range(n)]
god = [input() for _ in range(k)]

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]
like = dict()

def bfs(i, j):
    q = deque()
    q.append([i, j, world[i][j]])
    while q:
        x, y, word = q.popleft()
        if word not in like:
            like.setdefault(word, 1)
        else:
            like[word] += 1
        if len(word) > 5:
            continue
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0:
                nx = n - 1
            if ny < 0:
                ny = m - 1
            if nx >= n:
                nx = 0
            if ny >= m:
                ny = 0
            q.append([nx, ny, word + world[nx][ny]])

            

cnt =  [[] for _ in range(k)]
for i in range(n):
    for j in range(m):
        bfs(i, j)

for k in god:
    if k in like:
        print(like[k])
    else:
        print(0)
