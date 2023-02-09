from collections import deque
n = int(input())
pic = []
for i in range(n):
    pic.append(list(input()))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()
visited = [[False for _ in range(n)] for _ in range(n)]
ans_1, ans_2 = [], []
for i in range(n):
    for j in range(n):
        cnt = 0
        if (pic[i][j] == 'R' or pic[i][j] == 'G') and not visited[i][j]:
            visited[i][j] = True
            q.append([0, i, j])
        elif pic[i][j] == 'B' and not visited[i][j]:
            visited[i][j] = True
            q.append([1, i, j])
        while q:
            cnt += 1
            color, x, y = q.popleft()
            if not color:
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if pic[nx][ny] == 'R' or pic[nx][ny] == 'G':
                            if not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append([0, nx, ny])
            else:
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if pic[nx][ny] == 'B':
                            if not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append([1, nx, ny])
        if cnt != 0:
            ans_1.append(cnt)
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        cnt = 0
        if pic[i][j] == 'R' and not visited[i][j]:
            visited[i][j] = True
            q.append([0, i, j])
        elif pic[i][j] == 'B' and not visited[i][j]:
            visited[i][j] = True
            q.append([1, i, j])
        elif pic[i][j] == 'G' and not visited[i][j]:
            visited[i][j] = True
            q.append([2, i, j])
        while q:
            cnt += 1
            color, x, y = q.popleft()
            if color == 0:
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if pic[nx][ny] == 'R':
                            if not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append([0, nx, ny])
            elif color == 1:
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if pic[nx][ny] == 'B':
                            if not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append([1, nx, ny])
            else:
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if pic[nx][ny] == 'G':
                            if not visited[nx][ny]:
                                visited[nx][ny] = True
                                q.append([2, nx, ny])
        if cnt != 0:
            ans_2.append(cnt)
print(len(ans_2), len(ans_1))