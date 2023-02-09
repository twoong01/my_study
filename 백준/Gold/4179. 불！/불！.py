from collections import deque

r, c = map(int, input().split()) # 행, 열
maze = []
q = deque()
visited = [[-1 for _ in range(c)] for _ in range(r)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
ans = []

for i in range(r):
    maze.append(list(input()))
    for j in range(c):
        if maze[i][j] == 'F':
            q.append([0, i, j])
            visited[i][j] = 0
        elif maze[i][j] == 'J':
            q.append([1, i, j])
            visited[i][j] = 0
            ans.append([i, j, visited[i][j]])
        elif maze[i][j] == '#':
            visited[i][j] = '#'
q.reverse()
while q:
    who, x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i] # 행
        ny = y + dy[i] # 열
        if 0 <= nx < r and 0 <= ny < c:
            if who == 1:
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([1, nx, ny])
                    ans.append([nx, ny, visited[nx][ny]])
            else:
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append([0, nx, ny])
result = []
for i in ans:
    if i[0] == r - 1 or i[1] == c - 1 or i[1] == 0 or i[0] == 0:
        result.append(i)
if len(result) != 0:
    result = sorted(result, key=lambda x : x[2])
    print(result[0][2] + 1)
else:
    print('IMPOSSIBLE')