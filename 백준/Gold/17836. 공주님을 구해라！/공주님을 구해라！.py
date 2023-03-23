from collections import deque
n, m, t = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if Map[i][j] == 2:
            gram = (i, j)

gram_to_p = (n - 1 - gram[0]) + (m - 1 - gram[1])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append((0, 0))
visited[0][0] = 0
ans = -1
flag = False
while q:
    x, y = q.popleft()
    if (x, y) == (n - 1, m - 1):
        ans = 0
        break
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if not(0 <= nx < n and 0 <= ny < m): continue
        if visited[nx][ny] != -1: continue
        if Map[nx][ny] == 1: continue
        if Map[nx][ny] == 2:
            flag = True
            ans = 0
        visited[nx][ny] = visited[x][y] + 1
        q.append((nx, ny))

if ans != -1:
    if flag:
        tmp = visited[gram[0]][gram[1]] + gram_to_p
        if tmp <= t:
            if visited[n - 1][m - 1] == -1:
                ans = tmp
            elif tmp > visited[n - 1][m - 1]:
                ans = visited[n - 1][m - 1]
            else:
                ans = tmp
        else:
            ans = 'Fail'
    else:
        ans = visited[n - 1][m - 1]
else:
    ans = 'Fail'
print(ans)