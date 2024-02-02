import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
maps = [list(map(str, input().rstrip())) for _ in range(r)]

q = deque()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
ans = []
visited = [[-1 for _ in range(c)] for _ in range(r)]

for i in range(r):
    for j in range(c):
        if maps[i][j] == '*':
            q.append([i, j, 1])
            visited[i][j] = 0
        elif maps[i][j] == 'D':
            target = [i, j]

for i in range(r):
    for j in range(c):
        if maps[i][j] == 'S':
            q.append([i, j, 0])
            visited[i][j] = 0

while q:
    x, y, who = q.popleft()


    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if not(0 <= nx < r and 0 <= ny < c): continue
        if visited[nx][ny] != -1: continue
        if maps[nx][ny] == '*': continue
        if maps[nx][ny] == 'X': continue

        if who == 0:
            visited[nx][ny] = visited[x][y] + 1
            q.append([nx, ny, 0])
            ans.append([nx, ny, visited[nx][ny]])
        else:
            if maps[nx][ny] == 'D': continue
            visited[nx][ny] = visited[x][y] + 1
            q.append([nx, ny, 1])

for i in ans:
    if [i[0], i[1]] == target:
        print(i[2])
        break
else:
    print('KAKTUS')