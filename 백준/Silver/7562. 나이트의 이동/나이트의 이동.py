from collections import deque
tc = int(input())

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
for i in range(tc):
    l = int(input())
    cnt = [[0 for _ in range(l)] for _ in range(l)]
    visited = [[False for _ in range(l)] for _ in range(l)]
    a, b = map(int, input().split())
    q = deque()
    q.append([a, b])
    visited[a][b] = True
    target_x, target_y = map(int, input().split())
    while q:
        x, y = q.popleft()
        if x == target_x and y == target_y:
            ans = cnt[x][y]
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l:
                if nx == target_x and ny == target_y:
                    visited[nx][ny] = True
                    cnt[nx][ny] = cnt[x][y] + 1
                    q.append([nx, ny])
                    ans = cnt[nx][ny]
                    break
                else:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append([nx, ny])
                        cnt[nx][ny] = cnt[x][y] + 1
    print(ans)